from unittest.mock import MagicMock

import pytest

from string_calculator.string_calculator import StringCalc, InvalidInputException


def test_empty_string_returns_zero():
    assert StringCalc().add('') == 0


def test_one_number_addition():
    assert StringCalc().add('1') == 1


def test_two_numbers_addition():
    assert StringCalc().add('1,2') == 3


def test_more_than_two_numbers_addition():
    assert StringCalc().add('1\n2,3') == 6


def test_user_defined_delimiter():
    assert StringCalc().add('//;\n1;2') == 3


def test_thrown_exception():
    with pytest.raises(InvalidInputException):
        StringCalc().add('-1,2')


def test_should_display_calculation():
    display = MagicMock()

    StringCalc(display).add('1,2,3')

    display.show.assert_called_with('1 + 2 + 3 = 6')
