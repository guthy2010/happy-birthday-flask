from http import HTTPStatus

from flask import Blueprint, jsonify
from flask import request
from datetime import datetime

from app.happy_birthday.models import Users
from app.happy_birthday.schemas import UserDetailsSchema
from app.database import db

# Establish blueprint
happy_birthday = Blueprint('hello', __name__)

# Add get method to route for specific searching or fetching all
@happy_birthday.route('/', methods=["GET"])
def retrieve_username(username=None):
    datacenters = Users.query.all()
    schema = UserDetailsSchema(many=True).dump(datacenters)
    return jsonify(schema), HTTPStatus.OK


@happy_birthday.route('/<string:username>', methods = ['POST'], strict_slashes=False)
def add_user(username=None):
    data = request.get_json()
    data['username'] = username
    schema = UserDetailsSchema()
    schema.load(data)
    return jsonify(schema.dump(data)), HTTPStatus.CREATED