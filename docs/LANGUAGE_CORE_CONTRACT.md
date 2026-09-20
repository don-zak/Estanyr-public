# Language Core Contract — ESTANYR v0.2

ESTANYR must not depend on a single model family, vendor, checkpoint, or
inference engine.

The Language Core is the replaceable generative component that consumes text
and/or genome-conditioned context and produces model outputs. The Cognitive
Genome remains a distinct capability layer.

## Architectural role

```text
User / Task
    |
    v
ESTANYR Runtime
    |
    +--> Cognitive Genome
    |
    +--> Conditioning / Context Composition
    |
    v
Language Core
    |
    v
Generated Output
```

The Language Core may be a compact transformer, a small language model, or a
research baseline. A particular model family is an implementation choice, not
part of ESTANYR's public identity.

## Public requirements

A conforming Language Core profile MUST declare:

- a stable core identifier;
- model class;
- parameter-scale band;
- context-window capability;
- tokenizer identity or tokenizer-family label;
- supported numerical precision modes;
- whether the core is instruction-tuned or base/pretrained;
- whether genome conditioning is supported by the integration;
- the public license family or an explicit undisclosed marker.

## Interchangeability

The public contract is designed so that multiple candidate cores can be tested
under the same benchmark protocol.

At minimum, ESTANYR research SHOULD be able to compare:

```text
Core A + no genome
Core A + genome

Core B + no genome
Core B + genome
```

A claimed genome gain is stronger when it reproduces across more than one
independent Language Core family.

## Non-goals

This contract does not expose:

- private adapter weights;
- private genome encoders;
- private training recipes;
- unpublished model modifications;
- proprietary inference kernels;
- private benchmark datasets.

## Independence rule

ESTANYR should remain usable even if a specific external model family becomes
unavailable.

The public architecture therefore treats model choice as replaceable and the
Cognitive Genome as a separate, testable source of capability.
