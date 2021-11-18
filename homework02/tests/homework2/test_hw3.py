from homework2.hw3 import combinations


def test_regular1_case():
    """Testing first regular example"""
    assert combinations([1, 2], [3, 4]) == [[1, 3], [1, 4], [2, 3], [2, 4], ]


def test_regular2_case():
    """Testing second regular example"""
    assert combinations([1, 2], [3]) == [[1, 3], [2, 3], ]


def test_same_elements_case():
    """Testing lists with the same elements"""
    assert combinations([2, 2], [2, 2]) == [[2, 2], [2, 2], [2, 2], [2, 2], ]


def test_empty_case():
    """Testing empty example"""
    assert combinations([], []) == []
