import sqlite3

import pytest

from homework8.task2 import TableData


@pytest.fixture(scope="function")
def update_delete_database(database_name='homework8/example.sqlite',
                           table_name='presidents'):
    conn = sqlite3.connect(database_name)
    cursor = conn.cursor()
    cursor.execute(f"INSERT OR REPLACE INTO {table_name} \
        VALUES ('GreatDude', 69, 'FarAway')")
    conn.commit()

    yield

    cursor.execute(f"DELETE FROM {table_name} WHERE name='GreatDude'")
    conn.commit()


@pytest.fixture(scope="session")
def temp_file(tmpdir_factory):
    return tmpdir_factory.mktemp("data").join("temp.txt")


@pytest.fixture(scope="session")
def database():
    return TableData('homework8/example.sqlite', 'presidents')


@pytest.fixture(scope="function")
def database_connection(database_name='homework8/example.sqlite'):
    conn = sqlite3.connect(database_name)
    cursor = conn.cursor()

    return conn, cursor
