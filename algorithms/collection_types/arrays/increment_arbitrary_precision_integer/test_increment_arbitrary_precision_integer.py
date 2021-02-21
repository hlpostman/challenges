# test_increment_arbitrary_precision_integer.py
# 26 July 2018

import pytest
from increment_arbitrary_precision_integer import increment_arbitrary_precision_integer as increment

# Test valid

def test_basic_input():
    assert increment([1,2,3]) == [1,2,4]
    assert increment([0]) == [1]

def test_carry_case_basic():
    assert increment([1,9]) == [2,0]
    assert increment([1,0,9]) == [1,1,0]

def test_carry_case_max():
    assert increment([9]) == [1,0]
    assert increment([9,9,9]) == [1,0,0,0]

def test_empty_array():
    # No op
    assert increment([]) == []

def test_large_input():
    large_input = [1] + [0 for i in range(100000)]
    large_output = large_input[:-1] + [1]
    assert increment(large_input) == large_output

# Test bad input

# Test TypeError

def test_float_array():
    with pytest.raises(TypeError):
        increment([1.0, 3.56])

def test_non_numeric_array():
    with pytest.raises(TypeError):
        increment(["",[],(),{}])

def test_non_array_input():
    with pytest.raises(TypeError):
        increment(1)
    with pytest.raises(TypeError):
        increment("")
    with pytest.raises(TypeError):
        increment({})
    with pytest.raises(TypeError):
        increment(())

def test_wrong_number_of_arguments():
    # No arguments
    with pytest.raises(TypeError):
        increment()
    # Too many arguments
    with pytest.raises(TypeError):
        increment([1],[1])

# Test ValueError

# Array elements must be in range(0,10)
def test_array_element_out_of_range_big():
    with pytest.raises(ValueError):
        increment([10])

def test_array_element_out_of_range_small():
    with pytest.raises(ValueError):
        increment([-1])
