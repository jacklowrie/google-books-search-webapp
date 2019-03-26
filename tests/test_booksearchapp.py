import pytest
import requests_mock
import json

from booksearchapp import BookSearchApp

test_results = json.dumps({ 'kind': 'books#volumes',
                    'totalItems': 1,
                    'items': [{ 'kind': 'books#volume',
                                'volumeInfo': { 'title': 'Reckoning',
                                                'subtitle': 'The Quarter Boys',
                                                'authors': ['David Lennon'],
                                                'publisher': 'Createspace Indie Pub Platform',
                                                'industryIdentifiers': [{   'type': 'ISBN_10',
                                                                            'identifier': '1475009216'
                                                                        },
                                                                        {  'type': 'ISBN_13',
                                                                            'identifier': '9781475009217'
                                                                        }],
                                                'imageLinks': {'thumbnail': 'http://books.google.com/books/content?id=Osn8ugAACAAJ&printsec=frontcover&img=1&zoom=1&source=gbs_api'}
                                                }
                            }]
})


def test_can_make_booksearchapp():
    test = BookSearchApp('test')
    assert isinstance(test, BookSearchApp)

def test_can_query_googlebooks(requests_mock):
    requests_mock.get('https://www.googleapis.com/books/v1/volumes',
                      text=test_results
                      )
    search = BookSearchApp('intitle:reckoning inauthor:david inauthor:lennon')
    assert search.googlebooks_query.get_results() == [(  'Reckoning: The Quarter Boys',
                                        'David Lennon',
                                        'Createspace Indie Pub Platform',
                                        'http://books.google.com/books/content?id=Osn8ugAACAAJ&printsec=frontcover&img=1&zoom=1&source=gbs_api',
                                        '9781475009217'
                                    )]

def test_can_add_goodreads_link(requests_mock):
    requests_mock.get('https://www.googleapis.com/books/v1/volumes',
                      text=test_results
                      )
    search = BookSearchApp('intitle:reckoning inauthor:david inauthor:lennon')

    requests_mock.get('https://www.goodreads.com/book/isbn_to_id',
                      text='14429101'
                      )
    link = search.get_goodreads_link(search.books[0])
    assert link == 'https://www.goodreads.com/book/show/14429101'


def test_can_create_result_list(requests_mock):
        requests_mock.get('https://www.googleapis.com/books/v1/volumes',
                          text=test_results
                          )
        search = BookSearchApp('intitle:reckoning inauthor:david inauthor:lennon')

        requests_mock.get('https://www.goodreads.com/book/isbn_to_id',
                          text='14429101')
        search.create_result_list()
        assert search.get_results() == [{ 'title' : 'Reckoning: The Quarter Boys',
                                    'authors' : 'David Lennon',
                                    'publisher' : 'Createspace Indie Pub Platform',
                                    'thumbnail' : 'http://books.google.com/books/content?id=Osn8ugAACAAJ&printsec=frontcover&img=1&zoom=1&source=gbs_api',
                                    'goodreads' : 'https://www.goodreads.com/book/show/14429101'}]
