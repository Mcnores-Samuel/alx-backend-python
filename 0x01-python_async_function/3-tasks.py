#!/usr/bin/env python3
"""This module contains a task_wait_random function
return an instance of the asyncio task in progress.
"""
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay):
    """Takes an integer max_delay and returns a asyncio.Task."""
    return asyncio.create_task(wait_random(max_delay))
