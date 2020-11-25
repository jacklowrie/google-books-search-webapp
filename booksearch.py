import requests
import dateutil.parser as dparser


class BookSearch:

    books_api = 'https://www.googleapis.com/books/v1/volumes'
    parameters = dict(q='')
    startIndex = 0
    search = ''  # user's search query, populated in __init__
    results = ''  # response from google books, populated by parse_results()
    responseTime = 0
    maxDate = None
    minDate = None
    mostProlific = ''

    def __init__(self, search=''):
        self.search = search

    def make_a_search(self):
        self.construct_request()
        self.send_request()
        # self.send_all_requests()
        self.parse_results()
        if self.results['items']:
            self.analyze_results()

    # adds user's search phrase to parameters
    def construct_request(self):
        self.parameters['q'] = self.search

    def send_request(self):
        self.search = requests.get(self.books_api, params=self.parameters)
        self.responseTime = self.search.elapsed.total_seconds()

    def send_all_requests(self):
        self.parameters['startIndex'] = 0
        self.parameters['maxResults'] = 40
        self.search = requests.get(self.books_api, params=self.parameters)
        if 'totalItems' in self.search.json() and self.search.json()['totalItems'] > 0:
            self.results = self.search.json()
            num_results = self.results['totalItems']
            while self.parameters['startIndex'] < num_results:
                self.parameters['startIndex'] += 40
                next_results = requests.get(self.books_api, params=self.parameters).json()
                if 'items' in next_results:
                    for item in next_results['items']:
                        self.results['items'].append(item)

    # store the results in a python dictionary
    def parse_results(self):
        self.results = self.search.json()

    def get_search_results(self):
        if self.results['totalItems'] == 0:
            return 'no results'

        search_results = {
            'totalResults': self.results['totalItems'],
            'maxDate': self.maxDate,
            'minDate': self.minDate,
            'mostProlific': self.mostProlific,
            'responseTime': self.responseTime,
            'items': []
        }

        num_results = len(self.results['items'])

        # grab results by index from each of the resulting lists
        # send these back to the app for rendering front end
        for result in range(num_results):
            formatted_result = {
                'title': self.get_result_title(result),
                'description': self.get_result_description(result),
                'authors': self.get_result_authors(result),
                'thumbnail': self.get_thumbnail_url(result),
            }
            search_results['items'].append(formatted_result)
        return search_results

    # do a bit of processing on each json object
    def analyze_results(self):
        authors = {}
        dates = []
        for result in self.results['items']:
            if 'authors' in result['volumeInfo']:
                for author in result['volumeInfo']['authors']:
                    if author in authors:
                        authors[author] += 1
                    else:
                        authors[author] = 1
            if 'publishedDate' in result['volumeInfo']:
                dates.append(dparser.parse(result['volumeInfo']['publishedDate']))

        # sort dates to get the earliest and latest
        dates = sorted(dates)
        self.maxDate = dates[-1]
        self.minDate = dates[0]

        # having counted our authors in this traunch, sort and grab the highest count
        if authors:
            sorted_authors = sorted(authors, key=authors.get, reverse=True)
            # self.mostProlific = sorted(authors, key=authors.get, reverse=True)[0]
            plurality = " work." if authors.get(sorted_authors[0]) is 1 else " works."
            self.mostProlific = sorted_authors[0] + " who has contributed to " + str(authors.get(sorted_authors[0])) + plurality

    # collate title and subtitles per volume
    def get_result_title(self, result):
        title = self.results['items'][result]['volumeInfo']['title']
        if 'subtitle' in self.results['items'][result]['volumeInfo']:
            title += ': ' + self.results['items'][result]['volumeInfo']['subtitle']
        return title

    # check for and return a description if present, message otherwise
    def get_result_description(self, result):
        desc = 'No description provided.'
        if 'description' in self.results['items'][result]['volumeInfo']:
            desc = self.results['items'][result]['volumeInfo']['description']
        return desc

    # join all authors with a comma per volume
    def get_result_authors(self, result):
        authors = 'unknown'
        if 'authors' in self.results['items'][result]['volumeInfo']:
            authors = ', '.join(self.results['items'][result]['volumeInfo']['authors'])
        return authors

    # null check publisher, return if present
    def get_result_publisher(self, result):
        publisher = 'unknown'
        if 'publisher' in self.results['items'][result]['volumeInfo']:
            publisher = self.results['items'][result]['volumeInfo']['publisher']
        return publisher

    def get_thumbnail_url(self, result):
        thumbnail = ''
        if 'imageLinks' in self.results['items'][result]['volumeInfo']:
            thumbnail = self.results['items'][result]['volumeInfo']['imageLinks']['thumbnail']
        return thumbnail

    # unclear if relevant, consider removal
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
