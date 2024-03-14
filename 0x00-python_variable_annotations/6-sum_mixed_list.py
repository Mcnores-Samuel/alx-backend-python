#!/usr/bin/env python3
"""This module has a function sum_mixed_list which takes
a list mxd_lst of integers and floats and returns
their sum as a float.
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """takes a list mxd_lst of integers and floats and
    returns their sum as a float.
    """
    result: float = 0.0
    for n in mxd_lst:
        result += n
    return result
