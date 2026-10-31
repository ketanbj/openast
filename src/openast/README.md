# Implementation map

- `protocol.py`: request-bound signed display response and exact statement appraisal.
- `visual.py`: QR raster encoding, ZXing decoding and bounded image/compression input.
- `cli.py`: runnable local demo and unauthenticated public-evidence decoder.
- `modality_trust` (umbrella `core/`): permission, replay and durable local receipts.

The decoder does not authenticate the signer; the gateway does. A signed statement
does not authenticate neighboring content, the full image, location or proximity.
