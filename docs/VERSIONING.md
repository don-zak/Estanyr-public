# Public Surface Versioning

The public specification has its own version lifecycle and does not have to
match the private runtime commit-for-commit.

## Compatibility

Public schema changes should follow these rules:

- additive optional fields may be introduced in a minor public revision;
- removing or renaming public fields requires a breaking-version change;
- evidence-level names must not be silently redefined;
- private implementation changes do not require a public version change unless
  they alter a published contract.

## Current qualification

This package establishes the initial public qualification baseline:

```text
public-surface: v0.1
```

This is separate from the private CGT Genome Core runtime version.
