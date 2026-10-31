"""SDK example: generated display evidence, exact owner permission, local receipt."""

import tempfile
from pathlib import Path

from modality_trust import Action, Contract, Gateway, Signer, digest, grant

from openast import decode, encode, respond

now = 1000000  # deterministic demo clock; use a trusted current clock in an integration
statement = {"order": "42", "status": "ready"}
action = Action("agent", "record-pickup", "order/42", "pickup", {"statement_digest": digest(statement)})
display, owner = Signer.generate("display"), Signer.generate("owner")
with tempfile.TemporaryDirectory() as directory:
    gateway = Gateway(
        str(Path(directory) / "state.sqlite3"),
        audience="business",
        attesters={"display": display.public_key},
        delegators={"owner": owner.public_key},
        clock=lambda: now,
    )
    challenge = gateway.challenge(action, "sight")
    evidence = respond(display, challenge, action, statement, now=now)
    observed = decode(encode(evidence))
    permission = grant(owner, action, "business", now=now, modalities=("sight",))
    gateway.register_grant(permission)
    print(gateway.commit(observed, permission, action, Contract("sight")))
