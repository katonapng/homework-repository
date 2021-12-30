from homework3.task04 import is_armstrong


def test_positive_case():
    """Testing armstrong number gives true"""
    assert is_armstrong(153) is True


def test_positive2_case():
    """Testing another armstrong number gives true"""
    assert is_armstrong(370) is True


def test_negative_case():
    """Testing not armstrong number gives false"""
    assert is_armstrong(10) is False
