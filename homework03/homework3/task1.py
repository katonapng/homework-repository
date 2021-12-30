from functools import wraps
from typing import Callable


def create_hash_cell(func: Callable, cached: dict, *args):
    value = func(*args)
    cached[args] = [value, 0]
    return value


def cache(times: int) -> Callable:
    max_calls = times

    def cache_func(func: Callable) -> Callable:
        cached = {}

        @wraps(func)
        def wrapper(*args):
            try:
                if cached[args][1] < max_calls:
                    cached[args][1] += 1
                    return cached[args][0]
                else:
                    cached.pop(args)
                    return create_hash_cell(func, cached, *args)
            except KeyError:
                return create_hash_cell(func, cached, *args)
        return wrapper
    return cache_func


@cache(times=2)
def f():
    return input('? ')


@cache(times=2)
def g(value):
    return value/2
