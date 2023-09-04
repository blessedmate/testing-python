import pytest


def fizz_buzz(value):
    if is_multiple(value, 3):
        if is_multiple(value, 5):
            return "FizzBuzz"
        return "Fizz"
    elif is_multiple(value, 5):
        return "Buzz"
    return str(value)


def is_multiple(value, mod):
    return value % mod == 0


def check_fizz_buzz(value, expected):
    response = fizz_buzz(value)
    assert response == expected


def test_returns_1():
    check_fizz_buzz(1, "1")


def test_returns_2():
    check_fizz_buzz(2, "2")


def test_returns_3():
    check_fizz_buzz(3, "Fizz")


def test_returns_5():
    check_fizz_buzz(5, "Buzz")


def test_returns_fizz():
    check_fizz_buzz(6, "Fizz")


def test_returns_buzz():
    check_fizz_buzz(10, "Buzz")


def test_returns_fizzbuzz():
    check_fizz_buzz(15, "FizzBuzz")
