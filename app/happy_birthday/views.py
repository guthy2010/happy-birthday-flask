from http import HTTPStatus
from flask import Blueprint, jsonify
from flask import request
from marshmallow import ValidationError
from app.happy_birthday.models import Users
from app.happy_birthday.schemas import UserDetailsSchema
from app.database import db

# Establish blueprint
happy_birthday = Blueprint('hello', __name__)

# Add get method to route for specific searching or fetching all
@happy_birthday.route('/', methods=['GET'])
@happy_birthday.route('/<string:username>', methods = ['GET'], strict_slashes=False)
def retrieve_username(username=None):
    if username:
        try:
            user = Users.query.filter_by(username=username).first_or_404()
            schema = UserDetailsSchema().dump(user)
            return jsonify(schema['birthday_info']), HTTPStatus.OK

        except Exception:
            return '{} not found!'.format(username), HTTPStatus.BAD_REQUEST

        users = Users.query.all()
        schema = UserDetailsSchema(many=True).dump(users)

    return jsonify(schema), HTTPStatus.OK


@happy_birthday.route('/<string:username>', methods = ['POST','PUT'], strict_slashes=False)
def add_user(username=None):
    data = request.get_json()
    data['username'] = username
    try:
        UserDetailsSchema().load(data)
    except ValidationError as err:
        return jsonify(err.messages), HTTPStatus.BAD_REQUEST

    return jsonify(data), HTTPStatus.CREATED