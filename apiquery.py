import requests

class APIQuery:

    def __init__(self, query):
        self.base_url = ''
        self.parameters = {'q': query}
        self.response_object = None  # response from api, populated by parse_results()
        self.response = None

    def query_api(self):
        self.send_request()

        try:
            self.parse_response()
        except ValueError: #if the response isn't legitimate json
            self.response = self.response_object.text

    def send_request(self):
        self.response_object = requests.get(self.get_base_url(), params=self.parameters)

    def parse_response(self):
        self.response = self.response_object.json()

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

    def get_response(self):
        return self.response
