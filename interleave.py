# interleave.py
# 26 April 2018

import pytest

def interleave(stack):
    # Takes a stack and interleaves the elements in place.
    # This function has a side effect and no return value.
    for i in range(1,len(stack)):
        queue = []
        for j in range(len(stack) - i):
            queue.append(stack.pop())
        stack.extend(queue)
