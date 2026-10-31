"""Request-bound signed display responses. The display key is configured out of band."""

from modality_trust import Action, Signer, digest
from modality_trust.crypto import exact, identifier
from modality_trust.gateway import validate_challenge


def respond(signer: Signer, challenge: dict, action: Action, statement: dict, *, now: int) -> bytes:
    validate_challenge(challenge, now=now, modality="sight")
    if challenge["request_digest"] != action.digest:
        raise ValueError("challenge is for another action")
    observation = dict(
        profile="signed-qr-v1", resource=action.document["resource"], statement_digest=digest(statement)
    )
    appraise(observation, challenge, action.document)
    return signer.sign("sight-evidence", {"challenge": challenge, "observation": observation})


def appraise(observation: dict, challenge: dict, action: dict) -> frozenset[str]:
    exact(observation, ("profile", "resource", "statement_digest"))
    identifier(observation["resource"])
    identifier(observation["statement_digest"])
    if observation["profile"] != "signed-qr-v1" or observation["resource"] != action["resource"]:
        raise ValueError("visual resource/profile mismatch")
    expected = action["arguments"].get("statement_digest")
    if expected is None or observation["statement_digest"] != expected:
        raise ValueError("display statement differs from exact requested claim")
    # The resource name is a signed assertion. It is not a physical association.
    return frozenset({"signed-statement"})
