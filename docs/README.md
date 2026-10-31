# OPENAST documentation

OpenAST carries a signed statement through a QR image. The shared gateway
checks that statement, the exact request, and a separately signed owner grant.

| Goal | Read next |
|---|---|
| Understand the problem and run a demo | [Project README](../README.md) |
| Find implementation code | [Code map](code-map.md) |
| Install, change code, run checks | [Development guide](development.md) |
| Understand what a signature establishes | [Architecture](architecture.md), [threat model](threat-model.md) |
| Inspect measurements | [Recorded benchmarks](benchmarks/README.md), [environment](benchmarks/environment.json) |
| Assess prior work and research claims | [Novelty boundaries](novelty.md) |
| Read or rebuild the manuscript | [Paper guide](../paper/README.md) |
| Work as a coding agent | [Agent instructions](../AGENTS.md) |

## Read with these boundaries

The CLI demo and public fixtures are local and generated. Runtime behavior is
implemented in `src/`; numeric evidence comes from the raw report under
`docs/benchmarks/`. Research targets and stronger physical guarantees are described
as future work. A receipt is a local database record of an accepted request.

The shared core is maintained in the separate OpenModalityTrust repository.
OpenAVT's voice protocol remains independent of this local profile.
