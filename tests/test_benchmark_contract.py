from __future__ import annotations

import json
from pathlib import Path

import jsonschema

ROOT = Path(__file__).resolve().parents[1]


def load_json(relative: str):
    return json.loads((ROOT / relative).read_text(encoding="utf-8"))


def test_public_benchmark_example_validates():
    schema = load_json("schemas/benchmark_run.schema.json")
    example = load_json("examples/synthetic_benchmark_run.json")
    jsonschema.Draft202012Validator(schema).validate(example)


def test_genome_track_can_carry_public_evidence_level():
    schema = load_json("schemas/benchmark_run.schema.json")
    example = load_json("examples/synthetic_benchmark_run.json")
    example["evidence_level"] = "E3"
    jsonschema.Draft202012Validator(schema).validate(example)


def test_benchmark_rejects_unknown_track():
    schema = load_json("schemas/benchmark_run.schema.json")
    example = load_json("examples/synthetic_benchmark_run.json")
    example["track"] = "private-experimental-mode"

    errors = list(jsonschema.Draft202012Validator(schema).iter_errors(example))
    assert errors
