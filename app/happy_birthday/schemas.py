from marshmallow import Schema, fields, post_dump, pre_load, post_load, validates, ValidationError
from app.database import db
from app.happy_birthday.models import Users
from datetime import datetime,timedelta

#Schemas to map database relationships
class UserDetailsSchema(Schema):
    username = fields.Str(required=True)
    dateOfBirth = fields.DateTime(required=True)


    @validates('username')
    def validate_username(self, username, **kwargs):
        if not username.isalpha():
            raise ValidationError(
                '{username} contains characters that are not letters!'.format(username=username)
            )
        if bool(Users.query.filter_by(username=username).first()):
            raise ValidationError(
                '{username}" user already exists.'.format(username=username)
            )


    @pre_load
    def clean_userdata(self,data, **kwargas):
        data['dateOfBirth'] = datetime.strptime(data['dateOfBirth'], '%Y-%m-%d').isoformat()
        return data


    @post_load
    def post_datacenter(self,data,**kwargs):
        user = Users(**data)
        db.session.add(user)
        db.session.commit()
        self.instance = user


    @post_dump
    def calculate_birthday(self,data,**kwargs):
        date = datetime.strptime(data['dateOfBirth'], "%Y-%m-%dT%H:%M:%S")
        today = datetime.now()
        cleaned_date = date.replace(year=today.year)
        birthday = abs(today - cleaned_date).days
        if birthday > 0:
            ret = 'Hello, {user}! Your birthday is in {birthday} day(s)'.format(user=data['username'], birthday=birthday)
        else:
            ret = 'Hello, {user}! Happy Birthday!)'.format(user=data['username'])
        data['birthday_info'] = ret
        return data
