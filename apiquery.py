import requests

class APIQuery:
    base_url = ''
    parameters = {'q':''}
    response = None  #response from api, populated by parse_results()
    def __init__(self, base_url, search):
        self.base_url = base_url
        self.parameters['q'] = search

    def get_base_url(self):
        return self.base_url

    def get_parameters(self):
        return self.parameters

    def send_request(self):
        self.response = requests.get(self.get_base_url(), params=self.parameters)
