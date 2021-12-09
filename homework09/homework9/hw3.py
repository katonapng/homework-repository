"""
Write a function that takes directory path, a file extension
and an optional tokenizer.
It will count lines in all files with that extension if there are no tokenizer.
If a the tokenizer is not none, it will count tokens.

For dir with two files from hw1.py:
>>> universal_file_counter(test_dir, "txt")
6
>>> universal_file_counter(test_dir, "txt", str.split)
6

"""
import os
from pathlib import Path
from typing import Callable, Optional


def get_all_files(dir_path, file_extension):
    file_list = []
    for filename in os.listdir(dir_path):
        f = os.path.join(dir_path, filename)
        if os.path.isfile(f) and \
                os.path.basename(f).endswith('.' + file_extension):
            file_list.append(f)

    return file_list


def count_tokens(file_list, tokenizer):
    count_ = 0
    for file in file_list:
        with open(file) as f:
            if tokenizer is None:
                count_ += len([line for line in f])
            else:
                count_ += len([tokenizer(line) for line in f])
    return count_


def universal_file_counter(
    dir_path: Path, file_extension: str, tokenizer: Optional[Callable] = None
) -> int:
    file_list = get_all_files(dir_path, file_extension)
    return count_tokens(file_list, tokenizer)
