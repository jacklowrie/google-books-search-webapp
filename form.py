from flask_wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class SearchForm(Form):
    search_query = StringField('Search')
    submit = SubmitField('search', validators=[DataRequired("Enter a search phrase.")])
