import pytest
from unittest.mock import MagicMock
from booksearch import BookSearch



def test_can_make_empty_booksearch():
    new_search = BookSearch()
    assert isinstance(new_search, BookSearch)

def test_can_assign_search_attribute():
    search_phrase = 'this is a test search'
    new_search = BookSearch(search_phrase)
    assert new_search.search == search_phrase
