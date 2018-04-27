# interleave_with_optional_arguments.py
# 26 April 2018

from collections import deque

def interleave(stack, n=1, offset=0):
    """Takes a stack and interleave the elements in place.

    Interleaves the elements of the stack in groups of size n,
    starting at index offset.  This means that the first
    offset + n elements remain in their original order, with
    elements from the back first appearing at index n+offset.
    If n does not divide evenly the length of stack[offset:],
    performs as many full interweaves as possible and continues
    the interweave on the remainder of the elements

    Args:
        stack: A list.  This list gets modified in place.
        n: An optional argument of integer type. The default
            value is 1. Valid values for n are strictly positive
            integers. Numbers less than 1 are treated as 1.  If
            n is greater than the length of stack[offset:], then
            the stack is unchanged.
        offset: An optional argument of integer type. The default
            value is 0. Valid values for offset are non-negative
            integers. Numbers less than 0 will be treated as 0. If
            the value is equal to or greater than the length of the
            stack passed as the first argument, then the stack is
            unchanged.
    Returns:
        None
    Raises:
        TypeError: An error occurred due to non-list input in the first
            argument, or non-number input in the second or third arguments.
            Note that negative floating point values less than the default
            values of the second and third arguments do NOT raise TypeError,
            because the first two lines of the routine overide such values
            with the default value.
    """
    n = n if n >= 1 else 1
    offset = offset if offset >= 0 else 0
    queue = deque()
    for i in range(n,len(stack[offset:]),n):
        for j in range(len(stack[offset:]) - i):
            queue.append(stack.pop())
        for k in range(len(queue)):
            stack.append(queue.popleft())
