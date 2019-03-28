import pytest
import requests
import requests_mock
import json

from goodreadsapiquery import GoodreadsAPIQuery

@pytest.fixture
def goodreads_query():
    query = GoodreadsAPIQuery('0123456789')
    yield query
    del query

def test_googlebooksapiquery_has_right_base_url(goodreads_query):
    assert goodreads_query.base_url == 'https://www.goodreads.com/book/isbn_to_id'

def test_can_set_results_fields(goodreads_query):
    assert goodreads_query.get_parameters() == { 'key' : 'Hc3p3luBbcApaSFOTIgadQ'}

def test_can_add_isbn(goodreads_query):
    assert goodreads_query.get_query_url() == 'https://www.goodreads.com/book/isbn_to_id/0123456789'

def test_can_make_query_url(requests_mock, goodreads_query):
    requests_mock.get('https://www.goodreads.com/book/isbn_to_id/0123456789',
                      text='14429101'
                      )
    goodreads_query.query_api()
    assert goodreads_query.response_object.url == 'https://www.goodreads.com/book/isbn_to_id/0123456789?key=Hc3p3luBbcApaSFOTIgadQ'
def test_can_query_goodreads_api(requests_mock, goodreads_query):
    requests_mock.get('https://www.goodreads.com/book/isbn_to_id/0123456789',
                      text='ok'
                      )
    goodreads_query.query_api()
    assert goodreads_query.get_response() == 'ok'

def test_can_get_results(requests_mock, goodreads_query):
    requests_mock.get('https://www.goodreads.com/book/isbn_to_id/0123456789',
                      text='14429101'
                      )
    goodreads_query.query_api()
    assert goodreads_query.get_results() == 'https://www.goodreads.com/book/show/14429101'
