"""Signed visual *claims*, not authentication of an entire image or location."""

from .protocol import appraise, respond
from .visual import decode, encode

__all__ = ["appraise", "decode", "encode", "respond"]
__version__ = "0.1.0"
