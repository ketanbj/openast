"""Actual QR raster channel with bounded input and ambiguity rejection.

Compression reduces QR size; the inflater is bounded independently of the image.
Payloads carry public evidence, never a permission grant or private key.
"""

import base64
import io
import zlib
from pathlib import Path

import numpy as np
import qrcode
import zxingcpp
from modality_trust.crypto import MAX_BYTES, unpack
from PIL import Image, UnidentifiedImageError

PREFIX = "OAST1:"
MAX_IMAGE_BYTES = 8 * 1024 * 1024
MAX_PIXELS = 4 * 1024 * 1024


def encode(evidence: bytes, *, box_size: int = 6) -> Image.Image:
    if type(box_size) is not int or not 2 <= box_size <= 12:
        raise ValueError("box size must be between 2 and 12")
    unpack(evidence)  # Shape/profile parsing is separate from signature appraisal.
    text = PREFIX + base64.b85encode(zlib.compress(evidence, level=9)).decode("ascii")
    if len(text) > 2000:
        raise ValueError("evidence too large for this QR profile")
    code = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_M, box_size=box_size, border=4)
    code.add_data(text)
    code.make(fit=True)
    return code.make_image(fill_color="black", back_color="white").convert("RGB")


def _inflate(text: str) -> bytes:
    if not text.startswith(PREFIX) or len(text) > 2000:
        raise ValueError("unrecognized or oversized visual payload")
    try:
        compressed = base64.b85decode(text[len(PREFIX) :].encode("ascii"))
        inflater = zlib.decompressobj()
        evidence = inflater.decompress(compressed, MAX_BYTES + 1)
        if len(evidence) > MAX_BYTES or not inflater.eof or inflater.unused_data or inflater.unconsumed_tail:
            raise ValueError("invalid compressed evidence")
        unpack(evidence)
        return evidence
    except (zlib.error, UnicodeError) as error:
        raise ValueError("invalid visual payload") from error


def decode(source: str | Path | bytes | Image.Image) -> bytes:
    try:
        if isinstance(source, Image.Image):
            image = source
        else:
            if isinstance(source, (str, Path)):
                path = Path(source)
                if path.stat().st_size > MAX_IMAGE_BYTES:
                    raise ValueError("image byte limit")
                with path.open("rb") as stream:
                    encoded = stream.read(MAX_IMAGE_BYTES + 1)
            else:
                encoded = source
            if not isinstance(encoded, bytes) or len(encoded) > MAX_IMAGE_BYTES:
                raise ValueError("image byte limit")
            image = Image.open(io.BytesIO(encoded))
        width, height = image.size
        if width < 32 or height < 32 or width * height > MAX_PIXELS or max(width, height) > 4096:
            raise ValueError("image dimension limit")
        if getattr(image, "n_frames", 1) != 1:
            raise ValueError("animated images are not supported")
        pixels = np.asarray(image.convert("L"))
        markers = zxingcpp.read_barcodes(pixels, formats=zxingcpp.BarcodeFormat.QRCode)
        if len(markers) != 1 or not markers[0].valid:
            raise ValueError("expected exactly one decodable QR marker")
        return _inflate(markers[0].text)
    except (UnidentifiedImageError, Image.DecompressionBombError, OSError) as error:
        raise ValueError("image decode failed") from error
