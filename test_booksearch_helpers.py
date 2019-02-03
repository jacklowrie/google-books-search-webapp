import pytest
from unittest.mock import Mock, patch

from booksearch import BookSearch

search_phrase = 'this is a test search'
json = { 'kind': 'books#volumes',
                    'totalItems': 1,
                    'items': [{ 'kind': 'books#volume',
                                'volumeInfo': { 'title': 'Reckoning',
                                                'subtitle': 'The Quarter Boys',
                                                'authors': ['David Lennon'],
                                                'publisher': 'Createspace Indie Pub Platform',
                                                'industryIdentifiers': [{   'type': 'ISBN_10',
                                                                            'identifier': '1475009216'
                                                                        },
                                                                        {  'type': 'ISBN_13',
                                                                            'identifier': '9781475009217'
                                                                        }],
                                                'imageLinks': {'thumbnail': 'http://books.google.com/books/content?id=Osn8ugAACAAJ&printsec=frontcover&img=1&zoom=1&source=gbs_api'}
                                                }
                            }]
}

# many_results = 'harry potter sorcerer\'s stone' #test search many results
# quarter_boys = 'intitle:reckoning+inauthor:david+inauthor:lennon' #test search one result
# no_results = '3ugn398' #test search returns no results
# multiple_authors = 'introduction to algorithms inauthor:Thomas inauthor:H inauthor:Cormen inauthor:Thomas inauthor:H inauthor:Cormen inauthor:Charles inauthor:E inauthor:Leiserson'


@pytest.fixture()
def new_search():
    new_search = BookSearch(search_phrase)
    yield new_search
    del new_search

@pytest.fixture()
def successful_search():
    successful_search = BookSearch('intitle:reckoning+inauthor:david+inauthor:lennon')
    successful_search.construct_request()
    successful_search.results = json
    yield successful_search
    del successful_search

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

@patch('booksearch.requests.get') # this test may not be necessary (testing requests module built-in function)
def test_can_parse_results(mock_get, new_search):
    mock_get.return_value.ok = True

    def mock_return():
        return json

    new_search.construct_request()
    new_search.send_request()

    mock_get.setattr(json, mock_return)
    new_search.parse_results()
    assert True

# Test get_search_results() and helpers
def test_can_get_result_title(successful_search):
    assert successful_search.get_result_title(0) == 'title: Reckoning: The Quarter Boys'

def test_can_get_result_authors(successful_search):
    assert successful_search.get_result_authors(0) == 'authors: David Lennon'

def test_can_get_result_publisher(successful_search):
    assert successful_search.get_result_publisher(0) == 'publisher: Createspace Indie Pub Platform'

def test_can_get_thumbnail_url(successful_search):
    assert successful_search.get_thumbnail_url(0) == 'http://books.google.com/books/content?id=Osn8ugAACAAJ&printsec=frontcover&img=1&zoom=1&source=gbs_api'

def test_can_get_result_isbn(successful_search):
    assert successful_search.get_result_isbn(0) == '9781475009217'

@patch('booksearch.requests.get')
def test_can_get_goodreads_id(mock_get, successful_search):
    mock_get.return_value.text = '14429101'
    assert successful_search.get_goodreads_id(0) == '14429101'

@patch('booksearch.requests.get')
def test_can_make_goodreads_url(mock_get, successful_search):
    mock_get.return_value.text = '14429101'
    assert successful_search.make_goodreads_url(0) == 'https://www.goodreads.com/book/show/14429101'

@patch('booksearch.requests.get')
def test_can_get_search_results(mock_get, successful_search):
    mock_get.return_value.text = '14429101'
    real_result = [{'title': 'title: Reckoning: The Quarter Boys',
                    'authors': 'authors: David Lennon',
                    'publisher': 'publisher: Createspace Indie Pub Platform',
                    'thumbnail': 'http://books.google.com/books/content?id=Osn8ugAACAAJ&printsec=frontcover&img=1&zoom=1&source=gbs_api',
                    'goodreads': 'https://www.goodreads.com/book/show/14429101'
    }]
    assert successful_search.get_search_results() == real_result

def test_can_get_results_count(successful_search):
    assert successful_search.get_results_count() == 1
