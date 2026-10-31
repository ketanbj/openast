import json
from pathlib import Path

from modality_trust import canonical, verify

from openast import decode


def test_public_fixture_is_exact_signed_raster():
    directory = Path(__file__).resolve().parents[1] / "examples/fixtures"
    fixture = json.loads((directory / "public.json").read_text())
    observed = decode(directory / "signed-response.png")
    assert observed == canonical(fixture["evidence"])
    verify(observed, {"fixture-display": bytes.fromhex(fixture["public_key_hex"])}, "sight-evidence")
    assert fixture["synthetic"] and not fixture["measurement_trial"]
