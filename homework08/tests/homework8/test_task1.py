import pytest

from homework8.task1 import KeyValueStorage


def test_access_as_dict(temp_file):
    """Test dict access"""
    temp_file.write_text("name=kek\nlast_name=top\n\
        power=9001\nsong=shadilay\n__name__=new_name", encoding='utf-8')
    storage = KeyValueStorage(temp_file)
    assert storage['name'] == 'kek'


def test_access_as_property(temp_file):
    """Test property access"""
    temp_file.write_text("name=kek\nlast_name=top\n\
    power=9001\nsong=shadilay\n__name__=new_name", encoding='utf-8')
    storage = KeyValueStorage(temp_file)
    assert storage.name == 'kek'


def test_ValueError(temp_file):
    """Test raise of ValueError"""
    temp_file.write_text("name=kek\nlast_name=top\n\
        power=9001\nsong=shadilay\n1=blablabla", encoding='utf-8')
    with pytest.raises(ValueError):
        KeyValueStorage(temp_file)
