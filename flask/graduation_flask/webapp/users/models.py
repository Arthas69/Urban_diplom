from flask_login import UserMixin
from werkzeug.security import check_password_hash, generate_password_hash

from webapp.db import db


class User(db.Model, UserMixin):
    """
    User model with username, password, email, visible name, firstname, and lastname fields.
    """
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, index=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    email = db.Column(db.String, index=True, unique=True, nullable=False)
    visible_name = db.Column(db.String(40))
    firstname = db.Column(db.String, nullable=True)
    lastname = db.Column(db.String, nullable=True)

    def set_password(self, password):
        """
        Hash the password before saving it to the database.
        """
        self.password = generate_password_hash(password)

    def check_password(self, password):
        """
        Check if the provided password matches the stored hash.
        """
        return check_password_hash(self.password, password)

    def __repr__(self):
        return '<User {}>'.format(self.username)
