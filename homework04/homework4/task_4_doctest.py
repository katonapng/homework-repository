"""
Write a function that takes a number N as
an input and returns N FizzBuzz numbers*
Write a doctest for that function.

Definition of done:
 - function is created
 - function is properly formatted
 - function has doctests
 - doctests are run with pytest command

You will learn:
 - the most common test task for developers
 - how to write doctests
 - how to run doctests


assert fizzbuzz(5) == ["1", "2", "fizz", "4", "buzz"]

* https://en.wikipedia.org/wiki/Fizz_buzz
** Энциклопедия профессора Фортрана page 14, 15,
"Робот Фортран, чисть картошку!"
"""
from typing import List


def fizzbuzz(n: int) -> List[str]:
    """Return list of n FuzzBuzz numbers, n is an exact integer

    >>> fizzbuzz(5)
    [1, 2, 'fizz', 4, 'buzz']

    >>> fizzbuzz(15)
    [1, 2, 'fizz', 4, 'buzz', 'fizz', 7, 8, 'fizz',
    'buzz', 11, 'fizz', 13, 14, 'fizzbuzz']

    >> fizzbuzz(0)
    []

    >>> fizzbuzz(-1)
    []

    >>> fizzbuzz(1.2)
    Traceback (most recent call last):
        ...
    ValueError: n must be an integer
    """
    if not isinstance(n, int):
        raise ValueError("n must be an intege")
    return ["fizzbuzz" if number % 15 == 0 else "buzz" if number % 5 == 0 else
            "fizz" if number % 3 == 0 else number
            for number in range(1, n + 1)]
