from homework7.hw1 import find_occurrences

# Example tree:
example_tree = {
    "first": ["RED", "BLUE"],
    "second": {
        "simple_key": ["simple", "list", "of", "RED", "valued"],
    },
    "third": {
        "abc": "BLUE",
        "jhl": "RED",
        "complex_key": {
            "key1": "value1",
            "key2": "RED",
            "key3": ["a", "lot", "of", "values", {"nested_key": "RED"}],
        }
     },
    "fourth": "RED",
    "fifth": ("RED", "GREEN", set(["RED", "GREEN", "BLUE"])),
    "sixth": set(["RED", "GREEN", ("BLUE", "RED")]),
    "RED": True
}


def test_list():
    """Test searching in nested lists"""
    assert find_occurrences({"first": ["RED", "BLUE"],
                             "second": ["BLUE", ["RED",
                                                 ["GREEN", "BLUE"],
                                                 "ORANGE"]]}, "RED") == 2


def test_dict():
    """Test searching in nested dicts"""
    assert find_occurrences({"first": {
        "abc": "BLUE",
        "jhl": "RED",
        "complex_key": {
            "key1": "value1",
            "key2": "RED",
            "key3": {"nested_key": "RED"},
        }
     }}, "RED") == 3


def test_set():
    """Test searching in set"""
    assert find_occurrences({"first": set(["RED", "BLUE"])}, "RED") == 1


def test_tuple():
    """Test searching in nested tuples"""
    assert find_occurrences({"first": ("RED", "BLUE"),
                             "second": ("BLUE",
                                        ("RED", ("GREEN", "BLUE"), "ORANGE"))},
                            "RED") == 2


def test_all_structures():
    """Test searching in nested tree"""
    assert find_occurrences(example_tree, "RED") == 11
