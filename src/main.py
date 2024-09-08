"""Main router of FastAPI"""

from typing import Union, Annotated
from fastapi import FastAPI, Query
from handlers.calc import sum_handler, SumRes, \
                          law_of_cosine_handler, LawOfCosRes
from handlers.item import list_items_handler, Items, \
                          add_item_handler, AddItemReq, ItemManipulationRes, \
                          remove_item_handler, \
                          update_item_handler, Item, \
                          clear_items_handler
from handlers.param import param_generator, param_examples
from basemodels.param_basemodel import ValidatedParamInputRes

app = FastAPI()

#------------------------------------------------------------------------------#
# Basic HTTP with a path parameter                                             #
#------------------------------------------------------------------------------#

@app.get("/sum/{items}")
def sum_items(items: str) -> Union[SumRes, None]:
    """Basic get router for adding numbers together."""
    return sum_handler(items)

#------------------------------------------------------------------------------#
# Multiple path parameter with query parameter                                 #
#------------------------------------------------------------------------------#

@app.get("/law_of_cos/side1/{side1}/side2/{side2}")
async def law_of_cosine(side1: str, side2: str, angle: str = "90.0") -> Union[LawOfCosRes, None]:
    """Basic get router for calculating 3rd side of a triangle based on 2 sides
       and of their respective closed angle"""
    return law_of_cosine_handler(side1, side2, angle)

#------------------------------------------------------------------------------#
# Request body, other HTTP methods, CRUD implementation                        #
#------------------------------------------------------------------------------#

@app.get("/items")
async def list_items() -> Items:
    """Basic get router to list the stored items"""
    return list_items_handler()

@app.post("/items")
async def add_item(input_item: AddItemReq) -> Union[ItemManipulationRes, None]:
    """Basic post router to add new item to the storage"""
    return add_item_handler(input_item)

@app.delete("/items/")
async def delete_item(item_to_be_removed: str) -> Union[ItemManipulationRes, None]:
    """Basic delete router to remove an item from the storage"""
    return remove_item_handler(item_to_be_removed)

@app.put("/items")
async def update_item(updated_item: Item) -> Union[ItemManipulationRes, None]:
    """Basic put router to update an item in the storage"""
    return update_item_handler(updated_item)

@app.delete("/items/all")
async def clear_items() -> ItemManipulationRes:
    """Clear all items stored, used for testing"""
    return clear_items_handler()

#------------------------------------------------------------------------------#
# Query parameter input validation                                             #
#------------------------------------------------------------------------------#

@app.get("/validate")
async def param_input_validator(
    param: Annotated[str | None,
                     Query(default_factory = param_generator,
                           title = "Param validator 3000",
                           description = "Validates if the input starts with 'param'",
                           min_length = 6,
                           max_length = 70,
                           pattern = r'^param.*',
                           examples = param_examples,
                           openapi_examples = param_examples)]
) -> ValidatedParamInputRes:
    """Validates query parameter"""
    return {"validation": f"success, {param} is valid"}
