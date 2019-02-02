import pytest
from unittest.mock import Mock, patch

from booksearch import BookSearch

search_phrase = 'this is a test search'

@pytest.fixture()
def new_search():
    new_search = BookSearch(search_phrase)
    yield new_search
    del new_search


# test __init__
def test_can_make_empty_booksearch():
    new_search = BookSearch()
    assert isinstance(new_search, BookSearch)

def test_can_assign_search_attribute(new_search):
    assert new_search.search == search_phrase

# Test make_a_search() and helpers
def test_can_construct_request(new_search):
    new_search.construct_request()
    assert new_search.parameters['q'] == search_phrase

@patch('booksearch.requests.get')
def test_can_send_request(mock_get, new_search):
    mock_get.return_value.ok = True

    new_search.construct_request()
    new_search.send_request()

    assert new_search.search != 'search phrase'

def test_can_parse_results():
    pass #maybe not necessary (testing requests' built-in json() function)

# Test get_search_results() and helpers
