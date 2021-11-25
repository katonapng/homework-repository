from homework5.save_original_info import custom_sum


def test_doc():
    """Testing if func doc is correct"""
    custom_sum(1, 2, 3, 4)
    assert custom_sum.__doc__ == 'This function can sum any \
objects which have __add___'


def test_name():
    """Testing if func name is correct"""
    custom_sum(1, 2, 3, 4)
    assert custom_sum.__name__ == 'custom_sum'


def test_class_attribute():
    """Testing creation of class attribute"""
    custom_sum(1, 2, 3, 4)
    assert custom_sum.__original_func
