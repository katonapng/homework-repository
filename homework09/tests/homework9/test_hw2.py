import pytest

from homework9.hw2 import Suppressor, suppressor


def test_generator_suppressor():
    """Test generator suppressor"""
    with suppressor(IndexError):
        assert [][2]


def test_class_suppressor():
    """Test generator suppressor"""
    with Suppressor(IndexError):
        assert [][2]


def test_wrong_error_generator_suppressor():
    """Test generator suppressor doesnt suppress when
    wrong error is passed"""
    with suppressor(ValueError):
        with pytest.raises(IndexError):
            [][2]


def test_wrong_error_class_suppressor():
    """Test class suppressor doesnt suppress when
    wrong error is passed"""
    with Suppressor(ValueError):
        with pytest.raises(IndexError):
            [][2]
