#!/usr/bin/env python3
"""This module has a functions with the types
of the elements of the input are not known
"""
from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """The types of the elements of the input are not known"""
    if lst:
        return lst[0]
    else:
        return None
