# test_closest_int_with_same_weight.py
# 16 June 2018

import pytest
from closest_int_with_same_weight import closest_int_with_same_weight


# Test valid input

def test_basic_case_1():
    assert closest_int_with_same_weight(1) == 2

def test_lsb_neighbor_already_set():
    assert closest_int_with_same_weight(3) == 5

def test_value_error():
    # No 64-bit integer with the same weight as the integer passed exists for these values.
    with pytest.raises(ValueError):
        # Value Error type 1
        # Integer size passed is invalid (not 4, 8,16, 32, or 64)
        closest_int_with_same_weight(5,2)
        closest_int_with_same_weight(5,65)

        # Value Error type 2
        # Integer is too large for the integer size passed
        closest_int_with_same_weight(18446744073709551616) # Greater than 64
        closest_int_with_same_weight(32,4)

        # Value Error type 3
        # No integer with the same weight as the integer passed exists for the integer and bit-size passed (i.e. integer is 0 and has all bits unset, or is max_int for that size and has all bits set).
        # All bits unset
        closest_int_with_same_weight(0)
        closest_int_with_same_weight(0, 8)
        # All bits set
        closest_int_with_same_weight(18446744073709551615)
        closest_int_with_same_weight(65534, 16)



# Test bad input

def test_type_error():

    with pytest.raises(TypeError):
        # Bad number of arguments
        closest_int_with_same_weight(1,1,1)
        closest_int_with_same_weight()
        # Bad type in first argument
        closest_int_with_same_weight(1.0)
        closest_int_with_same_weight(-1)
        closest_int_with_same_weight([])
        closest_int_with_same_weight("")
        # Bad type in second argument
        closest_int_with_same_weight(1, 64.0)
        closest_int_with_same_weight(1, "")
        closest_int_with_same_weight(1, [])
