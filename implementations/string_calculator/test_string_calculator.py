import pytest

from string_calculator.string_calculator import addition, InvalidInputException


def test_empty_string_returns_zero():
    assert addition('') == 0


def test_one_number_addition():
    assert addition('1') == 1


def test_two_numbers_addition():
    assert addition('1,2') == 3


def test_more_than_two_numbers_addition():
    assert addition('1\n2,3') == 6


def test_user_defined_delimiter():
    assert addition('//;\n1;2') == 3


def test_thrown_exception():
    with pytest.raises(InvalidInputException):
        addition('-1,2')
