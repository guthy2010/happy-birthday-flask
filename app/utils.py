
import os
from werkzeug.utils import import_string


# Util to map configs for test and running the flask server
CONFIG_NAME_MAPPER = {
    'development': 'config.DevelopmentConfig',
    'testing': 'config.TestingConfig',
}

def get_config(config_name=None):
    flask_config_name = os.getenv('ENVIRONMENT', 'development')
    if config_name is not None:
        flask_config_name = config_name
    return import_string(CONFIG_NAME_MAPPER[flask_config_name])