from fizzbuzz.fizz_buzzer import FizzBuzzer


def test_should_print_number_for_non_multiples_of_five_or_three():
    buzzer = FizzBuzzer()

    assert buzzer.label(1) == '1'
    assert buzzer.label(2) == '2'
    assert buzzer.label(4) == '4'


def test_should_print_fizz_for_multiples_of_three():
    buzzer = FizzBuzzer()

    assert buzzer.label(3) == 'Fizz'
    assert buzzer.label(6) == 'Fizz'


def test_should_print_buzz_for_multiples_of_five():
    buzzer = FizzBuzzer()

    assert buzzer.label(5) == 'Buzz'
    assert buzzer.label(10) == 'Buzz'


def test_should_print_fizz_buzz_for_multiples_of_three_and_five():
    buzzer = FizzBuzzer()

    assert buzzer.label(15) == 'FizzBuzz'
    assert buzzer.label(30) == 'FizzBuzz'