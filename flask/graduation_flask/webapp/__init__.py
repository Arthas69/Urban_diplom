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
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    migrate = Migrate()
    migrate.init_app(app, db)

    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'users.login'

    app.register_blueprint(users_bp)
    app.register_blueprint(weather_bp)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)

    @app.route('/', methods=['GET', 'POST'])
    @app.route('/index', methods=['GET', 'POST'])
    def index():
        return render_template('index.html')

    # with app.app_context():
    #     db.create_all()

    return app
