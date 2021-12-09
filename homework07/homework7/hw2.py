"""
Given two strings. Return if they are equal when both are typed into
empty text editors. # means a backspace character.

Note that after backspacing an empty text, the text will continue empty.

Examples:
    Input: s = "ab#c", t = "ad#c"
    Output: True
    # Both s and t become "ac".

    Input: s = "a##c", t = "#a#c"
    Output: True
    Explanation: Both s and t become "c".

    Input: a = "a#c", t = "b"
    Output: False
    Explanation: s becomes "c" while t becomes "b".

"""
import re


def backspace_compare(first: str, second: str):
    first_backspace = re.findall(r'[\x00-\x7F]#', first)
    second_backspace = re.findall(r'[\x00-\x7F]#', second)
    for first_item, second_item in zip(first_backspace, second_backspace):
        first = first.replace(first_item, '')
        second = second.replace(second_item, '')
    return first == second
