from apiquery import APIQuery

class GoodreadsAPIQuery(APIQuery):

    def __init__(self, query):
        APIQuery.__init__(self, query)
        self.set_base_url('https://www.goodreads.com/book/isbn_to_id')
        self.add_parameter('key', 'Hc3p3luBbcApaSFOTIgadQ')
