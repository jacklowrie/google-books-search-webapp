from googlebooksapiquery import GoogleBooksAPIQuery
from goodreadsapiquery import GoodreadsAPIQuery

class BookSearchApp(object):
    def __init__(self, query):
        self.googlebooks_query = GoogleBooksAPIQuery(query)
     
