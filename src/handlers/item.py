"""Dummy internal item storage"""

from typing import List, Union
from hashlib import sha256
from datetime import datetime
from fastapi import HTTPException
from basemodels.item_basemodels import Item, Items, ItemManipulationRes, AddItemReq

MAX_ITEMS = 3
items: List[Item] = []

def list_items_handler() -> Items:
    """Returns the inner storage content"""
    return {"items": items}

def add_item_handler(input_item: AddItemReq) -> Union[ItemManipulationRes, None]:
    """Add an item to the storage"""
    if len(items) >= MAX_ITEMS:
        raise HTTPException(status_code = 507, detail="Server can't store more " \
                                                      "than " + str(MAX_ITEMS) + " items " \
                                                      "at once. Delete an item first " \
                                                      "to store this one.")
    item = Item(item_id = sha256((input_item.item_name +
                                  str(input_item.item_price) +
                                  str(input_item.item_stock) +
                                  str(datetime.now().timestamp())).encode('utf-8'))
                          .hexdigest(),
                item_name = input_item.item_name,
                item_price = input_item.item_price,
                item_stock = input_item.item_stock)
    items.append(item)

    return {"success": "The item " + item.item_name + " has been stored."}

def remove_item_handler(item_to_be_removed: str) -> Union[ItemManipulationRes, None]:
    """Remove an item from the storage"""
    item = None
    for item_stored in items:
        if item_stored.item_id == item_to_be_removed:
            item = item_stored
            break

    if item is None:
        raise HTTPException(status_code = 400, detail = "No item with the given "\
                                                        "item id is present.")

    items.remove(item)
    return {"success": "The item " + item.item_name + " has been removed."}

def update_item_handler(updated_item: Item) -> Union[ItemManipulationRes, None]:
    """Update an item in the storage"""
    for index, item in enumerate(items):
        if item.item_id == updated_item.item_id:
            items[index] = updated_item
            return {"success": "The item " + item.item_name + " has been updated."}
    raise HTTPException(status_code = 400, detail = "No item with the given "\
                                                    "item id is present.")

def clear_items_handler() -> ItemManipulationRes:
    """Clear all items"""
    items.clear()
    return {"success": "All items have been removed."}
