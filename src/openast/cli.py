"""A runnable local demonstration; all keys are ephemeral and media is generated."""

import argparse
import json
import tempfile
import time
from pathlib import Path

from modality_trust import Action, Contract, Denied, Gateway, Signer, digest, grant

from .protocol import respond
from .visual import decode, encode


def demo(directory: Path):
    directory.mkdir(parents=True, exist_ok=True)
    display, owner = Signer.generate("display.demo"), Signer.generate("owner.demo")
    statement = {"order": "demo-42", "status": "ready"}
    action = Action(
        "agent.demo",
        "record-pickup",
        "order/demo-42",
        "authorized-pickup",
        {"statement_digest": digest(statement)},
    )
    # Each invocation gets a fresh durable state file, never deletes existing state.
    with tempfile.TemporaryDirectory(prefix="openast-") as temporary:
        gateway = Gateway(
            str(Path(temporary) / "state.sqlite3"),
            audience="pickup.demo",
            attesters={"sight": {display.issuer: display.public_key}},
            delegators={owner.issuer: owner.public_key},
        )
        challenge = gateway.challenge(action, "sight")
        permission = grant(owner, action, gateway.audience, now=int(time.time()), modalities=("sight",))
        gateway.register_grant(permission)
        evidence = respond(display, challenge, action, statement, now=int(time.time()))
        path = directory / "signed-response.png"
        encode(evidence).save(path)
        observed = decode(path)
        receipt = gateway.commit(observed, permission, action, Contract("sight"))
        try:
            gateway.commit(observed, permission, action, Contract("sight"))
        except Denied as error:
            replay = str(error)
        else:
            raise RuntimeError("replay was unexpectedly accepted")
        report = {
            "receipt": receipt,
            "replay": replay,
            "effects": len(gateway.effects()),
            "channel": "generated PNG -> ZXing QR decoder",
            "physical_camera_trial": False,
        }
    (directory / "report.json").write_text(json.dumps(report, indent=2) + "\n")
    return report


def main():
    parser = argparse.ArgumentParser(description="OpenAST experimental signed visual evidence")
    commands = parser.add_subparsers(dest="command", required=True)
    run = commands.add_parser("demo")
    run.add_argument("--output", type=Path, default=Path("output/demo"))
    read = commands.add_parser("decode", help="decode public evidence; does not authenticate it")
    read.add_argument("image", type=Path)
    args = parser.parse_args()
    if args.command == "demo":
        print(json.dumps(demo(args.output), indent=2))
    else:
        print(decode(args.image).decode("ascii"))
