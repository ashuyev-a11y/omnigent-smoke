import pytest

from calc import add, multiply


def test_add_positive_numbers():
    assert add(2, 3) == 5


def test_add_negative_numbers():
    assert add(-1, -1) == -2


def test_add_zero():
    assert add(0, 5) == 5


def test_multiply_positive_numbers():
    assert multiply(2, 3) == 6


def test_multiply_negative_numbers():
    assert multiply(-2, -3) == 6


def test_multiply_mixed_sign_numbers():
    assert multiply(-2, 3) == -6


def test_multiply_zero():
    assert multiply(0, 5) == 0


def test_multiply_floats():
    assert multiply(1.5, 2.5) == pytest.approx(3.75)
