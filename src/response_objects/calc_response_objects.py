"""Holds response objects of handlers/calc"""

from typing_extensions import TypedDict, Union

class SumRes(TypedDict):
    """Return object of the sum handler function"""
    sum: Union[int, float]

class LawOfCosRes(TypedDict):
    """Return object of the law of cosine handler function"""
    side3: float
