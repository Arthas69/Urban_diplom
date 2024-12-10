import requests

from flask import render_template, redirect, url_for, flash, request, current_app
from flask_login import current_user
from flask.blueprints import Blueprint

from .forms import SearchForm
from .models import City

from webapp import db


# Create BP for weather views
blueprint = Blueprint('weather', __name__, url_prefix='/weather')


def get_weather_data(lat, lon):
    """
    Fetch weather data for given latitude and longitude.
    """
    base_url = "https://api.openweathermap.org/data/2.5/weather?"
    complete_url = f"{base_url}appid={current_app.config['OPENWEATHERMAP_API_KEY']}&lat={lat}&lon={lon}"
    response = requests.get(complete_url)
    return response.json()


def parse_data(data):
    """
    Parse weather data from API response.
    """
    main = data['main']
    content = {
        'name': data['name'],
        'temperature': round(main["temp"] - 273.15, 1),  # Convert Kelvin to Celsius
        'humidity': main.get("humidity", None),
        'visibility': round(data.get("visibility", 0) / 1000, 1),
        'icon': f'https://openweathermap.org/img/wn/{data["weather"][0]["icon"]}@2x.png',
        'weather_desc': data["weather"][0].get("description", None),
        'lat': data["coord"]["lat"],
        'lon': data["coord"]["lon"],
    }
    return content


@blueprint.route('/', methods=['GET', 'POST'])
def get_all_weather_data():
    """
    Get all cities with provided name.
    """
    form = SearchForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            city_name = form.city_name.data
            cities = City.query.filter_by(name=city_name).all()
            if not cities:
                geocoding_api = f'http://api.openweathermap.org/geo/1.0/direct?limit=5&appid={current_app.config['OPENWEATHERMAP_API_KEY']}&q={city_name}'
                items = requests.get(geocoding_api).json()
                cities = []
                for item in items:
                    city = City(name=item['name'], state=item['state'], country=item['country'], lat=item['lat'], lon=item['lon'])
                    db.session.add(city)
                    db.session.commit()
                    cities.append(city)
            return render_template('weather/all_cities.html', cities=cities, form=form)
    return render_template('weather/all_cities.html', form=form)


@blueprint.route('/<int:city_id>', methods=['GET', 'POST'])
def get_city_weather(city_id):
    """
    Get weather data for specific city.
    """
    city = City.query.get(city_id)
    if city:
        data = get_weather_data(city.lat, city.lon)
        if data["cod"] != "404":
            content = parse_data(data)
            content.update({'city_id': city.id})
            return render_template('weather/city.html', **content)
        else:
            flash("City not found")
            return redirect(url_for('weather.get_all_weather_data'))
    else:
        flash("City not found")
        return redirect(url_for('weather.get_all_weather_data'))


@blueprint.route('/my_cities')
def my_cities():
    """
    Get weather data for cities user is subscribed to.
    """
    cities = current_user.cities
    data = []
    for city in cities:
        city_data = parse_data(get_weather_data(city.lat, city.lon))
        city_data.update({'city_id': city.id})
        data.append(city_data)

    return render_template('weather/my_cities.html', cities=data)


@blueprint.route('/add')
def add_city():
    """
    Add city to user's subscriptions.
    """
    try:
        idx = int(request.args.get('city_id'))
    except ValueError:
        flash('Invalid city ID')
        return redirect(url_for('weather.get_all_weather_data'))
    city = City.query.get(idx)
    if not city:
        flash('Failed!')
        return redirect(url_for('weather.get_all_weather_data'))
    city.users.append(current_user)
    db.session.commit()
    flash('Success!')
    return redirect(url_for('weather.get_all_weather_data'))


@blueprint.route('/remove', methods=['GET'])
def remove_city():
    """
    Remove city from user's subscriptions.
    """
    try:
        idx = int(request.args.get('city_id'))
        print(idx)
    except ValueError:
        flash('Invalid city ID')
        return redirect(url_for('weather.get_all_weather_data'))
    city = City.query.get(idx)
    if not city:
        flash('City Not Found')
        return redirect(url_for('weather.get_all_weather_data'))
    city.users.remove(current_user)
    # current_user.cities.remove(city)
    db.session.commit()
    flash('Success!')
    return redirect(url_for('weather.my_cities'))
