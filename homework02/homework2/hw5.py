"""
Some of the functions have a bit cumbersome behavior when we deal with
positional and keyword arguments.

Write a function that accept any iterable of unique values and then
it behaves as range function:


import string


assert = custom_range(string.ascii_lowercase, 'g') ==
['a', 'b', 'c', 'd', 'e', 'f']
assert = custom_range(string.ascii_lowercase, 'g', 'p') ==
['g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o']
assert = custom_range(string.ascii_lowercase, 'p', 'g', -2) ==
['p', 'n', 'l', 'j', 'h']

"""


from typing import Any, Iterable


def string_range(iterable: str, start=None, stop=None, step=None):
    if step is None:
        step = 1
    if step < 0:
        iterable = iterable[::-1]
        step = -step
    if start is None:
        start = 0
    else:
        start = iterable.find(start)
    if stop is None:
        stop = len(iterable)
    else:
        stop = iterable.find(stop)

    result = []
    while start < stop:
        result.append(iterable[start])
        start += step

    return result


def dict_range(iterable: dict, start=None, stop=None):
    if start is None:
        start = min(iterable.keys())
    if stop is None:
        stop = len(iterable)

    keys = iterable.keys()
    return list(filter(lambda x: x < stop and x >= start, keys))


def list_range(iterable: list, start=None, stop=None, step=None):
    """In theory i should create a decorator, but i'm running out of time"""
    if step is None:
        step = 1
    if step < 0:
        iterable = iterable[:-1]
        step = -step
    if start is None:
        start = 0
    else:
        start = iterable.index(start)
    if stop is None:
        stop = len(iterable)
    else:
        stop = iterable.index(stop)

    result = []
    while start < stop:
        result.append(iterable[start])
        start += step

    return result


def custom_range(iterable: Iterable[Any], start=None, stop=None, step=None):
    if stop is None and step is None:
        stop, start = start, stop

    if isinstance(iterable, list):
        return list_range(iterable, start, stop, step)
    if isinstance(iterable, str):
        return string_range(iterable, start, stop, step)
    if isinstance(iterable, dict):
        if step:
            return None
        return dict_range(iterable, start, stop)
