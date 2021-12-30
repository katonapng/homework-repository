from homework7.hw2 import backspace_compare


def test_positive_lowercase():
    """Test equal lowercase strings"""
    assert backspace_compare("ab#c", "ad#c") is True


def test_lonely_hashtag():
    """Test equal lowercase strings"""
    assert backspace_compare("#a#c", "a##c") is True


def test_positive_uppercase():
    """Test equal lowercase strings"""
    assert backspace_compare("#A#C", "A##C") is True


def test_positive_random_ascii():
    """Test equal lowercase strings"""
    assert backspace_compare("#2#!", "2##!") is True


def test_negative_case():
    """Test equal lowercase strings"""
    assert backspace_compare("a#c", "b") is False
