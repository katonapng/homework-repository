def test_access_as_dict(database):
    """Test dict access"""
    assert database['Yeltsin'] == [999, 'Russia']


def test_len(database):
    """Test len function"""
    assert len(database) == 3


def test_iterations(database):
    """Test iter function"""
    pr = []
    for president in database:
        pr.append(president)

    assert pr == ['Big Man Tyrone', 'Trump', 'Yeltsin']


def test_in(database):
    """Test in function"""
    assert 'Yeltsin' in database


def test_updated_database(database, update_delete_database):
    assert 'GreatDude' in database
