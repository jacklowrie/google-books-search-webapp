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

def test_googlebooksapiquery_has_right_base_url(new_search):
    assert new_search.base_url == 'https://www.googleapis.com/books/v1/volumes'

def test_can_set_results_fields(new_search):
    assert new_search.parameters == { 'q' : 'some search',
                        'fields' : 'kind,totalItems,items(kind,volumeInfo(title,subtitle,authors,publisher,industryIdentifiers,imageLinks/thumbnail))'
                        }
def test_can_construct_query_uri(new_search):
    assert False
