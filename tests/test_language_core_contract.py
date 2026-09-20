from __future__ import annotations

import json
from pathlib import Path

import jsonschema

ROOT = Path(__file__).resolve().parents[1]


def load_json(relative: str):
    return json.loads((ROOT / relative).read_text(encoding="utf-8"))


def test_public_language_core_example_validates():
    schema = load_json("schemas/language_core.schema.json")
    example = load_json("examples/synthetic_language_core.json")
    jsonschema.Draft202012Validator(schema).validate(example)


def test_language_core_requires_replaceable_identity():
    schema = load_json("schemas/language_core.schema.json")
    example = load_json("examples/synthetic_language_core.json")
    del example["core_id"]

    errors = list(jsonschema.Draft202012Validator(schema).iter_errors(example))
    assert errors


def test_language_core_rejects_unknown_precision():
    schema = load_json("schemas/language_core.schema.json")
    example = load_json("examples/synthetic_language_core.json")
    example["precision_modes"] = ["imaginary-precision"]

    errors = list(jsonschema.Draft202012Validator(schema).iter_errors(example))
    assert errors
