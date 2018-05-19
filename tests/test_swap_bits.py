# test_swap_bits.py
# 19 May 2018

import pytest
import swap_bits.py

# Test valid input

# n = 37 bin => 100101, i = 0, j = 1 => 38 bin =>100110
assert swap_bits(37,0,1) == 38
# Test symmetry
assert swap_bits(37,1,0) == 38
# Test i or j is leading zero
# n = 5 bin => 101, i = 10, j = 1 => 1,028 bin => 10000000100
assert swap_bits(5,10,1) == 1028
# Test i and j the same
assert swap_bits(10,1,1) == 10
# Test n negative
assert swap_bits(-5,0,1) == -6
# Test i or j is 2's complement
assert swap_bits(3,63,0) == -2

# Test bad input

with pytest.raises(TypeError):
    # i or j negative raises ValueError
    swap_bits(5,-1,0)
    # n greater than 2^64-1 or less than -(2^64)
    swap_bits(18446744073709552000, 1,0)
    swap_bits(-18446744073709552001, 1,0)
