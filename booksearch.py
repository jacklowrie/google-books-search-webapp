import requests


class BookSearch:

    books_api = 'https://www.googleapis.com/books/v1/volumes'
    parameters = {  'q' : '',
                    'fields' : 'kind,items(kind,volumeInfo(title,subtitle,authors,publisher,industryIdentifiers,imageLinks/thumbnail))'
                }
    search = '' #user's search query
    results = '' #response from google books, in json format


    def __init__(self, search):
        self.search = search
        self.make_a_search()



    def make_a_search(self):
        self.construct_request()
        self.send_request()
        self.parse_results()



    def get_search_results(self):
        search_results = []

        if 0 == 0: # if there are no search results
            return 'no results'
        num_results = len(self.results['items'])
        for result in range(num_results):
            # add each result as a dictionary to search_results
            d = {
                'title': self.get_result_title(result),
                'authors': self.get_result_authors(result),
                'publisher': self.get_result_publisher(result),
                'thumbnail': self.get_thumbnail_url(result),
                'goodreads': self.make_goodreads_url(result)
            }
            search_results.append(d)

        return search_results

    #returns the isbn number of a result, if available
    def get_result_isbn(self, result):
        if 'industryIdentifiers' in self.results['items'][result]['volumeInfo']:
            for id in self.results['items'][result]['volumeInfo']['industryIdentifiers']:
                if id['type'] == 'ISBN_13':
                    return id['identifier']
        return 0

    # use the goodreads api to get the goodreads id for a given isbn
    def get_goodreads_id(self, result):
        goodreads_id = 0
        isbn = self.get_result_isbn(result)
        if isbn:
            goodreads_api = 'https://www.goodreads.com/book/isbn_to_id'
            params = {'key' : 'Hc3p3luBbcApaSFOTIgadQ', 'isbn' : isbn}
            goodreads_response = requests.get(goodreads_api, params=params)
            goodreads_id = goodreads_response.text
        return goodreads_id

    # construct link to result on goodreads
    def make_goodreads_url(self, result):
        goodreads = 'https://www.goodreads.com/book/show/'
        id = str(self.get_goodreads_id(result))
        return goodreads + id

    # adds user's search phrase to parameters
    def construct_request(self):
        self.parameters['q'] = self.search

    #send the GET request
    def send_request(self):
        self.search = requests.get(self.books_api, params=self.parameters)

    #store the results in a python dictionary
    def parse_results(self):
        self.results = self.search.json()




    def print_search_results(self):
        num_results = len(self.results['items'])
        for result in range(num_results):
            print('\n' + self.get_result_title(result) )
            print( '\t' + self.get_result_authors(result))
            print( '\t' + self.get_result_publisher(result))
            print( '\t isbn: ' + self.get_result_isbn(result))
            print('\t goodreads id: ' + self.get_goodreads_id(result))
            print('\t goodreads link: ' + self.make_goodreads_url(result))
            print( '\tthumbnail: ' + self.get_thumbnail_url(result) + '\n')

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
    # returns the status code as an int
    def get_status_code(self):
        return self.search.status_code

    # returns the total items found as an int
    def get_results_count(self):
        return self.results.get("totalItems")

    def print_search_url(self): #just for debugging
        print(self.search.url)


# test queries
# many_results = 'harry potter sorcerer\'s stone' #test search many results
# quarter_boys = 'intitle:reckoning+inauthor:david+inauthor:lennon' #test search one result
# no_results = '3ugn398' #test search returns no results
# multiple_authors = 'introduction to algorithms inauthor:Thomas inauthor:H inauthor:Cormen inauthor:Thomas inauthor:H inauthor:Cormen inauthor:Charles inauthor:E inauthor:Leiserson'


#try it out
#test = BookSearch(quarter_boys)
#test.print_search_results()
