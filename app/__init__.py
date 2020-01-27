
import os

from flask import Flask

from app.utils import get_config

from app.database import init_db
from app.happy_birthday.views import happy_birthday
from app.happy_birthday.models import Users


def create_app(config_name=None, **kwargs):
    app = Flask(__name__, **kwargs)
    try:
        app.config.from_object(get_config(config_name))

    except ImportError:
        raise Exception('Invalid Config')
    app.register_blueprint(happy_birthday, url_prefix='/hello')
    init_db(app)

    return app