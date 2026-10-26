#!/usr/bin/env python3
"""Replace inline response schemas by $refs to the named models in components/schemas.

Why: the Kitsu spec defines Asset, Shot, Task, ... under components/schemas but every
endpoint re-describes its response inline, so openapi-generator reports the models as
unused and emits throw-away classes (GetAssets200ResponseInner, ...).

A response schema is linked to a model only when BOTH checks agree:
  1. Shape: every shared property has a compatible type, the model has no `required`
     field missing from the response, and at least --min-props properties are shared
     and --min-coverage of the response's properties exist on the model.
  2. Name:  the model's name appears in the operation (summary first, then the last
     path segment); the match closest to the end of the phrase wins, since the head
     noun comes last ("Get asset tasks" -> Task, "Get asset task types" -> TaskType).

If the name matches several models equally, or only matches a model whose shape
disagrees, the response stays inline and is listed in the report.

Properties a response has but the model lacks (project_name, ...) are added to the
model as optional fields (disable with --strict). Request bodies are never linked:
the inline request schemas are more precise than the full model (they carry `required`).

Usage:
    python link_models.py openapi.fixed.json openapi.linked.json \
        [--strict] [--min-props 3] [--min-coverage 0.6] \
        [--overrides overrides.json] [--report links.json]

overrides.json maps "<method> <path>" to a model name, or to null to forbid linking:
    {"get /data/assets/{asset_id}/cast-in": "Shot", "get /data/foo": null}
"""
from __future__ import annotations

import argparse
import copy
import json
import re
from typing import Any, Iterator

HTTP = {"get", "put", "post", "delete", "patch", "options", "head", "trace"}
REF = "#/components/schemas/"
_MISSING = object()


# --------------------------------------------------------------------------- #
# Name matching
# --------------------------------------------------------------------------- #
def singular(w: str) -> str:
    if len(w) > 4 and w.endswith("ies"):
        return w[:-3] + "y"
    if w.endswith(("sses", "uses", "xes", "ches", "shes")):
        return w[:-2]
    if w.endswith(("ss", "us", "is")):
        return w
    if w.endswith("s") and len(w) > 3:
        return w[:-1]
    return w


def words(text: str) -> list[str]:
    text = re.sub(r"(?<=[a-z0-9])(?=[A-Z])", " ", text)  # split CamelCase
    return [singular(w) for w in re.findall(r"[a-z0-9]+", text.lower())]


def last_match_end(seq: list[str], sub: list[str]) -> int:
    n, best = len(sub), -1
    for i in range(len(seq) - n + 1):
        if seq[i:i + n] == sub:
            best = i + n - 1
    return best


def best_by_hint(cands: dict[str, list[str]], seq: list[str]) -> list[str]:
    """Models whose name occurs in `seq`; the latest (head noun), then longest, wins."""
    scored = []
    for name, toks in cands.items():
        end = last_match_end(seq, toks)
        if end >= 0:
            scored.append(((end, len(toks)), name))
    if not scored:
        return []
    top = max(k for k, _ in scored)
    return sorted(n for k, n in scored if k == top)


# --------------------------------------------------------------------------- #
# Shape matching
# --------------------------------------------------------------------------- #
def props_of(schema: Any) -> dict[str, Any] | None:
    if not isinstance(schema, dict):
        return None
    props = dict(schema.get("properties") or {})
    for part in schema.get("allOf") or []:
        if isinstance(part, dict) and "$ref" not in part:
            props.update(part.get("properties") or {})
    return props or None


def types_compatible(a: Any, b: Any) -> bool:
    if not isinstance(a, dict) or not isinstance(b, dict):
        return True
    ta, tb = a.get("type"), b.get("type")
    if "$ref" in a or "$ref" in b or ta is None or tb is None or ta == tb:
        return True
    return {ta, tb} <= {"integer", "number"}


def evaluate(P: dict, model: dict, mprops: dict, min_props: int, min_cov: float):
    shared = [k for k in P if k in mprops]
    conflicts = sorted(k for k in shared if not types_compatible(P[k], mprops[k]))
    required = model.get("required")
    missing = sorted(set(required) - set(P)) if isinstance(required, list) else []
    cov = len(shared) / len(P)
    reason = None
    if conflicts:
        reason = f"type conflict on {', '.join(conflicts)}"
    elif missing:
        reason = f"model requires {', '.join(missing)}"
    elif len(shared) < min_props:
        reason = f"only {len(shared)} shared properties"
    elif cov < min_cov:
        reason = f"coverage {cov:.0%} below {min_cov:.0%}"
    return reason is None, reason, cov


# --------------------------------------------------------------------------- #
# Spec traversal
# --------------------------------------------------------------------------- #
def iter_targets(op: dict[str, Any]) -> Iterator[tuple[str, dict, str, bool]]:
    """Yield (status, container, key, is_list); container[key] is the schema to replace."""
    for code, r in (op.get("responses") or {}).items():
        if not str(code).startswith("2") or not isinstance(r, dict):
            continue
        for mt, media in (r.get("content") or {}).items():
            if "json" not in mt or not isinstance(media, dict):
                continue
            sch = media.get("schema")
            if not isinstance(sch, dict):
                continue
            if sch.get("type") == "array" and isinstance(sch.get("items"), dict):
                yield str(code), sch, "items", True
            else:
                yield str(code), media, "schema", False


def refs_in(node: Any) -> Iterator[str]:
    if isinstance(node, dict):
        r = node.get("$ref")
        if isinstance(r, str) and r.startswith(REF):
            yield r[len(REF):]
        for v in node.values():
            yield from refs_in(v)
    elif isinstance(node, list):
        for v in node:
            yield from refs_in(v)


def reachable_models(spec: dict[str, Any]) -> set[str]:
    schemas = spec.get("components", {}).get("schemas", {})
    seen: set[str] = set()
    stack = list(refs_in(spec.get("paths", {})))
    while stack:
        n = stack.pop()
        if n in seen or n not in schemas:
            continue
        seen.add(n)
        stack.extend(refs_in(schemas[n]))
    return seen


# --------------------------------------------------------------------------- #
def link_models(
    spec: dict[str, Any],
    strict: bool = False,
    min_props: int = 3,
    min_coverage: float = 0.6,
    overrides: dict[str, str | None] | None = None,
    verbose: bool = True,
) -> dict[str, Any]:
    overrides = overrides or {}
    min_cov = 1.0 if strict else min_coverage
    schemas = spec.get("components", {}).get("schemas", {})
    models = {n: (s, p) for n, s in schemas.items() if (p := props_of(s))}
    tokens = {n: words(n) for n in models}
    original_props = {n: set(p) for n, (_, p) in models.items()}

    # ---- pass 1: decide against the ORIGINAL models (order independent) ---------
    decisions: list[dict[str, Any]] = []
    unlinked: list[dict[str, Any]] = []

    for path, item in spec.get("paths", {}).items():
        if not isinstance(item, dict):
            continue
        segs = [s for s in path.split("/") if s and not s.startswith("{")]
        path_seq = words(segs[-1]) if segs else []
        for method, op in item.items():
            if method not in HTTP or not isinstance(op, dict):
                continue
            label = f"{method} {path}"
            summary_seq = words(op.get("summary") or "")
            for code, container, key, is_list in iter_targets(op):
                obj = container[key]
                P = obj.get("properties") if isinstance(obj, dict) and "$ref" not in obj else None
                if not isinstance(P, dict) or not P:
                    continue
                entry = {"operation": label, "status": code, "list": is_list}

                forced = overrides.get(label, _MISSING)
                if forced is None:
                    unlinked.append({**entry, "why": "override: do not link"})
                    continue
                if forced is not _MISSING:
                    if forced not in models:
                        unlinked.append({**entry, "why": f"override names unknown model {forced!r}"})
                        continue
                    _, mprops = models[forced]
                    conflicts = [k for k in P if k in mprops and not types_compatible(P[k], mprops[k])]
                    if conflicts:
                        unlinked.append({**entry, "why": f"override {forced}: type conflict on {conflicts}"})
                        continue
                    decisions.append({**entry, "container": container, "key": key, "model": forced,
                                      "props": P, "via": "override"})
                    continue

                results = {n: evaluate(P, s, mp, min_props, min_cov) for n, (s, mp) in models.items()}
                ok = {n: tokens[n] for n, (good, _, _) in results.items() if good}

                chosen, via, ambiguous = None, "", None
                for seq, source in ((summary_seq, "summary"), (path_seq, "path")):
                    best = best_by_hint(ok, seq)
                    if len(best) == 1:
                        chosen, via = best[0], source
                        break
                    if len(best) > 1:
                        ambiguous = best
                        break

                if chosen:
                    decisions.append({**entry, "container": container, "key": key, "model": chosen,
                                      "props": P, "via": via})
                    continue

                # explain why it stayed inline
                if ambiguous:
                    why = f"ambiguous name match: {', '.join(ambiguous)}"
                else:
                    hinted = best_by_hint({n: tokens[n] for n in models}, summary_seq) or \
                             best_by_hint({n: tokens[n] for n in models}, path_seq)
                    if hinted:
                        n = hinted[0]
                        why = f"name suggests {n} but shape rejects it ({results[n][1]})"
                    else:
                        why = "no model name found in summary or path"
                near = sorted(((r[2], n) for n, r in results.items() if r[2] >= min_cov),
                              reverse=True)[:2]
                unlinked.append({**entry, "why": why,
                                 "closest_by_shape": [f"{n} ({c:.0%})" for c, n in near]})

    # ---- pass 2: apply ---------------------------------------------------------------
    linked: list[dict[str, Any]] = []
    extended: dict[str, set[str]] = {}
    for d in decisions:
        name, P = d["model"], d["props"]
        mprops = models[name][1]
        extras = [k for k in P if k not in mprops]
        clash = [k for k in P if k in mprops and k not in original_props[name]
                 and not types_compatible(P[k], mprops[k])]
        if clash:  # an earlier endpoint added this field with another type
            unlinked.append({"operation": d["operation"], "status": d["status"],
                             "why": f"{name}: field type clash on {clash}"})
            continue
        for k in extras:
            schemas[name].setdefault("properties", {})[k] = copy.deepcopy(P[k])
            mprops[k] = P[k]
            extended.setdefault(name, set()).add(k)
        d["container"][d["key"]] = {"$ref": REF + name}
        linked.append({"operation": d["operation"], "status": d["status"], "model": name,
                       "list": d["list"], "via": d["via"], "added_fields": extras})

    still_unused = sorted(set(schemas) - reachable_models(spec))
    report = {
        "linked": linked,
        "extended_models": {k: sorted(v) for k, v in sorted(extended.items())},
        "unlinked": unlinked,
        "models_still_unused": still_unused,
    }

    if verbose:
        by_model: dict[str, int] = {}
        for l in linked:
            by_model[l["model"]] = by_model.get(l["model"], 0) + 1
        print(f"linked {len(linked)} response schemas to {len(by_model)} models; "
              f"{len(unlinked)} left inline")
        for n, c in sorted(by_model.items(), key=lambda x: -x[1]):
            more = f"  (+{len(extended[n])} fields)" if n in extended else ""
            print(f"  {n:<28} {c:>3} response(s){more}")
        if still_unused:
            print(f"models still unreferenced: {', '.join(still_unused)}")
    return report


# --------------------------------------------------------------------------- #
def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawTextHelpFormatter)
    ap.add_argument("input")
    ap.add_argument("output")
    ap.add_argument("--strict", action="store_true",
                    help="only link when the response is fully contained in the model")
    ap.add_argument("--min-props", type=int, default=3)
    ap.add_argument("--min-coverage", type=float, default=0.6)
    ap.add_argument("--overrides", help="JSON file: {'<method> <path>': 'Model' | null}")
    ap.add_argument("--report", default="model_links.json", help="where to write the JSON report")
    args = ap.parse_args()

    with open(args.input, encoding="utf-8") as f:
        spec = json.load(f)
    overrides = None
    if args.overrides:
        with open(args.overrides, encoding="utf-8") as f:
            overrides = json.load(f)

    report = link_models(spec, strict=args.strict, min_props=args.min_props,
                         min_coverage=args.min_coverage, overrides=overrides)

    with open(args.output, "w", encoding="utf-8") as f:
        json.dump(spec, f, indent=2, ensure_ascii=False)
    with open(args.report, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2, ensure_ascii=False)
    print(f"wrote {args.output} and {args.report}")


if __name__ == "__main__":
    main()
