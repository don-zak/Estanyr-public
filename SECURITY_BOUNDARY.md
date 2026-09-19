# Public / Private Security Boundary

The public repository is a publication surface.

It must never become a mirror, fork, export, history rewrite, or implementation
copy of the private CGT repository.

Material may cross from PRIVATE to PUBLIC only after an explicit publication
review and sanitization step.

## Allowed

- public API and interoperability contracts;
- abstract architecture;
- non-sensitive schemas;
- synthetic examples;
- selected evidence terminology;
- public versioning information;
- documentation specifically approved for disclosure.

## Forbidden

- reconstruction-capable proprietary algorithms;
- private runtime implementation;
- exact private experiment definitions;
- unpublished qualification logic or results;
- private provenance artifacts;
- private datasets;
- model weights not explicitly approved for release;
- credentials, tokens, secrets, or cryptographic private keys;
- production configuration or customer data.

## Publication invariant

The permitted flow is:

```text
PRIVATE
→ publication review
→ sanitization
→ PUBLIC
```

There is no automatic synchronization from private to public.
