# interleave.py
# 26 April 2018

import pytest

def interleave(stack):
    """Takes a stack and interleaves the elements in place.

    Args:
        stack: A list

    Returns:
        None

    Raises:
        TypeError: An error occured due to non-list input.
    """
    for i in range(1,len(stack)):
        queue = []
        for j in range(len(stack) - i):
            queue.append(stack.pop())
        stack.extend(queue)
