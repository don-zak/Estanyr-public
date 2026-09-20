# Genome Conditioning Contract — ESTANYR v0.2

This document defines the public conditioning modes by which a Language Core may
use a Cognitive Genome.

It specifies architectural classes only. It does not disclose private genome
construction, learned operators, adapter weights, ranking logic, or unpublished
qualification results.

## Purpose

ESTANYR is not defined as retrieval-augmented generation.

Ordinary retrieval is retained as a baseline. The research target is a stronger
coupling in which qualified genome state can influence language-model inference.

## Public conditioning modes

### 1. retrieval-only

The genome is treated only as a source from which text or records are retrieved.

```text
Genome -> retrieval -> text context -> Language Core
```

This mode is a baseline and does not, by itself, establish genome-conditioned
cognition.

### 2. structured-context

Selected genome state is serialized into an explicit structured context carrying
public concepts such as claims, relations, evidence level, contradiction state,
or provenance markers.

```text
Genome -> structured projection -> Language Core
```

This mode is stronger than ordinary retrieval but still operates through the
model's input context.

### 3. latent-adapter

Genome state is encoded into a learned latent representation consumed by a
separate adapter or projection path.

```text
Genome -> Genome Encoder -> latent state -> Adapter -> Language Core
```

This is a target research mode. The public contract does not disclose the
private encoder, adapter architecture, or learned parameters.

### 4. cross-attention

The Language Core attends to a genome-derived latent state through a dedicated
conditioning interface.

```text
Language Core <-> genome-derived latent state
```

This is a target research mode and requires direct empirical qualification.

### 5. decoder-guidance

Qualified genome state influences generation-time selection, validation, or
revision under a public policy contract.

```text
candidate generation
      |
      v
genome consistency / evidence guidance
      |
      v
accept, revise, or reject
```

This mode may be combined with another conditioning mode.

## Maturity rule

No conditioning mode is assumed to be superior by definition.

Each mode must be compared under the same public benchmark contract.

The public research ladder is therefore:

```text
retrieval-only
    -> structured-context
    -> latent-adapter
    -> cross-attention
    -> decoder-guidance combinations
```

This ordering is a research progression, not a performance ranking.

## Required declarations

A public conditioning profile MUST declare:

- contract version;
- primary conditioning mode;
- whether conditioning is trainable;
- whether the genome enters only through text context;
- whether latent genome state is used;
- whether generation-time guidance is enabled;
- the public genome schema version;
- the claimed evidence level.

## Boundary

The following remain private unless explicitly published later:

- genome encoder implementation;
- private relation operators;
- adapter weights;
- private training objectives;
- private ranking or admission logic;
- proprietary datasets;
- unpublished benchmark results.

## Success criterion

A genome conditioning mode is valuable only when it improves a defined
capability-efficiency tradeoff relative to both:

```text
same Language Core alone
same Language Core + ordinary retrieval
```

under controlled evaluation.
