"""Query paramater validation"""

from hashlib import sha256
from datetime import datetime

param_examples = {
    "example1": {"summary": "Short example", "value": "param12"},
    "example2": {"summary": "Another example", "value": "param-3423"},
    "example3": {"summary": "An another example", "value": "param0"},
    "example4": {"summary": "Another an another example", "value": "paramarap"},
    "example5": {
        "summary": "Longer example", 
        "description": "This is an example with a longer string.",
        "value": "param540e4cd92151bc159e802241775d0b459459095ed26c551a72036f81eb6a58d5"
    }
}

def param_generator() -> str:
    """generates a "random" string"""
    return "param" + sha256(str(datetime.now().timestamp()).encode('utf-8')).hexdigest()
