"""
This task is optional.

Write a generator that takes a number N as an input
and returns a generator that yields N FizzBuzz numbers*
Don't use any ifs, you can find an
approach for the implementation in this video**.


Definition of done:
 - function is created
 - function is properly formatted
 - function has tests


>>> list(fizzbuzz(5))
['1', '2', 'fizz', '4', 'buzz']

* https://en.wikipedia.org/wiki/Fizz_buzz
** https://www.youtube.com/watch?v=NSzsYWckGd4
"""
from itertools import cycle
from typing import Generator


class FizzBuzz():
    def __init__(self, n) -> None:
        self.fizz = cycle(('', '', 'fizz'))
        self.buzz = cycle(('', '', '', '', 'buzz'))
        self.numbers = [str(i) for i in range(1, n + 1)]


def fizzbuzz_generator(n: int, fb: FizzBuzz):
    for i in range(0, n):
        yield next(fb.fizz) + next(fb.buzz) or str(fb.numbers[i])


def fizzbuzz(n: int) -> Generator[str, None, None]:
    """Return return generator for FizzBuzz numbers, n is an exact integer

    >>> list(fizzbuzz(5))
    ['1', '2', 'fizz', '4', 'buzz']

    >>> list(fizzbuzz(15))
    ['1', '2', 'fizz', '4', 'buzz', 'fizz', '7', '8', 'fizz', \
'buzz', '11', 'fizz', '13', '14', 'fizzbuzz']

    >> list(fizzbuzz(0))
    []

    >>> list(fizzbuzz(-1))
    []

    >>> list(fizzbuzz(1.2))
    Traceback (most recent call last):
        ...
    ValueError: n must be an integer
    """
    if not isinstance(n, int):
        raise ValueError("n must be an integer")
    fb = FizzBuzz(n)
    return fizzbuzz_generator(n, fb)
