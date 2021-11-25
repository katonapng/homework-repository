from homework2.hw4 import cache, func


def test_regular1_case():
    """Testing first regular example"""
    cache_func = cache(func)
    some = 100, 200

    val_1 = cache_func(*some)
    val_2 = cache_func(*some)

    assert val_1 is val_2
