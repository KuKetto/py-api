"""Holds response objects of handlers/calc"""

from pydantic import BaseModel

class SumRes(BaseModel):
    """Return object of the sum handler function"""
    sum: int | float

class LawOfCosRes(BaseModel):
    """Return object of the law of cosine handler function"""
    side3: float
