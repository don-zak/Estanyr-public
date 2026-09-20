from __future__ import annotations

import json
from pathlib import Path

import jsonschema

ROOT = Path(__file__).resolve().parents[1]


def load_json(relative: str):
    return json.loads((ROOT / relative).read_text(encoding="utf-8"))


def test_public_model_profile_example_validates():
    schema = load_json("schemas/model_profile.schema.json")
    example = load_json("examples/synthetic_model_profile.json")
    jsonschema.Draft202012Validator(schema).validate(example)


def test_model_profile_rejects_unknown_fields():
    schema = load_json("schemas/model_profile.schema.json")
    example = load_json("examples/synthetic_model_profile.json")
    example["private_runtime_algorithm"] = "must-not-be-public"

    validator = jsonschema.Draft202012Validator(schema)
    errors = list(validator.iter_errors(example))
    assert errors
