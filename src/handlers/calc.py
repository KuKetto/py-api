"""Handler for numeric operations"""

import re
from typing import Union
from fastapi import HTTPException
from response_objects.calc_response_objects import SumRes

def sum_handler(items: str) -> Union[SumRes, None]:
    """Sums comma separated numbers together"""

    # check for valid input
    if re.compile(r'.*[^0-9,.].*$').search(items):
        raise HTTPException(status_code=400, detail="Invalid input, input has a character " \
                                                    "other than a number or comma")

    item_list = items.split(',')
    # check for empty items
    if '' in item_list:
        raise HTTPException(status_code=400, detail="Invalid input, a double column is present " \
                                                    "or the input start / ends with a comma")

    if "." in items:
        total_sum = 0.0
        for item in item_list:
            total_sum += float(item)
    else:
        total_sum = 0
        for item in item_list:
            total_sum += int(item)

    return {"sum": total_sum}
