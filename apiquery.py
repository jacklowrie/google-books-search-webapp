import requests

class APIQuery:
    base_url = ''
    parameters = {'q':''}
    response = None  #response from api, populated by parse_results()
    results = None
    def __init__(self, query):
        self.parameters['q'] = query

    def set_base_url(self, url):
        self.base_url = url

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
