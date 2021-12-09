"""
Given a dictionary (tree), that can contains multiple nested structures.
Write a function, that takes element and finds the number of occurrences
of this element in the tree.

Tree can only contains basic structures like:
    str, list, tuple, dict, set, int, bool
"""
from itertools import count
from typing import Any


def decorator(count_):
    def occurrences_counter(key, item, element):
        if element == key:
            next(count_)
        if element == item:
            next(count_)
        if isinstance(item, dict):
            for val in item.values():
                occurrences_counter(key, val, element)
        if isinstance(item, list) or isinstance(item, tuple) \
                or isinstance(item, set):
            for val in item:
                occurrences_counter(key, val, element)
    return occurrences_counter


def find_occurrences(tree: dict, element: Any) -> int:
    count_ = count()
    decorated_occurences = decorator(count_)
    for key, item in tree.items():
        decorated_occurences(key, item, element)
    return next(count_)
