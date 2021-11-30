"""
Given a file containing text. Complete using only default collections:
    1) Find 10 longest words consisting from largest amount of unique symbols
    2) Find rarest symbol for document
    3) Count every punctuation char
    4) Count every non ascii char
    5) Find most common non ascii char for document
"""

import string
from collections import Counter, defaultdict
from itertools import product
from typing import List


def flatten(lines):
    return [item for sublist in lines for item in sublist]


def read_chunks(file_path, size=1024):
    for chunk in iter(lambda: file_path.read(size), b""):
        if not chunk:
            break
        yield chunk


def get_longest_diverse_words(file_path: str) -> List[str]:
    words = []
    with open(file_path) as f:
        for chunk in read_chunks(f):
            words.append(chunk.split())
    words = flatten(words)
    words = sorted(words, key=lambda sub: len(list(set(sub))), reverse=True)
    return words[:10]


def get_rarest_char(file_path: str) -> str:
    hash_map = defaultdict(str)
    with open(file_path) as f:
        for line in f:
            for char in line:
                if char in hash_map:
                    hash_map[char] += 1
                else:
                    hash_map[char] = 1
    return min(hash_map, key=hash_map.get)


def count_punctuation_chars(file_path: str) -> int:
    char_counter = 0
    punctuation = list(string.punctuation)
    with open(file_path) as f:
        for chunk, symbol in product(read_chunks(f), punctuation):
            char_counter += Counter(chunk)[symbol]
    return char_counter


def count_non_ascii_chars(file_path: str) -> int:
    counter = 0
    with open(file_path) as f:
        for chunk in read_chunks(f):
            encoded_chunk = chunk.encode("ascii", "ignore")
            decoded_chunk = encoded_chunk.decode()
            counter += len(encoded_chunk) - len(decoded_chunk)
    return counter


def get_most_common_non_ascii_char(file_path: str) -> str:
    hash_map = defaultdict(int)
    with open(file_path) as f:
        for line in f:
            for char in line:
                if not char.isascii() and char in hash_map:
                    hash_map[char] += 1
                elif not char.isascii():
                    hash_map[char] = 1
    return max(hash_map, key=hash_map.get)
