import pytest
from app import add, subtract, multiply, divide

def test_add():
    assert add(5, 3) == 8

def test_subtract():
    assert subtract(10, 4) == 6

def test_multiply():
    assert multiply(7, 6) == 42

def test_divide():
    assert divide(9, 3) == 3

def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(9, 0)
