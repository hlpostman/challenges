# test_rectangle_intersection.py
# 24 July 2018

import pytest
from rectangle_intersection import rectangle_intersection as intersection

# Test valid input

def test_boundary_intersection():
    assert intersection((0,0),(1,1),(1,1),(3,3)) == [(1,1),(1,1)]
    assert intersection((0,0),(1,1),(1,0),(1,3)) == [(1,0),(1,1)]

def test_partial_intersection():
    assert intersection((0,0),(10,10),(1,1),(30,30)) == [(1,1),(10,10)]
    assert intersection((0,0),(10,10),(1,1),(8,30)) == [(1,1),(8,10)]

def test_completely_contained():
    assert intersection((0,0),(1,1),(0,0),(1,1)) == [(0,0),(1,1)]
    assert intersection((0,0),(10,10),(2,2),(3,3)) == [(2,2),(3,3)]

def test_no_intersection():
    assert intersection((0,0),(1,1),(2,2),(3,3)) == [(float('inf'),float('inf')),(float('inf'),float('inf'))]

def test_argument_symmetry():
    # Whether the first two arguments are for rectangle A or B doesn't matter
    assert intersection((0,0),(10,10),(1,1),(30,30)) == intersection((1,1),(30,30),(0,0),(10,10))
    assert intersection((0,0),(10,10),(2,2),(3,3)) == intersection((2,2),(3,3),(0,0),(10,10))
    assert intersection((0,0),(1,1),(2,2),(3,3)) == intersection((2,2),(3,3),(0,0),(1,1))

def test_floats():
        assert intersection((0.5,0.5),(1.5,1.5),(1.5,1.5),(3.5,3.5)) == [(1.5,1.5),(1.5,1.5)]

# Test bad input

# Test TypeError
def test_non_tuple_input():
    with pytest.raises(TypeError):
        intersection("",[],{},1)

def test_non_numberic_input_in_tuples():
    with pytest.raises(TypeError):
        intersection((0,""),(1,1),(2,2),(3,3))

def test_wrong_number_of_elements_in_tuples():
    # Too few elements in the tuples
    with pytest.raises(TypeError):
        intersection((),(),(),())
    # Too many elements in the tuples (error coded by hand)
    with pytest.raises(TypeError):
        intersection((0,0),(1,1),(2,2),(3,3,3))

def test_wrong_number_of_arguments():
    # No arguments
    with pytest.raises(TypeError):
        intersection()
    # At least one argument, but not four
    with pytest.raises(TypeError):
        intersection((1,1))
    # Too many arguments
    with pytest.raises(TypeError):
        intersection((0,0),(1,1),(2,2),(3,3),(4,4))
    with pytest.raises(TypeError):
        intersection((0,0),(0,0),(0,0),(0,0),(0,0))

# Test ValueError
def test_negative_input():
    with pytest.raises(ValueError):
        intersection((0,0),(-1,1),(2,2),(3,3))
