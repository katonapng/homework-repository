import pytest

from homework5.oop_1 import Student, Teacher


@pytest.fixture(scope="session")
def teacher():
    return Teacher('Din', 'Djarin')


@pytest.fixture(scope="session")
def student():
    return Student('Baby', 'Yoda')
