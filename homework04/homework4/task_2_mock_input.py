"""
Write a function that accepts an URL as input
and count how many letters `i` are present in the HTML by this URL.

Write a test that check that your function works.
Test should use Mock instead of real network interactions.

You can use urlopen* or any other network libraries.
In case of any network error raise ValueError("Unreachable {url}).

Definition of done:
 - function is created
 - function is properly formatted
 - function has positive and negative tests
 - test could be run without internet connection

You will learn:
 - how to test using mocks
 - how to write complex mocks
 - how to raise an exception form mocks
 - do a simple network requests


>>> count_dots_on_i("https://example.com/")
59

* https://docs.python.org/3/library/urllib.request.html#urllib.request.urlopen
"""
import urllib
from collections import Counter

from bs4 import BeautifulSoup


def count_dots_on_i(url: str) -> int:
    try:
        sock = urllib.request.urlopen(url)
    except urllib.error.URLError:
        raise ValueError(f'Unreachable {url}')
    except urllib.error.HTTPError:
        raise ValueError(f'Unreachable {url}')

    html_page = sock.read().decode('utf-8')
    sock.close()

    soup = BeautifulSoup(html_page, "html.parser")

    return Counter(str(soup))['i']
