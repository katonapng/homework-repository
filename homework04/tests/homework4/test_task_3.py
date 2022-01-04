from homework4.task_3_get_print_output import my_precious_logger


def test_stdout_case(capsys):
    """Testing stdout"""
    my_precious_logger("OK")
    assert capsys.readouterr().out == "OK"


def test_stderr_case(capsys):
    """Testing stderr"""
    my_precious_logger("error: file not found")
    assert capsys.readouterr().err == "error: file not found"


def test_stdout_empty_case(capsys):
    """Testing empty string in stdout"""
    my_precious_logger("")
    assert capsys.readouterr().out == ""


def test_stderr_empty_case(capsys):
    """Testing error string in stdout"""
    my_precious_logger("error")
    assert capsys.readouterr().err == "error"
