import pytest
import requests_mock

from booksearchapp import BookSearchApp


def test_can_make_booksearchapp():
    test = BookSearchApp('test')
    assert isinstance(test, BookSearchApp)
