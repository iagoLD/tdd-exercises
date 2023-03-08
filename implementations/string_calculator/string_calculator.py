import re


def addition(input_string: str) -> int:
    if input_string == '':
        return 0
    else:
        numbers = decompose_numbers(input_string)
        result = 0
        for n in numbers:
            number = int(n)
            if number < 0:
                raise InvalidInputException
            result += number
    return result


def decompose_numbers(input_string: str):
    if input_string.startswith('//'):
        delimiter = input_string.split('\n')[0].replace('//', '')
        return input_string.split('\n')[1].split(delimiter)
    else:
        return re.split('[\n|,]', input_string)


class InvalidInputException(Exception):
    ...