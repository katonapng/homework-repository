import string

from homework2.hw5 import custom_range


def test_string_start_stop_case():
    """Testing example with start and stop"""
    assert custom_range(string.ascii_lowercase, 'g', 'p') == [
        'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o'
        ]


def test_string_stop_case():
    """Testing example with only stop"""
    assert custom_range(string.ascii_lowercase, 'g') == [
        'a', 'b', 'c', 'd', 'e', 'f'
        ]


def test_string_start_stop_step_case():
    """Testing example with start, step and stop"""
    assert custom_range(string.ascii_lowercase, 'p', 'g', -2) == [
        'p', 'n', 'l', 'j', 'h'
        ]


def test_dict_start_stop_case():
    """Testing example with start and stop"""
    assert custom_range({1: 'a', 5: 'rrr', 8: '00', -2: [0]}, -2, 6) == [
        1, 5, -2
        ]


def test_dict_stop_case():
    """Testing example with only stop"""
    assert custom_range({
        (1, 2): 'a', (5, 0): 'rrr', (8, 3): '00', (-2, 1): [0]
        }, (2, 2)) == [(1, 2), (-2, 1)]


def test_list_stop_case():
    """Testing example with only stop"""
    assert custom_range([-2, 5, 6, 0, 5], 6) == [-2, 5]


def test_list_start_stop_case():
    """Testing example with start and stop"""
    assert custom_range([-2, 5, 6, 0, 5], 5, 0) == [5, 6]


def test_list_start_stop_step_case():
    """Testing example with start, step and stop"""
    assert custom_range([-2, 5, 6, 0, 5], -2, 0, 2) == [-2, 6]
