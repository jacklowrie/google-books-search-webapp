import pytest
import requests
import requests_mock
import json

from apiquery import APIQuery

@pytest.fixture()
def basic_apiquery():
    pytest.test_url = 'https://www.example.com/'
    pytest.test_query = 'some query'
    new_apiquery = APIQuery(pytest.test_query)
    new_apiquery.set_base_url(pytest.test_url)
    yield new_apiquery
    del new_apiquery, pytest.test_url, pytest.test_query

class TestCreateAPIQueryObjects(object):

    def test_can_set_apiquery_base_url(self, basic_apiquery):
        assert basic_apiquery.base_url == pytest.test_url

    def test_can_create_apiquery_with_params(self, basic_apiquery):
        assert basic_apiquery.parameters['q'] == pytest.test_query

    def test_can_get_base_url(self, basic_apiquery):
        assert basic_apiquery.get_base_url() == pytest.test_url

    def test_can_get_parameters(self, basic_apiquery):
        assert basic_apiquery.get_parameters() == {'q': pytest.test_query}

    def test_can_construct_query_uri(self, requests_mock, basic_apiquery):
        requests_mock.get('https://www.example.com/?some+query', text='some response')
        basic_apiquery.send_request()

        assert basic_apiquery.response.text == 'some response'

    def test_can_parse_results(self, requests_mock, basic_apiquery):
        json_string = '{ "name":"John", "age":30, "city":"New York"}'

        requests_mock.get('https://www.example.com/?some+query', text=json_string)
        basic_apiquery.send_request()
        basic_apiquery.parse_results()
        assert basic_apiquery.results == json.loads(json_string)
