"""Handler for numeric operations"""

from typing import Union
from math import radians, cos, sqrt
from common_lib.input_validation import check_user_input, validate_geometry_side, \
                                        validate_geometry_angle
from basemodels.calc_basemodels import SumRes, LawOfCosRes

def sum_handler(items: str) -> Union[SumRes, None]:
    """Sums comma separated numbers together"""
    check_user_input(items, r'^(\d+(\.\d+)?)((,\d+(\.\d+)?)+)?$')

    item_list = items.split(',')
    if "." in items:
        total_sum = 0.0
        for item in item_list:
            total_sum += float(item)
    else:
        total_sum = 0
        for item in item_list:
            total_sum += int(item)

    return {"sum": total_sum}

def law_of_cosine_handler(side1: str, side2: str, angle: float) -> Union[LawOfCosRes, None]:
    """Calculates law of cosine"""
    check_user_input(side1, r'^\d+(\.\d+)?$')
    check_user_input(side2, r'^\d+(\.\d+)?$')
    check_user_input(angle, r'^\d+(\.\d+)?$')

    s1 = validate_geometry_side(side1)
    s2 = validate_geometry_side(side2)
    a = validate_geometry_angle(angle)
    side3 = sqrt(pow(s1, 2) + pow(s2, 2) - 2 * s1 * s2 * cos(radians(a)))

    return {"side3": side3}
            