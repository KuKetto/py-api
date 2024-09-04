"""Main router of FastAPI"""

from typing import Union
from fastapi import FastAPI
from handlers.calc import sum_handler, SumRes

app = FastAPI()

@app.get("/sum/{items}")
def sum_items(items: str) -> Union[SumRes, None]:
    """Basic get handler function for adding numbers together."""
    return sum_handler(items)
