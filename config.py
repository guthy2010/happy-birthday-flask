
import os

## Configs for running flask application

class BaseConfig:
    PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
    if os.environ.get('ENVIRONMENT') == 'PROD':
        user = os.environ['POSTGRES_USER']
        pwd = os.environ['POSTGRES_PASSWORD']
        db = os.environ['POSTGRES_DB']
        host = os.environ['POSTGRES_HOST']
        port = os.environ['POSTGRES_PORT']
        SQLALCHEMY_DATABASE_URI = 'postgres://%s:%s@%s:%s/%s' % (user, pwd, host, port, db)
    else:
        SQLALCHEMY_DATABASE_URI = 'sqlite:///%s' % (os.path.join(PROJECT_ROOT, "db.sqlite3"))
    DEBUG=False
    SQLALCHEMY_TRACK_MODIFICATIONS = True

class DevelopmentConfig(BaseConfig):
    ENV='development'
    DEBUG = True
    DOMAIN = 'http://localhost:5000'


class TestingConfig(BaseConfig):
    ENV='testing'
    TESTING = True
    DOMAIN = 'http://testserver'
    # Use memory for DB files
    SQLALCHEMY_DATABASE_URI = 'sqlite://'
