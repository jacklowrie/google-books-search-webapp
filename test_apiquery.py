import pytest
from unittest.mock import Mock, patch

from apiquery import APIQuery

# test can set base base_url
def test_can_create_apiquery_with_base_url():
    test_url = 'https://www.example.com/'
    new_apiquery = APIQuery(test_url, '')
    assert new_apiquery.base_url == test_url

def test_can_create_apiquery_with_params():
    test_url = 'https://www.example.com/'
    test_query = 'some query'
    new_apiquery = APIQuery(test_url, test_query)

    assert new_apiquery.parameters['q'] == test_query

def test_can_get_base_url():
    test_url = 'https://www.example.com/'
    test_query = 'some query'
    new_apiquery = APIQuery(test_url, test_query)

    assert new_apiquery.get_base_url() == test_url

def test_can_get_parameters():
    test_url = 'https://www.example.com/'
    test_query = 'some query'
    new_apiquery = APIQuery(test_url, test_query)

    assert new_apiquery.get_parameters() == {'q': test_query}

def test_can_send_request():
    assert False
