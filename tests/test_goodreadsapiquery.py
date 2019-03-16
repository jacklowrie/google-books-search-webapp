import pytest
import requests
import requests_mock
import json

from goodreadsapiquery import GoodreadsAPIQuery

@pytest.fixture
def goodreads_query():
    query = GoodreadsAPIQuery('some search')
    yield query
    del query

def test_googlebooksapiquery_has_right_base_url(goodreads_query):
    assert goodreads_query.base_url == 'https://www.goodreads.com/book/isbn_to_id'

def test_can_set_results_fields(goodreads_query):
    assert goodreads_query.get_parameters() == { 'q' : 'some search',
                                            'key' : 'Hc3p3luBbcApaSFOTIgadQ'}
