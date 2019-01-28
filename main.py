from flask import Flask, render_template, request
from form import SearchForm

app = Flask(__name__)
app.secret_key = 'QVwI5uhPuU'

@app.route('/', methods=["GET", "POST"])
def home():
    form = SearchForm() #instantiate the form
    if request.method == 'POST': #if submitting the form
        if form.validate() == False: #check for valid input
            return render_template("index.html", form=form)
        else:
            return "Success!"
    elif request.method == 'GET': #if returning results
        return render_template("index.html", form=form)

if __name__ == '__main__':
    app.run(debug=True)
