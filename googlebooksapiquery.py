from apiquery import APIQuery

class GoogleBooksAPIQuery(APIQuery):

    def __init__(self, query):
        APIQuery.__init__(self, query)
        self.base_url = 'https://www.googleapis.com/books/v1/volumes'
        self.parameters['fields'] = 'kind,totalItems,items(kind,volumeInfo(title,subtitle,authors,publisher,industryIdentifiers,imageLinks/thumbnail))'
