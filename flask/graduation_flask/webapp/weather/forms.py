from flask_wtf import FlaskForm

from wtforms import SubmitField, StringField
from wtforms.validators import DataRequired


class SearchForm(FlaskForm):
    """
    Form for searching weather data for a specific city.
    """
    city_name = StringField('City name', validators=[DataRequired()], render_kw={'class': 'form-control'})
    submit = SubmitField('Search', render_kw={'class': "btn btn-success"})
