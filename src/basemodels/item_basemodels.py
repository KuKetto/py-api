"""Holds typings for handlers/item"""

from typing import List
from pydantic import BaseModel

class Item(BaseModel):
    """Dummy item model"""
    item_id: str
    item_name: str
    item_price: int
    item_stock: int

class Items(BaseModel):
    """Return object of the list items handler function"""
    items: List[Item]

class ItemManipulationRes(BaseModel):
    """Return object of the any handler function manipulating the items"""
    success: str

class AddItemReq(BaseModel):
    """Input body to add an item to the storage"""
    item_name: str
    item_price: int
    item_stock: int
