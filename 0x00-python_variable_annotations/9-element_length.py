#!/usr/bin/env python3
"""This module has a function that returns an iterable list"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """returns values with the appropriate types
    (Sequence, Iterable, List and Tuple)
    """
    return [(i, len(i)) for i in lst]
