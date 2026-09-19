# Publication Policy

## Purpose

This repository exists to publish explicitly approved CGT specifications,
schemas, terminology, examples, and selected architecture material without
exposing the private implementation.

## Publication process

Every candidate publication must pass these stages:

```text
PRIVATE SOURCE
→ identify publication candidate
→ remove private implementation detail
→ remove secrets / credentials / private data
→ remove unpublished experiment detail
→ verify public schema and terminology
→ public-surface tests
→ human publication approval
→ PUBLIC COMMIT
```

## Prohibited publication methods

Do not:

- copy the private repository wholesale;
- preserve private Git history in the public repository;
- use subtree/filter-history tools to derive the public repository from private;
- automate private-to-public mirroring;
- publish private tests or qualification fixtures by default;
- publish files merely because they contain no obvious secret.

## Review questions

Before publication, confirm:

1. Is the material necessary for a public contract, explanation, example, or
   interoperability purpose?
2. Can it reconstruct or materially reveal a private algorithm?
3. Does it expose exact private experiments, target sets, datasets, or results?
4. Does it include secrets, key identifiers, credentials, customer data, or
   production configuration?
5. Has the material been rewritten as a public artifact rather than copied as
   an internal implementation artifact?

If any answer is uncertain, keep the material private.
