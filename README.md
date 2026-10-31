# OPENAST: Open Agent Sight Trust

**Signed visual claims bound to an exact agent action.**

An agent may decode a legitimate display or receive a controller contact report
and still lack permission for the action it proposes. OPENAST preserves
that distinction using explicitly scoped observations and separate customer
permission, enforced outside any language model.

## Status

Experimental local Python implementation, with runnable demos, tests, reproducible
benchmarks and a research paper draft. Actual QR raster encoding/decoding is implemented. Camera/display hardware and deployed agents have not been evaluated.

A valid QR response does not prove the truth of the surrounding scene, display location, proximity or human consent.

## Run

Requires Python 3.11+. From a parent folder containing the three repositories:

```sh
python -m venv .venv
source .venv/bin/activate
python -m pip install -e open-modality-trust/core -e openast
python -m openast demo --output openast/output/demo
```

In a recursive umbrella checkout, use `core` and `modalities/openast` instead.
The shared `open-modality-trust-core` package must come from that checkout; no
PyPI publication is asserted. No API key, cloud account or hardware is required.
The demo creates a signed QR image and durable local receipt. Keys are ephemeral.

## How it works

1. A verifier stores a random challenge bound to the exact principal, action,
   resource, purpose and every argument.
2. A configured display signs a response containing the exact requested statement digest and challenge. The response travels through an actual QR image.
3. A separate owner signer grants permission for the exact action, audience and
   modality. The modality signature itself supplies no permission.
4. The gateway checks current permission, supported guarantees and explicit
   assumptions, then atomically consumes the challenge/grant and inserts a local
   ledger receipt in one SQLite transaction.

The receipt is the only implemented effect. A later HTTP call or physical actuator
is outside this atomicity claim. Evidence is signed, not encrypted; do not place
secrets in public markers or traces. Ordinary scene text and arbitrary tactile
reports remain untrusted.

## Validate and reproduce

```sh
python -m pip install pytest ruff opencv-python-headless
python -m pytest openast/tests
python openast/scripts/benchmark.py --trials 20
```

- [Architecture and protocol](docs/architecture.md)
- [Threat model and limits](docs/threat-model.md)
- [Integration example](examples/workflow.py)
- [Benchmark method and results](docs/benchmarks/README.md) and [measured environment](docs/benchmarks/environment.json)
- [Research positioning](docs/novelty.md)
- [Paper and reproduction](paper/README.md)

## Research contribution

This is a concrete research reference, not a claim that signatures, visual
authentication, contact patterns or transactional authorization are new.
The benchmarks compare an intentionally weak signature-only check with an equally
expressive sequential typed-policy control. No advantage over that stronger
control, formal proof, IFC implementation, LLM resistance, external interoperability
or physical deployment is claimed. Cross-modal composition and efficient evidence
acquisition remain questions for the broader OpenModalityTrust project.

Apache-2.0. Generated fixtures contain no people, customer records or recordings.
