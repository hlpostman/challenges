# test_closest_int_with_same_weight.py
# 13 June 2018

import pytest
import closest_int_with_same_weight


# Test valid input
def test_basic_case_1():
    assert closest_int_with_same_weight(1) == 2

def test_extreme_case_1():
    assert closest_int_with_same_weight(0) == 0

def test_lsb_neighbor_already_set():
    assert closest_int_with_same_weight(3) == 5

# Test bad input
