from __future__ import annotations

import json
from pathlib import Path

import jsonschema

ROOT = Path(__file__).resolve().parents[1]


def load_json(relative: str):
    return json.loads((ROOT / relative).read_text(encoding="utf-8"))


def test_public_genome_conditioning_example_validates():
    schema = load_json("schemas/genome_conditioning.schema.json")
    example = load_json("examples/synthetic_genome_conditioning.json")
    jsonschema.Draft202012Validator(schema).validate(example)


def test_retrieval_only_cannot_claim_latent_state():
    schema = load_json("schemas/genome_conditioning.schema.json")
    example = load_json("examples/synthetic_genome_conditioning.json")
    example["mode"] = "retrieval-only"
    example["text_context_only"] = True
    example["latent_genome_state"] = True

    errors = list(jsonschema.Draft202012Validator(schema).iter_errors(example))
    assert errors


def test_cross_attention_requires_latent_state():
    schema = load_json("schemas/genome_conditioning.schema.json")
    example = load_json("examples/synthetic_genome_conditioning.json")
    example["mode"] = "cross-attention"
    example["text_context_only"] = False
    example["latent_genome_state"] = False

    errors = list(jsonschema.Draft202012Validator(schema).iter_errors(example))
    assert errors
