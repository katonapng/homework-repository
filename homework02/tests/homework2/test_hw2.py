from homework2.hw2 import major_and_minor_elem


def test_regular1_case():
    """Testing first regular example"""
    assert major_and_minor_elem([3, 2, 3]) == (3, 2)


def test_regular2_case():
    """Testing second regular example"""
    assert major_and_minor_elem([2, 2, 1, 1, 1, 2, 2]) == (2, 1)


def test_regular3_case():
    """Testing third regular example"""
    assert major_and_minor_elem([1, 1, 2, 2, 2, 1, 1]) == (1, 2)


def test_empty_case():
    """Testing empty example"""
    assert major_and_minor_elem([]) == (None, None)


def test_major_equals_minor_case():
    """Testing major equals minor example"""
    assert major_and_minor_elem([1, 1, 1]) == (1, 1)
