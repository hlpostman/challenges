# test_interleave.py
# 22 April 2018

import pytest
import interleave
from itertools import chain

# Extreme input
def test_null_input():
    assert interleave.interleave([]) == []
def test_singleton_input():
    assert interleave.interleave([4]) == [4]
def test_no_visible_chanage():
    assert interleave.interleave([1,2]) == [1,2]
    assert interleave.interleave([3,3,3,3,3]) == [3,3,3,3,3]
def test_smallest_size_visible_change():
    assert interleave.interleave([1,2,3]) == [1,3,2]
    assert interleave.interleave([1,2,3,4]) == [1,4,2,3]
def test_large_input():
    a = [i for i in range(10000)]
    b_1 = [i for i in range(5000)]
    b_2 = [i for i in range(9999, 4999, -1)]
    b = list(chain.from_iterable((b_1[i], b_2[i]) for i in range(5000)))
    assert interleave.interleave(a) == b

# Bad input
def test_non_stack_input():
    with pytest.raises(TypeError):
        interleave.interleave()
        interleave.interleave([],[])
        interleave.interleave("a")
        interleave.interleave(1)
