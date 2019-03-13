import pytest
import requests
import requests_mock
import json

from googlebooksapiquery import GoogleBooksAPIQuery

@pytest.fixture()
def new_search():
    new_search = GoogleBooksAPIQuery('some search')
    yield new_search
    del new_search

class TestGoogleBooksAPIQueryInheritance(object):
    def test_googlebooksapiquery_has_right_base_url(self, new_search):
        assert new_search.base_url == 'https://www.googleapis.com/books/v1/volumes'

    def test_can_set_results_fields(self, new_search):
        assert new_search.parameters == { 'q' : 'some search',
                            'fields' : 'kind,totalItems,items(kind,volumeInfo(title,subtitle,authors,publisher,industryIdentifiers,imageLinks/thumbnail))'
                            }

    def test_can_send_google_books_api_request(self, requests_mock, new_search):
        requests_mock.get('https://www.googleapis.com/books/v1/volumes',
                          text='ok'
                          )
        new_search.send_request()
        assert new_search.response.text == 'ok'

    def test_can_parse_results(self, requests_mock, new_search):
        json_string = '{ "name":"John", "age":30, "city":"New York"}'
        requests_mock.get('https://www.googleapis.com/books/v1/volumes',
                          text=json_string
                          )
        new_search.send_request()
        new_search.parse_results()
        assert new_search.results == json.loads(json_string)


@pytest.fixture()
def single_result(requests_mock):
    search = GoogleBooksAPIQuery('intitle:reckoning inauthor:david inauthor:lennon')
    requests_mock.get('https://www.googleapis.com/books/v1/volumes',
                      text=test_results
                      )
    search.send_request()
    search.parse_results()
    yield search
    del search

test_results = json.dumps({ 'kind': 'books#volumes',
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
})
class TestGoogleBooksAPIQueryMethods(object):
    def test_get_results_count(self, single_result):
        assert single_result.get_results_count() == 1

    def test_get_result_title(self, single_result_gb_search):
        assert False
