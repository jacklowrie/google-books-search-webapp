

import requests #this thing is awesome

# test queries
hp = 'harry potter sorcerer\'s stone' #test search many results
quarterboys = 'intitle:reckoning+inauthor:david+inauthor:lennon' #test search one result
noresults = '3ugn398' #test search returns no results

class BookSearch:

    books_api = 'https://www.googleapis.com/books/v1/volumes'
    parameters = {'q' : noresults, 'projection' : 'lite'}
    search = ''
    results = ''

    def __init__(self, search):
        self.search = search

#construct the GET request
    def construct_request(self):
        self.parameters['q'] = self.search

    def send_request(self):
        self.search = requests.get(self.books_api, params=self.parameters)

    def parse_results(self):
        self.results = self.search.json()

    def make_a_search(self):
        self.construct_request()
        self.send_request()
        self.parse_results()




    def print_search_url(self):
        print(self.search.url)
    def print_search_status_code(self):
        print('HTTP Status Code: ' + str(self.search.status_code))
    def print_results_count(self):
        print('number of results: ' + str(self.results.get("totalItems")))
    def print_results(self):
        print(self.results)
    def print_result_title(self):
        print ('title: ' + self.results['items'][0]['volumeInfo']['title']
                +': '
                + self.results['items'][0]['volumeInfo']['subtitle']
                + '\n\t'
                + str(self.results['items'][0]['volumeInfo']['authors']))
    def dump_search_results(self):
        self.print_search_status_code()
        self.print_results_count()
        self.print_result_title()
#try it out
test = BookSearch(quarterboys)
test.make_a_search()
test.dump_search_results()
