# Cognitive Genome — Public Architecture

The public conceptual genome is:

```text
G = (I, C, R, M, T, H, E, F)
```

Where:

- `I` = Identity
- `C` = Context
- `R` = Residual relational state
- `M` = Multiscale relational structure
- `T` = Transformations
- `H` = History
- `E` = Evidence
- `F` = Fate / admissible next-state constraints

This is a conceptual public contract, not a disclosure of private runtime
algorithms or internal implementation.

## Evidence constraint

The public architecture follows the rule:

```text
No capability may claim a maturity above its evidence level.
```

## Separation from implementation

The private runtime may use additional internal representations, controls,
qualification logic, storage details, or algorithms that are deliberately not
part of this public specification.
