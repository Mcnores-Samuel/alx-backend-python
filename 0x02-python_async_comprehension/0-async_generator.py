#!/usr/bin/env python3
"""Async Generator module for Python async comprehension"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """Async Generator function that yields random numbers"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
