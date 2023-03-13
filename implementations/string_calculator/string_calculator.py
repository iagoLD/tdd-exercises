import re
from abc import ABC, abstractmethod


class Display(ABC):
    @abstractmethod
    def show(self, string: str):
        ...


class NullDisplay(Display):
    def show(self, string: str):
        pass


class StringCalc:

    def __init__(self, display: Display = NullDisplay()):
        self._display = display

    def add(self, input_string: str) -> int:
        if input_string == '':
            return 0
        else:
            numbers = self._decompose_numbers(input_string)
            result = 0
            for n in numbers:
                number = int(n)
                if number < 0:
                    raise InvalidInputException
                result += number

            self._display.show(f"{' + '.join(numbers)} = {result}")

        return result

    def _decompose_numbers(self, input_string: str):

        match = re.match(r'^//(?P<delimiter>.)\n(?P<number_sequence>.*)$', input_string)

        if match is not None:
            return match['number_sequence'].split(match.groupdict()['delimiter'])
        else:
            return re.split(r',|\n', input_string)


class InvalidInputException(Exception):
    ...
