# OpenAST threat model

An attacker can change surrounding text, copy or relocate markers, replay images,
relay live responses, substitute action fields, alter payloads, and race duplicate
requests or revocation. The key store, verifier, clock, configured display signer,
owner signer and SQLite administrator are trusted.

- Tampering and unconfigured signers fail cryptographic verification.
- Session, audience, principal, purpose, resource and argument changes fail binding.
- Expired, revoked, unregistered and consumed grants cannot create a new receipt.
- A valid live response relayed without modification can be accepted when the
  contract asks only for signed/fresh/request-bound evidence. Requiring physical
  proximity or scene association is unsupported and must be denied.
- A compromised configured display can sign false statements. The system cannot
  infer scene truth, honest pixels or a person's consent from that signature.
- Multiple decoded QR markers are rejected, but absence of every hidden marker
  is not established. Decoding is not a full-image authenticity test.
- No encryption, secrecy of surrounding speech/text, model-output control,
  challenge-distribution authentication or production key enrollment is supplied.

The software consumes generated images and user-supplied image files. Benchmarks
apply synthetic transformations; no camera, live relay, LLM or physical trial has
been run. Native image decoders remain attack surface despite input bounds.
