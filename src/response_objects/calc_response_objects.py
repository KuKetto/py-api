"""Holds response objects of handlers/calc"""

from typing_extensions import TypedDict, Union

class SumRes(TypedDict):
    """Return object of the sum handler function"""
    sum: Union[int, float]
