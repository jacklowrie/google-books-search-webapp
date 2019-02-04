from flask import Flask, render_template, request
from form import SearchForm
from booksearch import BookSearch
import logging
import sys

app = Flask(__name__)
app.secret_key = 'QVwI5uhPuU'

app.logger.addHandler(logging.StreamHandler(sys.stdout))
app.logger.setLevel(logging.ERROR)

@app.route('/', methods=["GET", "POST"])
def home():
    form = SearchForm() #instantiate the form
    results = []
    if request.method == 'POST': #if submitting the form
        if form.validate() == False: #check for valid input
            return render_template("index.html", form=form)
        else:
            # Query google books
            search_query = form.search_query.data
            book_search = BookSearch(search_query)
            book_search.make_a_search()
            results = book_search.get_search_results()
            return render_template("index.html", form=form, results=results)
    elif request.method == 'GET': #if returning results
        return render_template("index.html", form=form, results=results)

if __name__ == '__main__':
    app.run()
