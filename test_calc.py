import pytest

from calc import add, divide, multiply


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


def test_divide_positive_numbers():
    assert divide(6, 3) == 2


def test_divide_negative_numbers():
    assert divide(-6, -3) == 2


def test_divide_mixed_sign_numbers():
    assert divide(-6, 3) == -2


def test_divide_floats():
    assert divide(7.5, 2.5) == pytest.approx(3.0)


def test_divide_by_zero_raises():
    with pytest.raises(ValueError, match="cannot divide by zero"):
        divide(5, 0)
