import requests

class APIQuery:
    base_url = ''
    parameters = []

    def __init__(self, base_url):
        self.base_url = base_url
