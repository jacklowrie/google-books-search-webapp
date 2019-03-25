from apiquery import APIQuery

class GoogleBooksAPIQuery(APIQuery):

    def __init__(self, query):
        APIQuery.__init__(self, query)
        self.set_base_url('https://www.googleapis.com/books/v1/volumes')
        self.add_parameter('fields', 'kind,totalItems,items(kind,volumeInfo(title,subtitle,authors,publisher,industryIdentifiers,imageLinks/thumbnail))')
        self.results = []
    def get_results_count(self):
        return self.response.get("totalItems")

    def get_result_title(self, result):
        title = self.response['items'][result]['volumeInfo']['title']

        if 'subtitle' in self.response['items'][result]['volumeInfo']:
            title += ': ' + self.response['items'][result]['volumeInfo']['subtitle']

        return title

    def get_result_authors(self, result):
        authors = 'unknown'
        if 'authors' in self.response['items'][result]['volumeInfo']:
            authors = ', '.join(self.response['items'][result]['volumeInfo']['authors'])
        return authors

    def get_result_publisher(self, result):
        publisher = 'unknown'

        if 'publisher' in self.response['items'][result]['volumeInfo']:
            publisher = self.response['items'][result]['volumeInfo']['publisher']

        return publisher

    def get_result_thumbnail_url(self, result):
        thumbnail = ''
        if 'imageLinks' in self.response['items'][result]['volumeInfo']:
            thumbnail = self.response['items'][result]['volumeInfo']['imageLinks']['thumbnail']
        return thumbnail

    def get_result_isbn(self, result):
        if 'industryIdentifiers' in self.response['items'][result]['volumeInfo']:
            for id in self.response['items'][result]['volumeInfo']['industryIdentifiers']:
                if id['type'] == 'ISBN_13':
                    return id['identifier']
        return 0

    def compile_results(self):

        if self.get_results_count() == 0:
            return 'no results'

        books = len(self.response['items'])
        for book in range(books):
            result = (
                        self.get_result_title(book),
                        self.get_result_authors(book),
                        self.get_result_publisher(book),
                        self.get_result_thumbnail_url(book),
                        self.get_result_isbn(book)
                    )
            self.results.append(result)

    def get_results(self):
        return self.results
