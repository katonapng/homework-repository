from homework6.counter import User


def test_no_instances_case():
    """Test counter if no instances are created"""
    assert User.get_created_instances() == 0


def test_multiple_instances_case():
    """Test counter if multiple instances are created"""
    user, _, _ = User(), User(), User()
    assert user.get_created_instances() == 3


def test_counter_reset():
    user, _, _ = User(), User(), User()
    user.reset_instances_counter()
    assert user._count == 0
