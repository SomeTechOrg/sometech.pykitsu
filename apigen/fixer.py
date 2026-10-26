import json
import re
from collections import defaultdict

HTTP = {"get", "put", "post", "delete", "patch", "options", "head", "trace"}
SCHEMA_KEYS = {"type", "format", "default", "enum", "items", "minimum", "maximum",
               "minLength", "maxLength", "pattern", "minItems", "maxItems"}


def snake(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "_", text.lower()).strip("_")


def fix_param(p: dict) -> None:
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


def convert_body_params(op: dict) -> None:
    """Swagger 2 'in: body' / 'in: formData' parameters -> OAS3 requestBody."""
    params = op.get("parameters", [])
    form = [p for p in params if p.get("in") == "formData"]
    body = [p for p in params if p.get("in") == "body"]
    if not form and not body:
        return
    op["parameters"] = [p for p in params if p.get("in") not in ("formData", "body")]
    if not op["parameters"]:
        del op["parameters"]
    if body and "requestBody" not in op:
        b = body[0]
        op["requestBody"] = {
            "required": b.get("required", False),
            "content": {"application/json": {"schema": b.get("schema", {})}},
        }
    if form and "requestBody" not in op:
        props, required = {}, []
        for p in form:
            if p.get("type") == "file":
                s = {"type": "string", "format": "binary"}
            else:
                s = {k: p[k] for k in SCHEMA_KEYS if k in p}
                s.setdefault("type", "string")
            if "description" in p:
                s["description"] = p["description"]
            props[p["name"]] = s
            if p.get("required"):
                required.append(p["name"])
        schema = {"type": "object", "properties": props}
        if required:
            schema["required"] = required
        op["requestBody"] = {"content": {"multipart/form-data": {"schema": schema}}}


def fix_responses(op: dict) -> None:
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


def add_missing_path_params(path: str, item: dict, op: dict) -> None:
    declared = {p.get("name") for p in item.get("parameters", []) if p.get("in") == "path"}
    declared |= {p.get("name") for p in op.get("parameters", []) if p.get("in") == "path"}
    for var in re.findall(r"\{([^}]+)\}", path):
        if var not in declared:
            op.setdefault("parameters", []).append({
                "in": "path", "name": var, "required": True,
                "schema": {"type": "string"},
            })


def is_param(node: dict) -> bool:
    return isinstance(node.get("in"), str) and "name" in node


def walk(node) -> None:
    if isinstance(node, dict):
        if node.get("type") == "array" and "items" not in node:
            node["items"] = {}
        if not is_param(node) and isinstance(node.get("required"), bool):
            del node["required"]
        for v in node.values():
            walk(v)
    elif isinstance(node, list):
        for v in node:
            walk(v)


with open("api.json") as f:
    spec = json.load(f)

for path, item in spec["paths"].items():
    for p in item.get("parameters", []):
        fix_param(p)
    for m, op in item.items():
        if m not in HTTP:
            continue
        convert_body_params(op)
        for p in op.get("parameters", []):
            fix_param(p)
        fix_responses(op)
        add_missing_path_params(path, item, op)

walk(spec)

ops = [(path, m, op) for path, item in spec["paths"].items()
       for m, op in item.items() if m in HTTP and "operationId" not in op]
groups = defaultdict(list)
for path, m, op in ops:
    groups[snake(op.get("summary") or f"{m} {path}")].append((path, m, op))
for base, members in groups.items():
    for path, m, op in members:
        op["operationId"] = base if len(members) == 1 else snake(f"{base} {m} {path}")

with open("api.fixed.json", "w") as f:
    json.dump(spec, f, indent=2)
