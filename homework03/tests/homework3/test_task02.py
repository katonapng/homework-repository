from homework3.task02 import run_slow_calculate


def test_positive_case():
    """Testing that calculations don't take more than a minute to calculate"""
    calls = 1
    """1 cuz i dont want CI to calculate this for an hour,
    localy i ran 50 and it's fine"""
    call_times = []
    for i in range(calls):
        call_times.append(run_slow_calculate())
        if call_times[i] > 60:
            assert False

    assert True
