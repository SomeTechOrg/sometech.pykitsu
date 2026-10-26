"""Repair a Swagger-2/OpenAPI-3 hybrid spec so openapi-generator accepts it.

Usage:
    python fix_spec.py openapi.json openapi.fixed.json [--drop-twin-paths] [--validate]

Fixes applied:
  1. Parameters: Swagger 2 keys (type, format, default, ...) moved under `schema`;
     `collectionFormat` -> style/explode. Path parameters forced to required: true.
  2. `in: body` / `in: formData` parameters (also behind a $ref) converted to
     `requestBody`, using `consumes` for the media type.
  3. Responses: Swagger 2 `schema` / `examples` / `headers` converted to `content`;
     missing `description` added. `produces` / `consumes` removed.
  4. Operations without `responses` get a default 200.
  5. Status codes accidentally nested inside another response are hoisted.
  6. Path variables with no declared path parameter get one (type: string).
  7. Arrays without `items` get `items: {}`; boolean `required` inside schemas removed
     (but kept on parameters, headers and requestBody, where OAS3 needs it).
     `type: file` -> string/binary, string `discriminator` -> object, `x-nullable` -> nullable.
  8. Root `host` / `basePath` / `schemes` folded into `servers`; `swagger` key dropped.
  9. `definitions` / global `parameters` / `responses` moved under `components`
     and every `$ref` rewritten; `securityDefinitions` converted to `securitySchemes`.
 10. securitySchemes names normalised to ^[A-Za-z0-9._-]+$ (references updated).
 11. Trailing-slash twin paths reported (or merged/dropped with --drop-twin-paths).
 12. operationIds generated when missing, then made unique across the whole spec.

--validate runs openapi-spec-validator on the result (pip install openapi-spec-validator)
and lists whatever is still wrong, so you can iterate on the real Kitsu spec.
"""
from __future__ import annotations

import argparse
import copy
import json
import re
import sys
from collections import defaultdict
from typing import Any

HTTP = {"get", "put", "post", "delete", "patch", "options", "head", "trace"}
SCHEMA_KEYS = {
    "type", "format", "default", "enum", "items", "minimum", "maximum",
    "exclusiveMinimum", "exclusiveMaximum", "multipleOf", "uniqueItems",
    "minLength", "maxLength", "pattern", "minItems", "maxItems",
}
STATUS_RE = re.compile(r"[1-5]\d\d")
REF_PREFIXES = (
    ("#/definitions/", "#/components/schemas/"),
    ("#/parameters/", "#/components/parameters/"),
    ("#/responses/", "#/components/responses/"),
)


def snake(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "_", text.lower()).strip("_")


def deref(spec: dict[str, Any], node: Any) -> Any:
    """Follow local $ref chains (needed to classify parameters given as $ref)."""
    for _ in range(10):
        if not (isinstance(node, dict) and isinstance(node.get("$ref"), str)):
            break
        ref = node["$ref"]
        if not ref.startswith("#/"):
            break
        cur: Any = spec
        for part in ref[2:].split("/"):
            part = part.replace("~1", "/").replace("~0", "~")
            if not isinstance(cur, dict) or part not in cur:
                return node
            cur = cur[part]
        node = cur
    return node


# --------------------------------------------------------------------------- #
# Parameters, bodies, responses
# --------------------------------------------------------------------------- #
def move_schema_keys(node: dict[str, Any]) -> None:
    """Swagger 2 inline type keys -> `schema` (parameters and headers)."""
    leftovers = {k: node.pop(k) for k in list(node) if k in SCHEMA_KEYS}
    schema = node.setdefault("schema", {})
    if "$ref" not in schema:
        for k, v in leftovers.items():
            schema.setdefault(k, v)
        schema.setdefault("type", "string")


def apply_collection_format(p: dict[str, Any], cf: str) -> None:
    if p.get("in") == "query":
        table = {"csv": ("form", False), "multi": ("form", True),
                 "ssv": ("spaceDelimited", False), "pipes": ("pipeDelimited", False)}
    elif p.get("in") in ("path", "header"):
        table = {"csv": ("simple", False)}
    else:
        table = {}
    if cf in table and "style" not in p:
        p["style"], p["explode"] = table[cf]


def fix_param(p: dict[str, Any]) -> None:
    if "$ref" in p:
        return
    if p.get("in") == "path":
        p["required"] = True
    if "content" in p:
        return
    cf = p.pop("collectionFormat", None)
    move_schema_keys(p)
    if cf:
        apply_collection_format(p, cf)


def convert_body_params(spec: dict[str, Any], op: dict[str, Any], root_consumes: list[str]) -> None:
    """Swagger 2 'in: body' / 'in: formData' parameters -> OAS3 requestBody."""
    resolved = [(p, deref(spec, p)) for p in op.get("parameters", [])]
    form = [rp for _, rp in resolved if rp.get("in") == "formData"]
    body = [rp for _, rp in resolved if rp.get("in") == "body"]
    if not form and not body:
        return

    remaining = [p for p, rp in resolved if rp.get("in") not in ("formData", "body")]
    if remaining:
        op["parameters"] = remaining
    else:
        op.pop("parameters", None)

    consumes = op.get("consumes") or root_consumes or ["application/json"]

    if body and "requestBody" not in op:
        b = body[0]
        media = [mt for mt in consumes if "form" not in mt] or ["application/json"]
        op["requestBody"] = {
            "required": b.get("required", False),
            "content": {mt: {"schema": copy.deepcopy(b.get("schema", {}))} for mt in media},
        }
    if form and "requestBody" not in op:
        props: dict[str, Any] = {}
        required: list[str] = []
        has_file = False
        for p in form:
            if p.get("type") == "file":
                has_file = True
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
        urlenc = "application/x-www-form-urlencoded"
        mt = urlenc if (urlenc in consumes and not has_file) else "multipart/form-data"
        op["requestBody"] = {"content": {mt: {"schema": schema}}}


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


def fix_response(r: dict[str, Any], produces: list[str]) -> None:
    """Swagger 2 response (schema/examples/headers) -> OAS3 response."""
    if "$ref" in r:
        return
    r.setdefault("description", "Response")
    for h in (r.get("headers") or {}).values():
        if isinstance(h, dict) and "$ref" not in h and "schema" not in h and "content" not in h:
            move_schema_keys(h)
    schema = r.pop("schema", None)
    examples = r.pop("examples", None)
    if schema is not None and "content" not in r:
        r["content"] = {mt: {"schema": copy.deepcopy(schema)} for mt in produces}
    if isinstance(examples, dict):
        for mt, ex in examples.items():
            r.setdefault("content", {}).setdefault(mt, {})["example"] = ex


def fix_responses(op: dict[str, Any], root_produces: list[str]) -> None:
    explicit = op.pop("produces", None)
    op.pop("consumes", None)
    if isinstance(explicit, str):
        explicit = [explicit]
    produces = explicit or root_produces or ["application/json"]

    if not op.get("responses"):
        op["responses"] = {"200": {"description": "Successful response"}}
    for code, r in op["responses"].items():
        if not isinstance(r, dict):
            continue
        fix_response(r, produces)
        # `produces` declared but no schema: still advertise the media type.
        if explicit and code in ("200", "201") and "content" not in r and "$ref" not in r:
            r["content"] = {
                mt: {"schema": {} if "json" in mt else {"type": "string"}} for mt in explicit
            }


def add_missing_path_params(spec: dict[str, Any], path: str, item: dict[str, Any], op: dict[str, Any]) -> None:
    declared: set[Any] = set()
    for p in list(item.get("parameters", [])) + list(op.get("parameters", [])):
        rp = deref(spec, p)  # a $ref'd parameter has no `in` / `name` until resolved
        if rp.get("in") == "path":
            declared.add(rp.get("name"))
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


VALID_TYPES = {"string", "number", "integer", "boolean", "array", "object"}
# Non-standard `type` values seen in hand-written specs -> (type, format)
TYPE_ALIASES: dict[str, tuple[str | None, str | None]] = {
    "float": ("number", "float"), "double": ("number", "double"),
    "decimal": ("number", None), "number": ("number", None),
    "int": ("integer", "int32"), "int32": ("integer", "int32"),
    "int64": ("integer", "int64"), "long": ("integer", "int64"),
    "str": ("string", None), "text": ("string", None),
    "bool": ("boolean", None),
    "date": ("string", "date"), "datetime": ("string", "date-time"),
    "date-time": ("string", "date-time"), "uuid": ("string", "uuid"),
    "dict": ("object", None), "map": ("object", None), "list": ("array", None),
    "any": (None, None), "null": (None, None),
}
VALUE_KEYS = {"example", "examples", "default", "enum", "const"}  # data, not schemas


def fix_type(node: dict[str, Any]) -> None:
    t = node.get("type")
    if isinstance(t, list):  # OAS 3.1 style ["string", "null"]
        non_null = [x for x in t if x != "null"]
        if "null" in t:
            node["nullable"] = True
        if len(non_null) == 1:
            node["type"] = t = non_null[0]
        else:
            del node["type"]
            return
    if not isinstance(t, str) or t in VALID_TYPES or t == "file":
        return
    new_type, new_format = TYPE_ALIASES.get(t.lower(), (None, None))
    if t.lower() == "null":
        node["nullable"] = True
    if new_type is None:
        del node["type"]  # unknown -> any
        return
    node["type"] = new_type
    if new_format and "format" not in node:
        node["format"] = new_format


def walk(node: Any, names: bool = False) -> None:
    """`names=True` means `node` is a `properties` map: its keys are property
    names, not schema keywords, so no keyword fixes apply to it."""
    if isinstance(node, dict):
        if names:
            for v in node.values():
                walk(v)
            return
        fix_type(node)
        if node.get("type") == "array" and "items" not in node:
            node["items"] = {}  # untyped items -> Any
        if node.get("type") == "file":
            node["type"], node["format"] = "string", "binary"
        if isinstance(node.get("discriminator"), str):
            node["discriminator"] = {"propertyName": node["discriminator"]}
        xn = node.get("x-nullable")
        if isinstance(xn, bool):
            del node["x-nullable"]
            if xn:
                node["nullable"] = True
        # `required: true` is Swagger 2 style inside schemas, but legitimate on
        # parameters, headers (have `schema`) and requestBody (has `content`).
        if (isinstance(node.get("required"), bool) and not is_param(node)
                and "content" not in node and "schema" not in node):
            del node["required"]
        for k, v in node.items():
            if k in VALUE_KEYS or k == "securitySchemes":
                continue  # data / non-schema sections: `type: apiKey` is legal there
            walk(v, names=(k == "properties" and isinstance(v, dict)))
    elif isinstance(node, list):
        for v in node:
            walk(v)


def rewrite_refs(node: Any) -> None:
    if isinstance(node, dict):
        ref = node.get("$ref")
        if isinstance(ref, str):
            for old, new in REF_PREFIXES:
                if ref.startswith(old):
                    node["$ref"] = new + ref[len(old):]
                    break
        for v in node.values():
            rewrite_refs(v)
    elif isinstance(node, list):
        for v in node:
            rewrite_refs(v)


# --------------------------------------------------------------------------- #
# Root-level fixes
# --------------------------------------------------------------------------- #
def fix_root(spec: dict[str, Any]) -> tuple[list[str], list[str]]:
    produces = spec.pop("produces", None) or ["application/json"]
    consumes = spec.pop("consumes", None) or ["application/json"]
    spec.pop("swagger", None)
    spec.setdefault("openapi", "3.0.2")

    host = spec.pop("host", None)
    base_path = spec.pop("basePath", "")
    schemes = spec.pop("schemes", None) or ["https"]
    if "servers" not in spec:
        url = f"{schemes[0]}://{host}{base_path}" if host else (base_path or "/")
        spec["servers"] = [{"url": url}]

    components = spec.setdefault("components", {})
    for old, new in (("definitions", "schemas"), ("parameters", "parameters"), ("responses", "responses")):
        if old in spec:
            components.setdefault(new, {}).update(spec.pop(old))
    sec = spec.pop("securityDefinitions", None)
    if sec:
        components.setdefault("securitySchemes", {}).update(sec)
    rewrite_refs(spec)
    spec.setdefault("paths", {})
    return produces, consumes


def fix_components(spec: dict[str, Any], produces: list[str]) -> None:
    comps = spec.get("components", {})
    params = comps.get("parameters", {})
    for name in list(params):
        p = params[name]
        if p.get("in") in ("body", "formData"):
            del params[name]  # already inlined into each requestBody
        else:
            fix_param(p)
    for r in comps.get("responses", {}).values():
        if isinstance(r, dict):
            fix_response(r, produces)


def infer_security_type(s: dict[str, Any], name: str) -> str | None:
    """Guess the missing `type` of a security scheme from its other keys."""
    if "scheme" in s or "bearerFormat" in s:
        return "http"
    if "in" in s and "name" in s:
        return "apiKey"
    if "flows" in s or "flow" in s:
        return "oauth2"
    if "openIdConnectUrl" in s:
        return "openIdConnect"
    if re.search(r"jwt|bearer|token", name, re.I):
        return "http"  # completed to `scheme: bearer` below
    return None


def convert_security(s: dict[str, Any], name: str = "") -> dict[str, Any]:
    """Swagger 2 security definition -> OAS3 security scheme."""
    if "type" not in s:
        guessed = infer_security_type(s, name)
        if guessed:
            s = {"type": guessed, **s}
            if guessed == "http":
                s.setdefault("scheme", "bearer")
                if re.search(r"jwt", name, re.I):
                    s.setdefault("bearerFormat", "JWT")
            print(f"securityScheme {name!r} had no type; assumed {guessed!r}")
    t = s.get("type")
    if t == "basic":
        out: dict[str, Any] = {"type": "http", "scheme": "basic"}
    elif t == "oauth2" and "flow" in s:
        flow_names = {"implicit": "implicit", "password": "password",
                      "application": "clientCredentials", "accessCode": "authorizationCode"}
        flow: dict[str, Any] = {"scopes": s.get("scopes", {})}
        for k in ("authorizationUrl", "tokenUrl"):
            if k in s:
                flow[k] = s[k]
        out = {"type": "oauth2", "flows": {flow_names.get(s["flow"], s["flow"]): flow}}
    else:
        return s
    if "description" in s:
        out["description"] = s["description"]
    return out


def fix_security_names(spec: dict[str, Any]) -> None:
    schemes = spec.get("components", {}).get("securitySchemes", {})
    for name in list(schemes):
        schemes[name] = convert_security(schemes[name], name)
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
    for path, m, op in all_ops:
        if "operationId" not in op:
            # clashes are resolved in step 2 (method + path suffix)
            op["operationId"] = snake(op.get("summary") or "") or snake(f"{m} {path}")

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
def validate(spec: dict[str, Any]) -> int:
    try:
        from openapi_spec_validator import OpenAPIV30SpecValidator
    except ImportError:
        print("pip install openapi-spec-validator to use --validate", file=sys.stderr)
        return 1
    errors = list(OpenAPIV30SpecValidator(spec).iter_errors())
    for e in errors[:50]:
        loc = "/".join(str(x) for x in getattr(e, "absolute_path", []))
        print(f"INVALID {loc}: {str(e.message)[:200]}")
    print(f"{len(errors)} validation error(s)")
    return 2 if errors else 0


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawTextHelpFormatter)
    ap.add_argument("input", nargs="?", default="openapi.json")
    ap.add_argument("output", nargs="?", default="openapi.fixed.json")
    ap.add_argument("--drop-twin-paths", action="store_true",
                    help="merge and drop '/x/' when '/x' also exists (default: only report)")
    ap.add_argument("--validate", action="store_true",
                    help="validate the result with openapi-spec-validator")
    args = ap.parse_args()

    with open(args.input, encoding="utf-8") as f:
        spec = json.load(f)

    produces, consumes = fix_root(spec)

    for path, item in spec["paths"].items():
        if not isinstance(item, dict):
            continue
        for p in item.get("parameters", []):
            fix_param(p)
        for m, op in item.items():
            if m not in HTTP:
                continue
            convert_body_params(spec, op, consumes)
            for p in op.get("parameters", []):
                fix_param(p)
            hoist_nested_status_codes(op)
            fix_responses(op, produces)
            add_missing_path_params(spec, path, item, op)

    fix_components(spec, produces)
    walk(spec)
    fix_security_names(spec)
    handle_twin_paths(spec, drop=args.drop_twin_paths)
    fix_operation_ids(spec)

    with open(args.output, "w", encoding="utf-8") as f:
        json.dump(spec, f, indent=2, ensure_ascii=False)
    print(f"wrote {args.output}")

    if args.validate:
        sys.exit(validate(spec))


if __name__ == "__main__":
    main()
