import pytest


@pytest.fixture(scope="session")
def make_dir(tmpdir_factory):
    temp_dir = tmpdir_factory.mktemp("temp_dir")
    file1 = temp_dir.join("file1.txt")
    file1.write_text("1\n3\n5", encoding="utf-8")
    file2 = temp_dir.join("file2.txt")
    file2.write_text("2\n4\n6", encoding="utf-8")

    temp_dir.join("file3.pptx")
    temp_dir.join("file4.png")
    temp_dir.join("nested_dir")
    return temp_dir
