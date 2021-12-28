"""
Write a context manager, that suppresses passed exception.
Do it both ways: as a class and as a generator.

>>> with suppressor(IndexError):
...    [][2]

"""

from contextlib import contextmanager


@contextmanager
def suppressor(error):
    try:
        yield
    except error:
        pass


class Suppressor:
    def __init__(self, error, *args, **kwargs) -> None:
        self.error = error

    def __enter__(self):
        return self.error

    def __exit__(self, type, value, traceback):
        if type == self.error:
            return True
        return False
