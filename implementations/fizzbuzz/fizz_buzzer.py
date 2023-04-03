class FizzBuzzer:
    def label(self, number: int) -> str:
        result = ''

        if number % 3 == 0:
            result = 'Fizz'

        if number % 5 == 0:
            result = f'{result}Buzz'

        if not result:
            result = str(number)

        return result
