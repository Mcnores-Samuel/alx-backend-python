#!/usr/bin/env python3
"""This module has a wait_random function which takes in an integer argument
(max_delay, with a default value of 10) named wait_random that waits
for a random delay between 0 and max_delay (included and float value)
seconds and eventually returns it.
"""
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """Takes an integer and awaits for a coroutine execution of
    random seconds and returns the random seconds float number.
    """
    rand = random.uniform(0, max_delay)
    await asyncio.sleep(rand)
    return rand
