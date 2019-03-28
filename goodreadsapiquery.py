import requests
from apiquery import APIQuery

class GoodreadsAPIQuery(APIQuery):

    def __init__(self, query):
        APIQuery.__init__(self, query)
        self.set_base_url('https://www.goodreads.com/book/isbn_to_id')
        self.add_parameter('key', 'Hc3p3luBbcApaSFOTIgadQ')
        self.parameters.pop('q', None)

        self.query_url = self.get_base_url()
        self.add_isbn(query)

        self.goodreads_book_url = 'https://www.goodreads.com/book/show/'

    def send_request(self):
        self.response_object = requests.get(self.get_query_url(), params=self.parameters)

    def get_results(self):
        url = self.goodreads_book_url + str(self.get_response())
        return url

    def add_isbn(self, isbn):
        self.query_url += '/' + str(isbn)

    def get_query_url(self):
        return self.query_url
