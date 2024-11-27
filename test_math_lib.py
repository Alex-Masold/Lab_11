import pytest
from math_lib import *
from Point import *

def test_multiply():
    assert multiply(3, 10) == 30

def test_divide():
    assert divide(14, 2) == 7
    with pytest.raises(ValueError):
        divide(1, 0)

def test_distanse():
    p1: Point = Point(1, 5)
    p2: Point = Point(4, 9)
    assert distanse(p1, p2) == 5


def test_quadratic_solver():
    assert quadratic_solver(1, -3, 2) == (2, 1) 
    assert quadratic_solver(1, 2, 1) == -1
    assert quadratic_solver(1, 2, 5) == None

def test_geometric_sum():
    geometric_sum(1, 2, 4) == 15