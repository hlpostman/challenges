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
        closest_int_with_same_weight(0) # All bits unset
        closest_int_with_same_weight(18446744073709551615) # All bits set
        closest_int_with_same_weight(18446744073709551616) # Greater than 64

# Test bad input

def test_type_error():
    with pytest.raises(TypeError):
        closest_int_with_same_weight(1.0)
        closest_int_with_same_weight(-1)
        closest_int_with_same_weight([])
        closest_int_with_same_weight("")
        closest_int_with_same_weight(1,1)
        closest_int_with_same_weight()
