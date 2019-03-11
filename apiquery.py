import requests

class APIQuery:
    base_url = ''
    parameters = {'q':''}
    response = None  #response from api, populated by parse_results()
    results = None
    def __init__(self, base_url, search):
        self.base_url = base_url
        self.parameters['q'] = search

    def get_base_url(self):
        return self.base_url

    def get_parameters(self):
        return self.parameters

    def send_request(self):
        self.response = requests.get(self.get_base_url(), params=self.parameters)

    def parse_results(self):
        self.results = self.response.json()

    def get_results(self):
        return results
