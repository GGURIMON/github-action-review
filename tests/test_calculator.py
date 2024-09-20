import pytest
from src import calculator

def test_add():
    assert calculator.add(2, 3) == 5
    assert calculator.add(0, 0) == 0
    assert calculator.add(5, -3) == 2

def test_subtract():
    assert calculator.subtract(5, 3) == 2
    assert calculator.subtract(0, 0) == 0
    assert calculator.subtract(3, 5) == -2
    assert calculator.subtract(3, -3) == 6

def test_multiply():
    assert calculator.multiply(2, 3) == 6
    assert calculator.multiply(5, 0) == 0
    assert calculator.multiply(0.5, 2) == 1.0
    assert calculator.multiply(2, -3) == -6

def test_divide():
    assert calculator.divide(6, 3) == 2
    assert calculator.divide(0, 3) == 0
    assert calculator.divide(1, 2) == 0.5
    with pytest.raises(ZeroDivisionError):
        calculator.divide(3, 0)