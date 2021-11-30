import pytest
from homework6.oop_2 import Student, Teacher


@pytest.fixture(scope="session")
def teacher():
    return Teacher('Din', 'Djarin')


@pytest.fixture(scope="session")
def student():
    return Student('Baby', 'Yoda')
