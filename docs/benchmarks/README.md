# OPENAST local benchmark evidence

Generated from `local-2026-10-31.json`; synthetic channel trials, not deployment results.

Report SHA-256: `13cd10a9e9414098a77496eac57022bb3d4b549cbacdebf4c58e462e401bfd2a`.

## Reproduce

```sh
python openast/scripts/benchmark.py --trials 20
python openast/scripts/report.py
```

Install the local shared core and modality package first, plus pytest, matplotlib and (for OpenAST) opencv-python-headless.

New runs use fresh signing keys and random security challenges; image outcomes and timing may vary.
The signal scenario seeds are explicit. Code SHA-256s, environment versions, per-case outcomes and timings are in the JSON.

## Channel results

| Condition | Successes | 95% Wilson interval | Median / p95 processing (ms) |
|---|---:|---:|---:|
| clean | 20/20 | 0.839-1.000 | 1.421 / 1.687 |
| rotate-90 | 20/20 | 0.839-1.000 | 1.323 / 1.771 |
| perspective-8pct | 20/20 | 0.839-1.000 | 1.407 / 1.773 |
| blur-0.8px | 20/20 | 0.839-1.000 | 1.470 / 1.795 |
| blur-2.0px | 20/20 | 0.839-1.000 | 1.578 / 2.073 |
| contrast-0.35 | 20/20 | 0.839-1.000 | 1.300 / 2.325 |
| downsample-0.5 | 20/20 | 0.839-1.000 | 0.662 / 1.135 |
| jpeg-q35 | 20/20 | 0.839-1.000 | 1.339 / 1.473 |
| noise-sd25 | 20/20 | 0.839-1.000 | 1.440 / 1.931 |
| occlusion-8pct | 20/20 | 0.839-1.000 | 1.391 / 1.785 |
| neighboring-instruction | 20/20 | 0.839-1.000 | 1.563 / 1.894 |
| blur-4.0px | 0/20 | 0.000-0.161 | 0.802 / 1.294 |
| downsample-0.15 | 0/20 | 0.000-0.161 | 0.115 / 0.467 |
| occlusion-25pct | 20/20 | 0.839-1.000 | 1.500 / 1.779 |

Conditions are paired within each source-image/scenario trial. Wilson intervals are descriptive per-condition binomial intervals, not independent evidence across paired conditions or estimates of real-world security.

## Exact-action policy cases

600 observations (30 cases x 20 trials).

| Case | Gateway accepted | Signature-only accepted | Typed control accepted | New effects |
|---|---:|---:|---:|---:|
| valid | 20 | 20 | 20 | 20 |
| evidence-tamper | 0 | 0 | 0 | 0 |
| unconfigured-key | 0 | 0 | 0 | 0 |
| action-substitution | 0 | 20 | 0 | 0 |
| resource-substitution | 0 | 20 | 0 | 0 |
| principal-substitution | 0 | 20 | 0 | 0 |
| purpose-substitution | 0 | 20 | 0 | 0 |
| arguments-substitution | 0 | 20 | 0 | 0 |
| session-transplant | 0 | 20 | 0 | 0 |
| nonce-transplant | 0 | 20 | 0 | 0 |
| wrong-audience | 0 | 20 | 0 | 0 |
| expired-challenge | 0 | 20 | 0 | 0 |
| expired-grant | 0 | 20 | 0 | 0 |
| revoked-grant | 0 | 20 | 0 | 0 |
| revoked-before-registration | 0 | 20 | 0 | 0 |
| revoked-attester | 0 | 20 | 0 | 0 |
| revoked-delegator | 0 | 20 | 0 | 0 |
| unregistered-grant | 0 | 20 | 0 | 0 |
| wrong-grant-scope | 0 | 20 | 0 | 0 |
| wrong-grant-modality | 0 | 20 | 0 | 0 |
| wrong-attester-modality | 0 | 0 | 0 | 0 |
| consumed-replay | 0 | 20 | 0 | 0 |
| unknown-observation-profile | 0 | 20 | 0 | 0 |
| extra-observation-field | 0 | 20 | 0 | 0 |
| unaccepted-assumption | 0 | 20 | 0 | 0 |
| require-proximity | 0 | 20 | 0 | 0 |
| require-consent | 0 | 20 | 0 | 0 |
| fresh-relay-without-proximity-requirement | 20 | 20 | 20 | 20 |
| compromised-attester-without-sensor-truth-requirement | 20 | 20 | 20 | 20 |
| wrong-statement | 0 | 20 | 0 | 0 |

Unexpected outcomes: 0; unauthorized **new local receipts**: 0; disagreements with the typed control: 0.

Gate processing over mixed accepted/denied cases: median 0.232 ms, p95 1.227 ms. This is not an end-to-end physical-channel delay.

The signature-only baseline intentionally ignores action permission and freshness. Its failures are an ablation, not evidence against a fully scoped existing authorization system. The typed control has the same serial policy and shares crypto/adapter primitives; no security advantage over it is demonstrated.

The relay and compromised-attester cases forward valid structured bytes; they are **modeled limitations**, not measured physical attacks. They are accepted only when proximity/sensor truth is not required. Separate proximity/consent requirements are denied.

The policy attack cases enter after modality decoding; the channel and policy suites are separate. The end-to-end demos combine both paths.

## Concurrency

20 trials each of 8 simultaneous duplicate attempts and revocation serialized before commit. Each duplicate trial produces exactly one receipt; each prior-revocation trial produces zero. State is a local SQLite file, not a remote or physical actuator.

## Limits

Generated fixtures contain no human subjects or customer data. No camera/display hardware, force sensor, LLM, live relay, cloud integration, formal proof or independent security review was evaluated. Timings are one-host descriptive measurements; do not pool trial repetitions into a deployment security claim.
