"""Main router of FastAPI"""

from typing import Union
from fastapi import FastAPI
from handlers.calc import sum_handler, SumRes, \
                          law_of_cosine_handler, LawOfCosRes

app = FastAPI()

@app.get("/sum/{items}")
def sum_items(items: str) -> Union[SumRes, None]:
    """Basic get router for adding numbers together."""
    return sum_handler(items)

@app.get("/law_of_cos/side1/{side1}/side2/{side2}")
async def law_of_cosine(side1: str, side2: str, angle: str = "90.0") -> Union[LawOfCosRes, None]:
    """Basic get router for calculating 3rd side of a triangle based on 2 sides
       and of their respective closed angle"""
    return law_of_cosine_handler(side1, side2, angle)
