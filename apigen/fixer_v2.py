#!/usr/bin/env python3
"""Repair a Swagger-2/OpenAPI-3 hybrid spec so openapi-generator accepts it.

Usage:
    python fix_spec.py openapi.json openapi.fixed.json [--drop-twin-paths]

Fixes applied:
  1. Parameters: Swagger 2 keys (type, format, default, ...) moved under `schema`.
     Path parameters forced to required: true.
  2. `in: body` / `in: formData` parameters converted to `requestBody`.
  3. `produces` / `consumes` removed (turned into response content when useful).
  4. Operations without `responses` get a default 200.
  5. Status codes accidentally nested inside another response are hoisted.
  6. Path variables with no declared path parameter get one (type: string).
  7. Arrays without `items` get `items: {}`; boolean `required` inside schemas removed.
  8. Root `host` / `basePath` / `schemes` folded into `servers`.
  9. securitySchemes names normalised to ^[A-Za-z0-9._-]+$ (references updated).
 10. Trailing-slash twin paths reported (or merged/dropped with --drop-twin-paths).
 11. operationIds generated when missing, then made unique across the whole spec.
"""
from __future__ import annotations

import argparse
import json
import re
from collections import defaultdict
from typing import Any

HTTP = {"get", "put", "post", "delete", "patch", "options", "head", "trace"}
SCHEMA_KEYS = {
    "type", "format", "default", "enum", "items", "minimum", "maximum",
    "minLength", "maxLength", "pattern", "minItems", "maxItems",
}
STATUS_RE = re.compile(r"[1-5]\d\d")


def snake(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "_", text.lower()).strip("_")


# --------------------------------------------------------------------------- #
# Parameters, bodies, responses
# --------------------------------------------------------------------------- #
def fix_param(p: dict[str, Any]) -> None:
    if "$ref" in p:
        return
    if p.get("in") == "path":
        p["required"] = True
    if "content" in p:
        return
    leftovers = {k: p.pop(k) for k in list(p) if k in SCHEMA_KEYS}
    schema = p.setdefault("schema", {})
    if "$ref" not in schema:
        for k, v in leftovers.items():
            schema.setdefault(k, v)
        schema.setdefault("type", "string")


def convert_body_params(op: dict[str, Any]) -> None:
    """Swagger 2 'in: body' / 'in: formData' parameters -> OAS3 requestBody."""
    params = op.get("parameters", [])
    form = [p for p in params if p.get("in") == "formData"]
    body = [p for p in params if p.get("in") == "body"]
    if not form and not body:
        return

    remaining = [p for p in params if p.get("in") not in ("formData", "body")]
    if remaining:
        op["parameters"] = remaining
    else:
        op.pop("parameters", None)

    if body and "requestBody" not in op:
        b = body[0]
        op["requestBody"] = {
            "required": b.get("required", False),
            "content": {"application/json": {"schema": b.get("schema", {})}},
        }
    if form and "requestBody" not in op:
        props: dict[str, Any] = {}
        required: list[str] = []
        for p in form:
            if p.get("type") == "file":
                s: dict[str, Any] = {"type": "string", "format": "binary"}
            else:
                s = {k: p[k] for k in SCHEMA_KEYS if k in p}
                s.setdefault("type", "string")
            if "description" in p:
                s["description"] = p["description"]
            props[p["name"]] = s
            if p.get("required"):
                required.append(p["name"])
        schema: dict[str, Any] = {"type": "object", "properties": props}
        if required:
            schema["required"] = required
        op["requestBody"] = {"content": {"multipart/form-data": {"schema": schema}}}


def hoist_nested_status_codes(op: dict[str, Any]) -> None:
    """e.g. responses.201.400 -> responses.400"""
    responses = op.get("responses")
    if not isinstance(responses, dict):
        return
    for r in list(responses.values()):
        if isinstance(r, dict):
            for k in list(r):
                if STATUS_RE.fullmatch(k):
                    responses.setdefault(k, r.pop(k))


def fix_responses(op: dict[str, Any]) -> None:
    produces = op.pop("produces", None)
    op.pop("consumes", None)
    if not op.get("responses"):
        op["responses"] = {"200": {"description": "Successful response"}}
    if produces:
        if isinstance(produces, str):
            produces = [produces]
        for code in ("200", "201"):
            r = op["responses"].get(code)
            if isinstance(r, dict) and "content" not in r:
                r["content"] = {mt: {"schema": {"type": "string"}} for mt in produces}


def add_missing_path_params(path: str, item: dict[str, Any], op: dict[str, Any]) -> None:
    declared = {p.get("name") for p in item.get("parameters", []) if p.get("in") == "path"}
    declared |= {p.get("name") for p in op.get("parameters", []) if p.get("in") == "path"}
    for var in re.findall(r"\{([^}]+)\}", path):
        if var not in declared:
            op.setdefault("parameters", []).append(
                {"in": "path", "name": var, "required": True, "schema": {"type": "string"}}
            )


# --------------------------------------------------------------------------- #
# Schema walk
# --------------------------------------------------------------------------- #
def is_param(node: dict[str, Any]) -> bool:
    return isinstance(node.get("in"), str) and "name" in node


def walk(node: Any) -> None:
    if isinstance(node, dict):
        if node.get("type") == "array" and "items" not in node:
            node["items"] = {}  # untyped items -> Any
        if not is_param(node) and isinstance(node.get("required"), bool):
            del node["required"]  # Swagger 2 style, invalid inside schemas
        for v in node.values():
            walk(v)
    elif isinstance(node, list):
        for v in node:
            walk(v)


# --------------------------------------------------------------------------- #
# Root-level fixes
# --------------------------------------------------------------------------- #
def fix_root(spec: dict[str, Any]) -> None:
    host = spec.pop("host", None)
    base_path = spec.pop("basePath", "")
    schemes = spec.pop("schemes", None) or ["https"]
    if "servers" not in spec:
        url = f"{schemes[0]}://{host}{base_path}" if host else (base_path or "/")
        spec["servers"] = [{"url": url}]


def fix_security_names(spec: dict[str, Any]) -> None:
    schemes = spec.get("components", {}).get("securitySchemes", {})
    renames: dict[str, str] = {}
    for name in list(schemes):
        clean = re.sub(r"[^A-Za-z0-9._-]+", "", name)
        if clean != name:
            schemes[clean] = schemes.pop(name)
            renames[name] = clean
    if not renames:
        return

    def rename(requirements: Any) -> None:
        for req in requirements or []:
            for old, new in renames.items():
                if old in req:
                    req[new] = req.pop(old)

    rename(spec.get("security"))
    for item in spec["paths"].values():
        for m, op in item.items():
            if m in HTTP:
                rename(op.get("security"))


def handle_twin_paths(spec: dict[str, Any], drop: bool) -> None:
    """Paths that differ only by a trailing slash ('/x' and '/x/')."""
    paths = spec["paths"]
    for p in list(paths):
        if p.endswith("/") and p != "/" and p.rstrip("/") in paths:
            keep = p.rstrip("/")
            if not drop:
                print(f"twin path: {p!r} and {keep!r}")
                continue
            for method, op in paths[p].items():
                if method in HTTP and method not in paths[keep]:
                    paths[keep][method] = op  # merge ops the kept path lacks
            del paths[p]
            print(f"dropped twin path {p!r} (kept {keep!r})")


# --------------------------------------------------------------------------- #
# operationIds
# --------------------------------------------------------------------------- #
def fix_operation_ids(spec: dict[str, Any]) -> None:
    all_ops = [
        (path, m, op)
        for path, item in spec["paths"].items()
        for m, op in item.items()
        if m in HTTP
    ]

    # 1. generate missing ids from summaries
    missing: dict[str, list] = defaultdict(list)
    for path, m, op in all_ops:
        if "operationId" not in op:
            missing[snake(op.get("summary") or f"{m} {path}")].append((path, m, op))
    for base, members in missing.items():
        for path, m, op in members:
            op["operationId"] = base if len(members) == 1 else snake(f"{base} {m} {path}")

    # 2. make every id unique
    by_id: dict[str, list] = defaultdict(list)
    for path, m, op in all_ops:
        by_id[op["operationId"]].append((path, m, op))

    used = {oid for oid, members in by_id.items() if len(members) == 1}
    for oid, members in by_id.items():
        if len(members) == 1:
            continue
        for path, m, op in members:
            slug = snake(f"{oid} {m} {path}")
            candidate, n = slug, 2
            while candidate in used:
                candidate = f"{slug}_{n}"
                n += 1
            used.add(candidate)
            op["operationId"] = candidate


# --------------------------------------------------------------------------- #
def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawTextHelpFormatter)
    ap.add_argument("input", nargs="?", default="openapi.json")
    ap.add_argument("output", nargs="?", default="openapi.fixed.json")
    ap.add_argument("--drop-twin-paths", action="store_true",
                    help="merge and drop '/x/' when '/x' also exists (default: only report)")
    args = ap.parse_args()

    with open(args.input, encoding="utf-8") as f:
        spec = json.load(f)

    fix_root(spec)

    for path, item in spec["paths"].items():
        for p in item.get("parameters", []):
            fix_param(p)
        for m, op in item.items():
            if m not in HTTP:
                continue
            convert_body_params(op)
            for p in op.get("parameters", []):
                fix_param(p)
            hoist_nested_status_codes(op)
            fix_responses(op)
            add_missing_path_params(path, item, op)

    walk(spec)
    fix_security_names(spec)
    handle_twin_paths(spec, drop=args.drop_twin_paths)
    fix_operation_ids(spec)

    with open(args.output, "w", encoding="utf-8") as f:
        json.dump(spec, f, indent=2, ensure_ascii=False)
    print(f"wrote {args.output}")


if __name__ == "__main__":
    main()
