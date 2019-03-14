from apiquery import APIQuery

class GoogleBooksAPIQuery(APIQuery):

    def __init__(self, query):
        APIQuery.__init__(self, query)
        self.set_base_url('https://www.googleapis.com/books/v1/volumes')
        self.add_parameter('fields', 'kind,totalItems,items(kind,volumeInfo(title,subtitle,authors,publisher,industryIdentifiers,imageLinks/thumbnail))')

    def get_results_count(self):
        return self.results.get("totalItems")
