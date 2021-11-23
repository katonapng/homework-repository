import pytest
from homework4.task_2_mock_input import count_dots_on_i
from httpretty import HTTPretty, httprettified


@httprettified
def test_positive_case():
    """Testing positive case """
    HTTPretty.register_uri(HTTPretty.GET,  "https://my_example.com/",
                           body="i apologize for anything i might have done. \
                                i was not myself. said Rhy. \
                                i apologize for shooting you in the leg. \
                                said Lila. i was myself entirely.")

    assert count_dots_on_i("https://my_example.com/") == 15


def test_no_url_case():
    """Testing raise of ValueError"""
    with pytest.raises(ValueError):
        count_dots_on_i("https://non-existing-url-for-sure.com/")
