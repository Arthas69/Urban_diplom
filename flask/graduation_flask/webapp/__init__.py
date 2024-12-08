from flask import Flask, render_template
from flask_login import login_required, LoginManager
from flask_migrate import Migrate

from .config import Config
from .db import db

from .users import blueprint as users_bp
from .weather import blueprint as weather_bp
from .users import User
from .weather import City


def create_app():
    # Create or app and configure it from Config file
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize DB with flask app
    db.init_app(app)

    # Initialize migrations
    migrate = Migrate()
    migrate.init_app(app, db)

    # Initialize login manager and set login view to users.login route
    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'users.login'

    # Register blueprints for users and weather views
    app.register_blueprint(users_bp)
    app.register_blueprint(weather_bp)

    # Set user loader callback to load user by ID from User model
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)

    # Define route for homepage and index page
    @app.route('/', methods=['GET', 'POST'])
    @app.route('/index', methods=['GET', 'POST'])
    def index():
        return render_template('index.html')

    # Create all tables in DB
    # with app.app_context():
    #     db.create_all()

    # Return created and configured application
    return app
