# openast agent guide

OpenAST produces signed visual claims for exact agent requests. It performs QR
raster encoding/decoding; the shared core appraises evidence and owner permission.
It does not authenticate the surrounding scene, location or human consent.

## Read first

`README.md` -> `docs/README.md` -> `docs/architecture.md` -> `docs/code-map.md`.

## Commands

Run from this repository root, in a Python 3.11+ virtual environment:

```sh
make install                          # sibling umbrella or recursive checkout
make help
make demo
make test
make lint
make check-docs
make verify-evidence
```

Set `CORE=/path/to/open-modality-trust/core` if automatic layout detection does
not apply. `make install-benchmark` adds optional plot/transform dependencies.
`make benchmark` writes a new report to ignored `output/`, preserving recorded
results. See `docs/development.md` before regenerating publication artifacts.

## Change map

| Change | Start with | Closest tests |
|---|---|---|
| Signed visual statement/action binding | `src/openast/protocol.py` | `tests/test_visual.py`, umbrella `core/tests` |
| QR and bounded image parsing | `src/openast/visual.py` | `tests/test_visual.py` |
| CLI demo/output | `src/openast/cli.py` | `make demo`, `tests/test_visual_fixture.py` |
| Shared grant/receipt checks | umbrella `core/src/modality_trust/gateway.py` | umbrella `core/tests/test_core.py` |
| Measured evidence | `scripts/benchmark.py`, `scripts/verify_evidence.py` | recorded `docs/benchmarks/` report |

## Important boundaries

Decoding a QR is not signature verification. Preserve image/decompression bounds
and ambiguity rejection. Only the configured display key can endorse its specific
structured statement; the separate owner key supplies permission.

## Working rules

- Read the task guide and closest code/tests before editing; use `rg` to navigate.
- Keep changes within the requested behavior. Explain changed guarantees in the
  architecture/threat model and cover them with relevant protocol tests.
- Preserve the separation between observations, verified claims and permission.
  Never promote a fresh signature to location, or a contact report to consent.
- Recorded benchmarks and publication artifacts are evidence. Do not hand-edit
  numeric results or overwrite historical reports to hide a mismatch. Exploratory
  benchmarks go in ignored `output/`; docs-only changes need no benchmark rerun.
- New or changed relative Markdown links should pass `make check-docs`.
- Keep keys, grants, credentials, recordings and databases out of commits. Public fixtures
  must be explicitly synthetic or have documented rights; public verification
  keys are distinct from private signing credentials.
- Publishing a package, running paid/provider integrations and submitting papers
  are separate tasks; the local demo and normal checks require none of them.
