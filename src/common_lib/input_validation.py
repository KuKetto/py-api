"""Library for input validation"""

import re
from typing import Union
from fastapi import HTTPException

def check_user_input(user_input: str, input_filter: str) -> None:
    """check for valid input, math operations require numbers :)"""
    if not re.compile(input_filter).search(user_input):
        raise HTTPException(status_code=400, detail="Invalid input. Possible reasons:" \
                                                    "1) Input has a character other than a " \
                                                    "number or comma." \
                                                    "2) Input has multiple commas without a " \
                                                    "number between them."\
                                                    "3) Input start with or ends in a comma.")
    return None

def validate_geometry_side(side: str) -> Union[float, None]:
    """Validates input side length, raises exception if the length is invalid"""
    converted_side = float(side)
    if converted_side <= 0.0:
        raise HTTPException(status_code=400, detail="The given side with length of " + side + " " \
                                                    "is not a valid geometry length.")
    return converted_side

def validate_geometry_angle(angle: str) -> Union[float, None]:
    """Validates input angle, raises exception if the angle is invalid"""
    converted_angle = float(angle)
    if converted_angle <= 0.0 or converted_angle >= 360.0:
        raise HTTPException(status_code=400, detail="The given angle of " + angle + " " \
                                                    "degrees is not a valid geometry angle.")
    return converted_angle
