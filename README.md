# CGT Public Surface

This repository is the public specification and interoperability surface for CGT.

It is intentionally separate from the private implementation repository and
must never be treated as a mirror, fork, history rewrite, or implementation
export of the private CGT runtime.

## Public scope

This repository may contain:

- stable public interfaces;
- non-sensitive schemas;
- public scientific terminology;
- synthetic examples;
- interoperability contracts;
- selected abstract architecture documentation;
- publication and versioning policy.

## Explicitly out of scope

This repository must not contain:

- private CGT algorithms;
- reconstruction-capable proprietary implementation details;
- unpublished qualification logic;
- exact private experiment definitions;
- private experimental results;
- frozen sensitive target sets;
- private model weights;
- credentials or secrets;
- cryptographic private keys;
- production data.

## Evidence rule

CGT uses the public rule:

> No capability may claim a maturity above its evidence level.

The public evidence ladder is documented in `docs/EVIDENCE_LEVELS.md`.

## Repository role

The public repository is a specification surface. It does not imply that the
private runtime implementation is open source.

No software license is selected by this qualification bundle. A license decision
must be made explicitly before public release.
