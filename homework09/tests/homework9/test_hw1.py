from homework9.hw1 import merge_sorted_files


def test_two_files_case(tmpdir):
    """Test merge two files"""
    temp_file1 = tmpdir.join("temp1.txt")
    temp_file2 = tmpdir.join("temp2.txt")
    temp_file1.write("1\n3\n5\n")
    temp_file2.write("2\n4\n6\n")

    assert list(merge_sorted_files([temp_file1, temp_file2])) == [
        1, 2, 3, 4, 5, 6
        ]


def test_one_file_case(tmpdir):
    """Test merge one file"""
    temp_file1 = tmpdir.join("temp1.txt")
    temp_file1.write("1\n3\n5\n")

    assert list(merge_sorted_files([temp_file1])) == [1, 3, 5]


def test_no_files_case():
    """Test merge zero files"""
    assert list(merge_sorted_files([])) == []
