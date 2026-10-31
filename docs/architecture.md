# OpenAST architecture

A pickup assistant wants to record that an order is ready. A participating display
can sign that exact structured claim; an unrelated sign or overlay must not gain
its authority. The business still needs a separate owner grant to permit the
assistant's exact action.

`Action -> stored challenge -> signed display response -> QR raster -> decoder
-> independent appraisal + current grant -> durable local receipt`

`respond` checks the challenge's action digest and statement digest. `encode`
compresses the public evidence and encodes a QR marker; `decode` bounds file size,
pixels and decompression and requires one decoded QR marker. ZXing handles the
raster channel. A decoded payload remains unauthenticated until the gateway checks
its signature and context. Marker ambiguity is rejected when multiple QR symbols
are detected. Hidden/undecodable symbols cannot be guaranteed absent.

The observation includes only a profile, resource name and exact statement digest.
It proves that a configured display key signed those bytes in response to the
challenge. It does not authenticate the full image or prove where the display is.
Neighboring text is neither parsed nor endorsed. There is no LLM in the benchmark.

## Enforcement and trust

The verifier and gateway clock are trusted. Public keys are pinned out of band;
the demo generates them locally. Separate attester and owner trust maps prevent
an observation key from acting as the permission signer. A grant binds an exact
immutable principal/action/resource/purpose/arguments digest and business audience.
Nonce/session scope prevents reusing an old signed response for a new interaction.
A configured signer can lie; key possession is not identity proofing.

The SQLite write lock is the reference linearization boundary. Current grant and
issuer revocation, expiry, challenge/grant consumption and local receipt insertion
are checked in one transaction. After restart, consumed state remains unavailable.
No remote callback, payment, lock or robot movement is included in that guarantee.
Replay-state cleanup, account enrollment, clock synchronization and deployment
hardening remain work for production integration.

## Encoding

The shared local signing profile uses sorted ASCII-escaped JSON and a domain
separator, Ed25519, explicit version/kind/issuer fields, 32 KiB message bounds,
depth/collection limits and duplicate-key rejection. Floats, nonfinite values,
unknown fields and boolean timestamps are rejected. Signatures authenticate
structured bytes only. This profile is not JOSE, COSE, RFC 8785, or the draft
umbrella evidence schema. No wire interoperability is asserted.
