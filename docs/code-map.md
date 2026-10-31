# OPENAST code and artifact map

| File | Responsibility | Useful verification |
|---|---|---|
| [protocol.py](../src/openast/protocol.py) | `respond` signs a challenge-bound resource/statement digest; `appraise` checks the exact requested statement | `tests/test_visual.py`; shared core tests |
| [visual.py](../src/openast/visual.py) | `encode` creates QR pixels; `decode` bounds image/decompression inputs and rejects ambiguous decoded markers | `tests/test_visual.py` |
| [cli.py](../src/openast/cli.py) | Local demo orchestration and public-evidence decoding | `make demo` |
| [workflow.py](../examples/workflow.py) | Small SDK example using separate display and owner keys | Run `python examples/workflow.py` |
| [public fixture](../examples/fixtures/README.md) | A signed synthetic QR example with its public key | `tests/test_visual_fixture.py` |
| [benchmark.py](../scripts/benchmark.py) | Generated-image transformations, policy cases and concurrency schedules | `make benchmark` |
| [verify_evidence.py](../scripts/verify_evidence.py) | Checks recorded arithmetic and measured source hashes | `make verify-evidence` |
| [report.py](../scripts/report.py) | Generates benchmark prose, LaTeX measurements and plots from recorded JSON | Publication workflow below |

## Shared enforcement

The separately installed `modality_trust` package owns immutable actions,
per-modality issuer trust, owner grants, revocation/replay state and transactional
local receipts. The implementation lives in the umbrella's
`core/src/modality_trust/`; its main behavior tests are `core/tests/test_core.py`.
An adapter change does not automatically update the shared core or other adapters.

## Editable sources and generated evidence

- Edit `src/`, `tests/`, human guides and Makefiles for implementation/navigation work.
- `examples/fixtures/` contains public synthetic inputs; its exporter writes fresh
  random keys/signatures, so do not regenerate it for unrelated documentation edits.
- `docs/benchmarks/local-2026-10-31.json` is a recorded measurement snapshot.
- `docs/benchmarks/README.md`, `paper/artifacts/measurements.tex` and channel plots
  are generated from that snapshot by `scripts/report.py`.
- `paper/sections/` and `paper/references.bib` are editable manuscript sources.
- Compiled PDFs and `paper/artifacts/build-verification.json` identify the reviewed
  build. Rebuilding a PDF alone does not refresh its review/hashes.

See [development](development.md) before updating evidence or publication files.
