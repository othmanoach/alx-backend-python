#!/usr/bin/env python3
"""a type-annotated function named sum_list
"""


from typing import List


def sum_list(input_list: List[float]) -> float:
    '''returns their sum as a float
    '''
    return float(sum(input_list))
