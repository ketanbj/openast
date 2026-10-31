"""Export an explicitly synthetic public fixture; private keys are never written."""

import json
from pathlib import Path

from modality_trust import Action, Signer, digest, unpack

from openast import encode, respond

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "fixtures"
OUT.mkdir(exist_ok=True)

statement = {"order": "fixture-42", "status": "ready"}
action = Action(
    "fixture-agent", "record", "order/fixture-42", "fixture", {"statement_digest": digest(statement)}
)
signer = Signer.generate("fixture-display")
challenge = dict(
    v=1,
    audience="fixture-backend",
    modality="sight",
    nonce="synthetic-visual-nonce",
    session="synthetic-visual-session",
    request_digest=action.digest,
    issued_at=1000,
    expires_at=1030,
)
evidence = respond(signer, challenge, action, statement, now=1000)
encode(evidence).save(OUT / "signed-response.png")
(OUT / "public.json").write_text(
    json.dumps(
        {
            "synthetic": True,
            "measurement_trial": False,
            "public_key_hex": signer.public_key.hex(),
            "action": action.document,
            "statement": statement,
            "evidence": unpack(evidence),
        },
        indent=2,
    )
    + "\n"
)
