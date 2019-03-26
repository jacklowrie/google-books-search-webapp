from apiquery import APIQuery

class GoodreadsAPIQuery(APIQuery):

    def __init__(self, query):
        APIQuery.__init__(self, query)
        self.set_base_url('https://www.goodreads.com/book/isbn_to_id')
        self.add_parameter('key', 'Hc3p3luBbcApaSFOTIgadQ')
        self.goodreads_book_url = 'https://www.goodreads.com/book/show/'

    def get_results(self):
        url = self.goodreads_book_url + str(self.get_response())
        return url
