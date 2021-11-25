from homework3.task1 import f, g


def test_regular_case(monkeypatch):
    """Testing that cache works"""
    monkeypatch.setattr('builtins.input', lambda _: "1")
    first_call = f()
    second_call = f()
    assert first_call is second_call


def test_regular2_case(monkeypatch):
    """Testing that cache works for set amount of calls"""
    monkeypatch.setattr('builtins.input', lambda _: "1")
    first_call = f()
    f()
    third_call = f()
    assert first_call is third_call


def test_regular3_case(monkeypatch):
    """Testing that cache stops after set amount of calls"""
    first_call = g(1)
    g(1)
    g(1)
    fourth_call = g(1)
    assert first_call is not fourth_call
