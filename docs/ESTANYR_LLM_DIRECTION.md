# ESTANYR LLM Direction

ESTANYR is being developed as a lightweight, high-efficiency language model
system whose reasoning and answer generation can be conditioned by a qualified
Cognitive Genome.

This public document defines direction only. It does not disclose private
runtime algorithms, qualification logic, model weights, training data, or
reconstruction-capable implementation details.

## Product objective

The target is not merely an orchestration layer and not merely an external
memory service.

The target architecture is:

```text
Lightweight Base Model
        +
Cognitive Genome
        +
Genome-Aware Context / Retrieval
        +
Evidence-Calibrated Reasoning
        =
ESTANYR
```

The intended research question is whether a smaller model, when supported by a
qualified relational and evidential genome, can deliver higher effective
capability per unit of compute than the same model operating without that
genome.

## Public design principles

1. **Lightweight first** — model size is a constrained resource, not the primary
   source of capability.
2. **Genome-conditioned cognition** — the genome is intended to influence what
   knowledge is activated, related, trusted, retained, or challenged.
3. **Evidence-bounded claims** — no claimed capability may exceed its measured
   evidence level.
4. **Provider independence** — the public contract must not require one model
   vendor or one inference engine.
5. **Measurable efficiency** — quality gains must be assessed together with
   latency, memory use, model size, and compute cost.
6. **RAG is a baseline, not the definition** — ordinary retrieval-augmented
   generation remains a comparison point; ESTANYR's research objective is a
   stronger integration between model inference and qualified genome state.

## Required comparison track

Public evaluation should distinguish at least:

```text
A. Base LLM
B. Base LLM + ordinary retrieval
C. Base LLM + Cognitive Genome
```

The same base model and task set should be used wherever possible.

## Minimum public metrics

A future benchmark contract may expose measurements for:

- factual accuracy;
- relation discovery;
- contradiction handling;
- evidence calibration;
- cross-session consistency;
- transfer to unseen domains;
- latency;
- peak memory use;
- model artifact size;
- effective capability per unit of compute.

## Boundary

This document specifies the public research and product direction. Internal
genome construction, admission rules, learned relational operators, private
evaluation corpora, model weights, and unpublished qualification results remain
outside this repository.
