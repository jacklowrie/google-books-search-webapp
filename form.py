from flask_wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length


class SearchForm(Form):
    search_query = StringField('Search', validators=[DataRequired("Enter a search phrase."), Length(max=68)])
    submit = SubmitField('search')


class PaginateForm(Form):
    search_query = StringField('Search', validators=[DataRequired("Enter a search phrase."), Length(max=68)])
    submit = SubmitField('nextResults')

