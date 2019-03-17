import pytest
import requests
import requests_mock
import json

from apiquery import APIQuery

@pytest.fixture
def apiquery_object():
    pytest.test_url = 'https://www.example.com/'
    pytest.test_query = 'some query'
    apiquery = APIQuery(pytest.test_query)
    apiquery.set_base_url(pytest.test_url)
    yield apiquery
    del apiquery, pytest.test_url, pytest.test_query

class TestAPIQueryUtilities(object):

    def test_can_set_apiquery_base_url(self, apiquery_object):
        assert apiquery_object.base_url == pytest.test_url

    def test_can_create_apiquery_with_params(self, apiquery_object):
        assert apiquery_object.parameters['q'] == pytest.test_query

    def test_can_get_base_url(self, apiquery_object):
        assert apiquery_object.get_base_url() == pytest.test_url

    def test_can_get_parameters(self, apiquery_object):
        assert apiquery_object.get_parameters() == {'q': pytest.test_query}

    def test_can_get_parameter(self, apiquery_object):
        assert apiquery_object.get_parameter('q') == pytest.test_query

    def test_can_add_parameters(self, apiquery_object):
        new_param= 'field'
        new_value = 'something in the field'
        apiquery_object.add_parameter(new_param, new_value)
        assert apiquery_object.get_parameter(new_param) == new_value


class TestSendAPIQueries(object):

    def test_can_send_api_request(self, requests_mock, apiquery_object):
        requests_mock.get('https://www.example.com/?some+query', text='some response')
        apiquery_object.send_request()

        assert apiquery_object.response_object.text == 'some response'

    def test_can_parse_response(self, requests_mock, apiquery_object):
        json_string = '{ "name":"John", "age":30, "city":"New York"}'
        requests_mock.get('https://www.example.com/?some+query', text=json_string)
        apiquery_object.send_request()
        apiquery_object.parse_response()

        assert apiquery_object.response == json.loads(json_string)

    def test_can_query_api(self, requests_mock, apiquery_object):
        json_string = '{ "name":"John", "age":30, "city":"New York"}'
        requests_mock.get('https://www.example.com/?some+query', text=json_string)
        apiquery_object.query_api()

        assert apiquery_object.response == json.loads(json_string)

    def test_can_handle_nonjson_response(self, requests_mock, apiquery_object):
        requests_mock.get('https://www.example.com/?some+query', text = 'ok')
        apiquery_object.query_api()
        assert apiquery_object.get_response() == 'ok'
