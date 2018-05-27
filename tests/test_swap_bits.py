# test_swap_bits.py
# 27 May 2018

import pytest
from algorithms.swap_bits import swap_bits

# Test valid input

def test_basic_input():
# n = 37 bin => 100101, i = 0, j = 1 => 38 bin =>100110
    assert swap_bits(37,0,1) == 38

def test_basic_input1():
# Test symmetry with respect to test_basic_input()
    assert swap_bits(37,1,0) == 38

def test_ij_is_leading_zero():
# Test i or j is leading zero
# n = 5 bin => 101, i = 10, j = 1 => 1,028 bin => 10000000100
    assert swap_bits(5,10,0) == 1028

def test_ij_are_same():
# Test i and j the same
    assert swap_bits(10,1,1) == 10

def test_n_is_negative():
# Test n negative
    assert swap_bits(-7,0,1) == -6

def test_twos_complement():
# Test i or j is 2's complement. Because of the arbitrary precision of integers
# in Python, swap_bits(3,63,0) does not return -2.
    assert swap_bits(3,63,0) == 9223372036854775810

def test_arbitrary_precision():
# Test that there is no overflow as per Python integer arbitrary precision
    assert swap_bits(3,65, 0) == 36893488147419103234

# Test bad input

def test_bad_values():
    with pytest.raises(ValueError):
        # i or j negative raises ValueError
        swap_bits(5,-1,0)
        # n greater than 2^64-1 or less than -(2^64)
        swap_bits(18446744073709552000, 1,0)
        swap_bits(-18446744073709552001, 1,0)

def test_bad_types():
    with pytest.raises(TypeError):
        # n, i, or j is float
        swap_bits(37.0,1,0)
        swap_bits(37,1.0,0)
        swap_bits(37,1,0.0)
        # n, i, or j is not even a number
        swap_bits([],"",())
