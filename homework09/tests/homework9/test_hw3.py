from homework9.hw3 import universal_file_counter


def test_no_token_case(make_dir):
    """Test count without token"""
    assert universal_file_counter(make_dir, 'txt') == 6


def test_token_case(make_dir):
    """Test count with token"""
    assert universal_file_counter(make_dir, 'txt', str.split) == 6
