import requests

class APIQuery:
    base_url = ''
    parameters = {'q':''}
    response = None  # response from api, populated by parse_results()
    results = None
    def __init__(self, query):
        self.parameters['q'] = query

    def query_api(self):
        self.send_request()

        try:
            self.parse_results()
        except ValueError: #if the response isn't legitimate json
            self.results = self.response.text

    def send_request(self):
        self.response = requests.get(self.get_base_url(), params=self.parameters)

    def parse_results(self):
        self.results = self.response.json()

    def add_parameter(self, param, value):
        self.parameters[param] = value

# Setters and Getters

    def set_base_url(self, url):
        self.base_url = url

    def get_base_url(self):
        return self.base_url

    def get_parameter(self, param):
        return self.parameters[param]

    def get_parameters(self):
        return self.parameters

    def get_results(self):
        return self.results
