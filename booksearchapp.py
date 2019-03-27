from googlebooksapiquery import GoogleBooksAPIQuery
from goodreadsapiquery import GoodreadsAPIQuery

class BookSearchApp(object):
    def __init__(self, query):
        self.googlebooks_query = GoogleBooksAPIQuery(query)
        self.googlebooks_query.query_api()
        self.books = self.googlebooks_query.compile_results()
        self.results = []

    def create_result_list(self):
        for book in self.books:
            isbn = book[4]
            goodreads_link = self.get_goodreads_link(isbn)

            result = {  'title'     : book[0],
                        'authors'   : book[1],
                        'publisher' : book[2],
                        'thumbnail' : book[3],
                        'goodreads' : goodreads_link
            }
            self.results.append(result)

    def get_goodreads_link(self, isbn):
        query = GoodreadsAPIQuery(isbn)
        query.query_api()
        return query.get_results()

    def get_results(self):
        return self.results
