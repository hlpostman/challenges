# test_interleave.py
# 26 April 2018

import pytest
import interleave
from itertools import chain

# Extreme input
def test_null_input():
    stack = []
    interleave.interleave(stack)
    assert stack == []
def test_singleton_input():
    stack = [4]
    interleave.interleave(stack)
    assert stack == [4]
def test_no_visible_chanage():
    stack1 = [1,2]
    interleave.interleave(stack1)
    assert stack1 == [1,2]
    stack2 = [3,3,3,3,3]
    interleave.interleave(stack2)
    assert stack2 == [3,3,3,3,3]
def test_smallest_size_visible_change():
    stack1 = [1,2,3]
    interleave.interleave(stack1)
    assert stack1 == [1,3,2]
    stack2 = [1,2,3,4]
    interleave.interleave(stack2)
    assert stack2 == [1,4,2,3]
def test_large_input():
    a = [i for i in range(10000)]
    b_1 = [i for i in range(5000)]
    b_2 = [i for i in range(9999, 4999, -1)]
    b = list(chain.from_iterable((b_1[i], b_2[i]) for i in range(5000)))
    interleave.interleave(a)
    assert a == b

# Bad input
def test_non_stack_input():
    with pytest.raises(TypeError):
        interleave.interleave()
        interleave.interleave([],[])
        interleave.interleave("a")
        interleave.interleave(1)
