import os

BASEDIR = os.path.abspath(os.path.dirname(__file__))
TEST_DB = 'test.db'


class Config(object):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASEDIR, TEST_DB)
    SECRET_KEY = 'secret'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    OPENWEATHERMAP_API_KEY = 'API_KEY'
