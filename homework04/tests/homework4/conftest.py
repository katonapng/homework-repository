import pytest


@pytest.fixture(scope="session")
def temp_file(tmpdir_factory):
    return tmpdir_factory.mktemp("data").join("temp.txt")
