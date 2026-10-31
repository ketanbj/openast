import base64
import zlib

import pytest
from modality_trust import Action, Signer, digest
from PIL import Image

from openast.protocol import respond
from openast.visual import PREFIX, _inflate, decode, encode


@pytest.fixture
def evidence():
    action = Action("agent", "record", "order/42", "pickup", {"statement_digest": digest({"ready": True})})
    challenge = dict(
        v=1,
        audience="backend",
        modality="sight",
        nonce="a" * 32,
        session="b" * 32,
        request_digest=action.digest,
        issued_at=1000,
        expires_at=1030,
    )
    return respond(Signer.generate("display"), challenge, action, {"ready": True}, now=1000)


def test_real_png_roundtrip(tmp_path, evidence):
    path = tmp_path / "code.png"
    encode(evidence).save(path)
    assert decode(path) == evidence


def test_rotated_roundtrip(evidence):
    assert decode(encode(evidence).transpose(Image.Transpose.ROTATE_90)) == evidence


def test_multiple_markers_rejected(evidence):
    code = encode(evidence)
    canvas = Image.new("RGB", (code.width * 2 + 50, code.height + 40), "white")
    canvas.paste(code, (0, 20))
    canvas.paste(code, (code.width + 50, 20))
    with pytest.raises(ValueError):
        decode(canvas)


@pytest.mark.parametrize("image", [b"not-an-image", Image.new("RGB", (20, 20)), Image.new("L", (4096, 2048))])
def test_bad_images_rejected(image):
    with pytest.raises(ValueError):
        decode(image)


def test_compression_bomb_and_trailing_data_rejected():
    text = PREFIX + base64.b85encode(zlib.compress(b"a" * 1000000)).decode()
    with pytest.raises(ValueError):
        _inflate(text)
    text = PREFIX + base64.b85encode(zlib.compress(b"{}") + b"trailing").decode()
    with pytest.raises(ValueError):
        _inflate(text)


def test_statement_must_match_exact_action():
    action = Action("agent", "record", "order/42", "pickup", {"statement_digest": digest({"ready": True})})
    challenge = dict(
        v=1,
        audience="backend",
        modality="sight",
        nonce="a" * 32,
        session="b" * 32,
        request_digest=action.digest,
        issued_at=1000,
        expires_at=1030,
    )
    with pytest.raises(ValueError, match="statement"):
        respond(Signer.generate("display"), challenge, action, {"ready": False}, now=1000)
