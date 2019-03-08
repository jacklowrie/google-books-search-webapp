import requests

class APIQuery:
    base_url = ''
    parameters = {'q':''}

    def __init__(self, base_url, search):
        self.base_url = base_url
        self.parameters['q'] = search

    def get_base_url(self):
        return self.base_url

    def get_parameters(self):
        return self.parameters
