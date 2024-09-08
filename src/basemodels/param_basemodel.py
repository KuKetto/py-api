"""Holds typings of query parameter validation"""

from typing_extensions import TypedDict

class ValidatedParamInputRes(TypedDict):
    """Return of /validate"""
    validation: str
