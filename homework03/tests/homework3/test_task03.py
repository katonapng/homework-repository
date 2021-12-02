from homework3.task03 import Filter, make_filter


def test_Filter_init():
    """Testing Filter __init__"""
    assert Filter(lambda a: a % 2 == 0,
                  lambda a: a > 0,
                  lambda a: isinstance(a, int))


def test_make_filter_func():
    """Testing make_filter_func"""
    sample_data = [
        {
            "name": "Bill",
            "last_name": "Gilbert",
            "occupation": "was here",
            "type": "person",
        },
        {
            "is_dead": True,
            "kind": "parrot",
            "type": "bird",
            "name": "polly"
        }
    ]
    assert make_filter(name='polly', type='bird').apply(sample_data) == [
        {'is_dead': True, 'kind': 'parrot', 'type': 'bird', 'name': 'polly'}
        ]


def test_Filter_apply():
    """Testing Filter apply"""
    positive_even = Filter(lambda a: a % 2 == 0,
                           lambda a: a > 0,
                           lambda a: isinstance(a, int))
    assert positive_even.apply(range(100)) == [2, 4, 6, 8, 10, 12, 14, 16,
                                               18, 20, 22, 24, 26, 28, 30,
                                               32, 34, 36, 38, 40, 42, 44,
                                               46, 48, 50, 52, 54, 56, 58,
                                               60, 62, 64, 66, 68, 70, 72,
                                               74, 76, 78, 80, 82, 84, 86,
                                               88, 90, 92, 94, 96, 98]
