#!/usr/bin/env python3
"""This module contains wait_n function that takes in 2 int
arguments (in this order): n and max_delay.it spawns
wait_random n times with the specified max_delay
"""
from typing import List
import asyncio


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Takes in 2 int arguments (in this order): n and max_delay and
    spawns wait_random n times with the specified max_delay

    returns the list of all the delays (float values) in ascending order.
    """
    result = await asyncio.gather(
        *tuple(map(lambda _: task_wait_random(max_delay), range(n)))
    )
    return sorted(result)
