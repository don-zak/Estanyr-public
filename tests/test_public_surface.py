from __future__ import annotations

import json
from pathlib import Path

import jsonschema
from referencing import Registry, Resource

ROOT = Path(__file__).resolve().parents[1]


def load_json(relative: str):
    return json.loads(
        (ROOT / relative).read_text(encoding="utf-8")
    )


def public_registry() -> Registry:
    evidence = load_json(
        "schemas/evidence_level.schema.json"
    )

    registry = Registry().with_resource(
        "https://cgt.example/spec/evidence_level.schema.json",
        Resource.from_contents(evidence),
    )

    return registry


def test_json_files_parse():
    for path in ROOT.rglob("*.json"):
        json.loads(
            path.read_text(encoding="utf-8")
        )


def test_synthetic_example_validates_against_public_schema():
    schema = load_json(
        "schemas/genome_state.schema.json"
    )
    example = load_json(
        "examples/synthetic_genome_state.json"
    )

    validator = jsonschema.Draft202012Validator(
        schema,
        registry=public_registry(),
    )

    validator.validate(example)


def test_manifest_schema_accepts_public_shape():
    schema = load_json(
        "schemas/genome_manifest.schema.json"
    )

    sample = {
        "genome_id": "synthetic-demo",
        "schema_version": "0.1",
        "engine_version": "public-contract",
        "state_id": "a" * 64,
        "parent_state_id": None,
        "evidence_level": "E0",
        "created_at": "2026-09-19T20:00:00Z",
        "source_hashes": [],
        "crypto_profile": "PUBLIC-EXAMPLE",
        "signature_b64": None,
    }

    validator = jsonschema.Draft202012Validator(
        schema,
        registry=public_registry(),
    )

    validator.validate(sample)


def test_no_known_private_paths_or_backup_artifacts():
    forbidden_fragments = (
        ".integration-backup",
        ".security-qualification-backup",
        ".final-hardening-backup",
        ".metadata-backup",
        "cgt-private-local",
        "private experimental results",
    )

    for path in ROOT.rglob("*"):
        if not path.is_file():
            continue

        relative = str(
            path.relative_to(ROOT)
        ).lower()

        assert ".backup" not in relative
        assert "private-local" not in relative

        if path.suffix.lower() == ".json":
            text = path.read_text(
                encoding="utf-8"
            ).lower()

            for fragment in forbidden_fragments[:5]:
                assert fragment.lower() not in text


def test_required_public_documents_exist():
    required = (
        "README.md",
        "SECURITY_BOUNDARY.md",
        "docs/ARCHITECTURE.md",
        "docs/EVIDENCE_LEVELS.md",
        "docs/PUBLICATION_POLICY.md",
        "docs/VERSIONING.md",
        "schemas/evidence_level.schema.json",
        "schemas/genome_state.schema.json",
        "schemas/genome_manifest.schema.json",
    )

    for relative in required:
        assert (ROOT / relative).is_file()
