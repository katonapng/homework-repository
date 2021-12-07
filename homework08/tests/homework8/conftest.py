import sqlite3

import pytest

from homework8.task2 import TableData


@pytest.fixture(scope="session")
def temp_file(tmpdir_factory):
    return tmpdir_factory.mktemp("data").join("temp.txt")


@pytest.fixture(scope="function")
def database():
    return TableData('homework8/example.sqlite', 'presidents')


@pytest.fixture(scope="session")
def database_connection(database_name='homework8/example.sqlite'):
    conn = sqlite3.connect(database_name)
    cursor = conn.cursor()
    return conn, cursor
