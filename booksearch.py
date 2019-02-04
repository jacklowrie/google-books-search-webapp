import requests


class BookSearch:

    books_api = 'https://www.googleapis.com/books/v1/volumes'
    parameters = {  'q' : '',
                    'fields' : 'kind,totalItems,items(kind,volumeInfo(title,subtitle,authors,publisher,industryIdentifiers,imageLinks/thumbnail))'
                }
    search = '' #user's search query, populated in __init__
    results = '' #response from google books, populated by parse_results()

    def __init__(self, search=''):
        self.search = search




    def make_a_search(self):
        self.construct_request()
        self.send_request()
        self.parse_results()

    # adds user's search phrase to parameters
    def construct_request(self):
        self.parameters['q'] = self.search

    def send_request(self):
        self.search = requests.get(self.books_api, params=self.parameters)

    #store the results in a python dictionary
    def parse_results(self):
        self.results = self.search.json()




    def get_search_results(self):
        search_results = []

        if self.results['totalItems'] == 0:
            return 'no results'
        num_results = len(self.results['items'])
        for result in range(num_results):

            formatted_result = {
                'title': self.get_result_title(result),
                'authors': self.get_result_authors(result),
                'publisher': self.get_result_publisher(result),
                'thumbnail': self.get_thumbnail_url(result),
                'goodreads': self.make_goodreads_url(result)
            }
            search_results.append(formatted_result)

        return search_results

    def get_result_title(self, result):
        title = self.results['items'][result]['volumeInfo']['title']

        if 'subtitle' in self.results['items'][result]['volumeInfo']:
            title += ': ' + self.results['items'][result]['volumeInfo']['subtitle']

        return 'title: ' + title

    def get_result_authors(self, result):
        authors = 'unkown'
        if 'authors' in self.results['items'][result]['volumeInfo']:
            authors = ', '.join(self.results['items'][result]['volumeInfo']['authors'])
        return 'authors: ' + authors

    def get_result_publisher(self, result):
        publisher = 'unknown'

        if 'publisher' in self.results['items'][result]['volumeInfo']:
            publisher = self.results['items'][result]['volumeInfo']['publisher']

        return 'publisher: ' + publisher

    def get_thumbnail_url(self, result):
        thumbnail = ''
        if 'imageLinks' in self.results['items'][result]['volumeInfo']:
            thumbnail = self.results['items'][result]['volumeInfo']['imageLinks']['thumbnail']
        return thumbnail

    def make_goodreads_url(self, result):
        goodreads = 'https://www.goodreads.com/book/show/'
        id = str(self.get_goodreads_id(result))
        return goodreads + id

    def get_goodreads_id(self, result):
        goodreads_id = 0
        isbn = self.get_result_isbn(result)
        if isbn:
            goodreads_api = 'https://www.goodreads.com/book/isbn_to_id'
            params = {'key' : 'Hc3p3luBbcApaSFOTIgadQ', 'isbn' : isbn}
            goodreads_response = requests.get(goodreads_api, params=params)
            goodreads_id = goodreads_response.text
        return goodreads_id

    def get_result_isbn(self, result):
        if 'industryIdentifiers' in self.results['items'][result]['volumeInfo']:
            for id in self.results['items'][result]['volumeInfo']['industryIdentifiers']:
                if id['type'] == 'ISBN_13':
                    return id['identifier']
        return 0

    def get_results_count(self):
        return self.results.get("totalItems")
