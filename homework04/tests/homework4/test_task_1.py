import pytest

from homework4.task_1_read_file import read_magic_number


def test_positive_case(temp_file):
    """Testing positive case"""
    temp_file.write_text("2\n1234567890\nbdsksn", encoding='utf-8')
    assert read_magic_number(temp_file)


def test_negative_case(temp_file):
    """Testing negative case"""
    temp_file.write_text("4\n1234567890\nbdsksn", encoding='utf-8')
    assert not read_magic_number(temp_file)


def test_value_error_case(temp_file):
    """Testing raise of ValueError"""
    temp_file.write_text("e r t\n1234567890\nbdsksn", encoding='utf-8')
    with pytest.raises(ValueError):
        read_magic_number(temp_file)


def test_no_file_case():
    """Testing raise of FileNotFoundError"""
    with pytest.raises(FileNotFoundError):
        read_magic_number("non-existing-file.txt")
