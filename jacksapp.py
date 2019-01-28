

import requests #this thing is awesome


class BookSearch:

    books_api = 'https://www.googleapis.com/books/v1/volumes'
    parameters = {'q' : '', 'projection' : 'lite'}
    search = ''
    results = ''

    def __init__(self, search):
        self.search = search



    def make_a_search(self):
        self.construct_request()
        self.send_request()
        self.parse_results()

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
            print( '\t' + self.get_result_publisher(result) + '\n')

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



    # returns the status code as an int
    def get_status_code(self):
        return self.search.status_code

    # returns the total items found as an int
    def get_results_count(self):
        return self.results.get("totalItems")

    def print_search_url(self): #just for debugging
        print(self.search.url)



    def dump_search_results(self):
        print("HTTP Status Code: " +str(self.get_status_code()))
        print("total results: " + str(self.get_results_count())+'\n')
        print(self.get_result_title())
        print('\t' + self.get_result_authors())


# test queries
many_results = 'harry potter sorcerer\'s stone' #test search many results
quarter_boys = 'intitle:reckoning+inauthor:david+inauthor:lennon' #test search one result
no_results = '3ugn398' #test search returns no results
multiple_authors = 'introduction to algorithms inauthor:Thomas inauthor:H inauthor:Cormen inauthor:Thomas inauthor:H inauthor:Cormen inauthor:Charles inauthor:E inauthor:Leiserson'


#try it out
test = BookSearch(many_results)
test.make_a_search()
test.print_search_results()
