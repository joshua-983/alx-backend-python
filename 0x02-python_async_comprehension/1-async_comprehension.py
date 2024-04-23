#!/usr/bin/env python3
"""A module that returns random numbers generated asynchronously"""
from typing import List
import asyncio

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """A function that returns random numbers generated"""

    return [num async for num in async_generator()]
