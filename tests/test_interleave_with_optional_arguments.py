# test_interleave_with_optional_arguments.py
# 26 April 2018

import pytest
import interleave_with_optional_arguments as interleave
from itertools import chain

# Valid extreme input
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

# Valid optional arguments specified - n only
def test_n_specified():
    stack = [i for i in range(15)]
    interleave.interleave(stack, n=3)
    assert stack == [0,1,2,14,13,12,3,4,5,11,10,9,6,7,8]
def test_n_smaller_than_stack_length_but_does_not_divide_stack_length():
    stack = [i for i in range(10)]
    interleave.interleave(stack, n=6)
    assert stack == [0,1,2,3,4,5,9,8,7,6]
def test_n_larger_than_stack_length():
    stack = [i for i in range(10)]
    interleave.interleave(stack, n=11)
    assert stack == [0,1,2,3,4,5,6,7,8,9]
def test_large_input_with_n_specified():
    a = [i for i in range(10000)]
    b_1 = [i for i in range(5000)]
    b_2 = [i for i in range(9999, 4999, -1)]
    b = list(chain.from_iterable((b_1[i], b_1[i+1], b_2[i], b_2[i+1]) for i in range(0,5000,2)))
    interleave.interleave(a, n=2)
    assert a == b

# Valid optional arguments specified - offset only
def test_offset_specified():
    stack = [i for i in range(10)]
    interleave.interleave(stack, offset=3)
    assert stack == [0,1,2,3,9,4,8,5,7,6]
def test_offset_larger_than_stack_length():
    stack = [1,2,3,4,5]
    interleave.interleave(stack, offset = 10)
    assert stack == [1,2,3,4,5]
def test_large_input_with_offset_specified():
    a = [i for i in range(10000)]
    b_1 = [i for i in range(5000,7500)]
    b_2 = [i for i in range(9999, 7499, -1)]
    b = [i for i in range(5000)]+list(chain.from_iterable((b_1[i], b_2[i]) for i in range(2500)))
    interleave.interleave(a, offset=5000)
    assert a == b

# Valid optional arguments specified - both n and offset
def test_n_and_offset_specified():
    stack = [i for i in range(15)]
    interleave.interleave(stack, n=2, offset=5)
    assert stack == [0,1,2,3,4,5,6,14,13,7,8,12,11,9,10]
def test_n_and_offset_less_than_stack_lenght_but_sum_too_large():
    stack = [i for i in range(15)]
    interleave.interleave(stack,n=5,offset=10)
    assert stack == [i for i in range(15)]
def test_large_input_with_both_n_and_offset_specified():
    a = [i for i in range(10000)]
    b_1 = [i for i in range(5000,7500)]
    b_2 = [i for i in range(9999, 7499, -1)]
    b = [i for i in range(5000)]+list(chain.from_iterable((b_1[i],b_1[i+1],b_1[i+2],b_1[i+3],b_1[i+4],b_2[i],b_2[i+1],b_2[i+2],b_2[i+3],b_2[i+4]) for i in range(0,2500,5)))
    interleave.interleave(a, n=5, offset=5000)
    assert a == b

# Bad input
def test_non_stack_first_argument():
    with pytest.raises(TypeError):
        interleave.interleave()
        interleave.interleave("a")
        interleave.interleave(1)
def test_non_integer_optional_arguments():
    with pytest.raises(TypeError):
        interleave.interleave([1,2,3,4],n=3.2)
        interleave.interleave([1,2,3,4],n="a")
        interleave.interleave([1,2,3,4],n=1,offset=1.5)
        interleave.interleave([1,2,3,4],n=1,offset="a")
def test_too_small_optional_arguments():
    stack1 = [1,2,3,4]
    interleave.interleave(stack1, n = -5)
    assert stack1 == [1,4,2,3]
    stack2 = [1,2,3,4]
    interleave.interleave(stack2, n=1, offset = -5)
    assert stack2 == [1,4,2,3]
