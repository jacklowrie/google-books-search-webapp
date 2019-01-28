

import requests #this thing is awesome


class BookSearch:

    books_api = 'https://www.googleapis.com/books/v1/volumes'
    parameters = {'q' : '', 'projection' : 'lite'}
    search = ''
    results = ''

    def __init__(self, search):
        self.search = search

    #construct the GET request
    def construct_request(self):
        self.parameters['q'] = self.search

    #send the GET request
    def send_request(self):
        self.search = requests.get(self.books_api, params=self.parameters)

    #store the results in a python dictionary
    def parse_results(self):
        self.results = self.search.json()

    def make_a_search(self):
        self.construct_request()
        self.send_request()
        self.parse_results()

    def print_search_url(self): #just for debugging
        print(self.search.url)

    # returns the status code as an int
    def get_status_code(self):
        return self.search.status_code

    # returns the total items found as an int
    def print_results_count(self):
        return self.results.get("totalItems")

    def print_results(self):
        print(self.results)

    def get_result_title(self):
        title = self.results['items'][0]['volumeInfo']['title']

        if 'subtitle' in self.results['items'][0]['volumeInfo']:
            title += ': ' + self.results['items'][0]['volumeInfo']['subtitle']

        return 'title: ' + title

    def get_result_author(self):
        authors = ', '.join(self.results['items'][0]['volumeInfo']['authors'])
        return 'authors: ' + authors

    def dump_search_results(self):
        print("HTTP Status Code: " +str(self.get_status_code()))
        print("total results: " + str(self.print_results_count())+'\n')
        print(self.get_result_title())
        print('\t' + self.get_result_author())


# test queries
many_results = 'harry potter sorcerer\'s stone' #test search many results
quarter_boys = 'intitle:reckoning+inauthor:david+inauthor:lennon' #test search one result
no_results = '3ugn398' #test search returns no results
multiple_authors = 'introduction to algorithms inauthor:Thomas inauthor:H inauthor:Cormen inauthor:Thomas inauthor:H inauthor:Cormen inauthor:Charles inauthor:E inauthor:Leiserson'


#try it out
test = BookSearch(multiple_authors)
test.make_a_search()
test.dump_search_results()
