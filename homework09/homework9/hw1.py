"""
Write a function that merges integer from sorted files and returns an iterator
file1.txt:
1
3
5
file2.txt:
2
4
6
>>> list(merge_sorted_files(["file1.txt", "file2.txt"]))
[1, 2, 3, 4, 5, 6]
"""
from pathlib import Path
from typing import Iterator, List, Union


def file_iterator(file):
    with open(file, 'r') as f:
        for line in f:
            yield int(line) if line.strip().isdigit() else None


def iterator(iterators):
    while True:
        for iter in iterators:
            try:
                yield next(iter)
            except StopIteration:
                return


def merge_sorted_files(file_list: List[Union[Path, str]]) -> Iterator:
    if not file_list:
        return []
    iterators = []
    for file in file_list:
        iterators.append(file_iterator(file))

    return iterator(iterators)
