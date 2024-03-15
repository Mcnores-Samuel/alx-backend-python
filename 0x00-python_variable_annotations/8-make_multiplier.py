#!/usr/bin/env python3
"""This module has a function make_multiplier that takes
a float multiplier as argument and returns a function that
multiplies a float by multiplier.
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Returns a callable function for additional calculations"""
    def func_mlt(n: float) -> float:
        """returns float number"""
        return multiplier * n
    return func_mlt
