import pytest
import requests
import requests_mock
import json

from googlebooksapiquery import GoogleBooksAPIQuery

@pytest.fixture
def new_search():
    query = GoogleBooksAPIQuery('some search')
    yield query
    del query
    print('teardown new_search')

class TestGoogleBooksAPIQueryInheritance(object):
    def test_googlebooksapiquery_has_right_base_url(self, new_search):
        assert new_search.base_url == 'https://www.googleapis.com/books/v1/volumes'

    def test_can_set_results_fields(self, new_search):
        print(new_search.parameters)
        print(new_search.get_parameters())
        assert new_search.get_parameters() == { 'q' : 'some search', 'fields' : 'kind,totalItems,items(kind,volumeInfo(title,subtitle,authors,publisher,industryIdentifiers,imageLinks/thumbnail))'}

    def test_can_query_googlebooksapi(self, requests_mock, new_search):
        requests_mock.get('https://www.googleapis.com/books/v1/volumes',
                          text='ok'
                          )
        new_search.query_api()
        assert new_search.response.text == 'ok'

    def test_can_parse_results(self, requests_mock, new_search):
        json_string = '{ "name":"John", "age":30, "city":"New York"}'
        requests_mock.get('https://www.googleapis.com/books/v1/volumes',
                          text=json_string
                          )
        new_search.query_api()
        assert new_search.results == json.loads(json_string)


@pytest.fixture()
def single_result(requests_mock):
    search = GoogleBooksAPIQuery('intitle:reckoning inauthor:david inauthor:lennon')
    requests_mock.get('https://www.googleapis.com/books/v1/volumes',
                      text=test_results
                      )
    search.query_api()
    yield search
    del search

#test_results is a reference of the api response for David's book on google books.
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

class TestGoogleBooksAPIQueryUtilities(object):
    def test_get_results_count(self, single_result):
        assert single_result.get_results_count() == 1

    def test_can_get_result_title(self, single_result):
        assert single_result.get_result_title(0) == 'Reckoning: The Quarter Boys'

    def test_can_get_result_authors(self, single_result):
        assert single_result.get_result_authors(0) == 'David Lennon'

    def test_can_get_result_publisher(self, single_result):
        assert single_result.get_result_publisher(0) == 'Createspace Indie Pub Platform'

    def test_can_get_result_thumbnail_url(self, single_result):
        assert single_result.get_result_thumbnail_url(0) == 'http://books.google.com/books/content?id=Osn8ugAACAAJ&printsec=frontcover&img=1&zoom=1&source=gbs_api'

    def test_can_get_result_isbn(self, single_result):
        assert single_result.get_result_isbn(0) == '9781475009217'
