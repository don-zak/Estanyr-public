# Public Benchmark Contract — ESTANYR v0.2

This document defines the public comparison protocol for evaluating whether a
lightweight language model gains measurable capability from Cognitive Genome
conditioning.

It is intentionally implementation-neutral and does not expose private genome
construction, ranking, admission, training data, model weights, or internal
reasoning algorithms.

## Research objective

The benchmark asks:

> Can a lightweight base model achieve higher effective capability per unit of
> compute when conditioned by a qualified Cognitive Genome than when used alone
> or with ordinary retrieval?

## Required tracks

Each benchmark campaign SHOULD compare the same base model across three tracks:

```text
A. BASE
   Base language model only.

B. RETRIEVAL
   Same base model with ordinary retrieval augmentation.

C. GENOME
   Same base model with Cognitive Genome conditioning.
```

The model family, model checkpoint, decoding parameters, task set, hardware
class, and evaluation procedure SHOULD remain fixed across tracks except for the
conditioning mechanism under test.

## Core measurements

At minimum, a benchmark report SHOULD capture:

- task accuracy or task-specific quality score;
- factual consistency;
- relation discovery or relation-sensitive accuracy;
- contradiction handling;
- evidence calibration;
- cross-session consistency when the task supports it;
- transfer to held-out domains or topics when applicable;
- input tokens;
- output tokens;
- wall-clock latency;
- peak host memory;
- peak accelerator memory when applicable;
- model artifact size;
- declared parameter scale.

## Efficiency measurements

A benchmark MAY publish normalized indicators such as:

```text
quality / parameter
quality / peak-memory
quality / latency
quality / energy
quality / monetary-cost
```

No normalized score should be interpreted without the raw measurements from
which it was derived.

## Fairness constraints

A public comparison SHOULD satisfy all of the following:

1. Same frozen base model checkpoint across A/B/C.
2. Same task instances and scoring logic.
3. Same decoding settings unless the benchmark explicitly tests decoding.
4. Comparable external knowledge access.
5. No private answer-key leakage into retrieval or genome state.
6. Separate reporting of failed, timed-out, or invalid runs.
7. Repeated trials where stochastic decoding is used.

## Genome-specific disclosure

The public benchmark result may disclose:

- whether genome conditioning was enabled;
- public conditioning mode;
- public genome schema version;
- evidence level claimed for the tested capability.

It must not require disclosure of private construction algorithms, proprietary
relation operators, unpublished datasets, or private runtime internals.

## Evidence rule

A result does not raise the maturity of a capability by itself.

Promotion requires evidence consistent with the public evidence ladder and must
remain bounded by the rule:

```text
No capability may claim a maturity above its evidence level.
```

## Interpretation

ESTANYR's target is not to prove that a small model is universally superior to
a larger model.

The target is to establish whether structured cognitive state can substitute
for some model scale on defined tasks while preserving or improving efficiency.
