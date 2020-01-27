from marshmallow import Schema, fields, post_dump, pre_load, post_load, validates, ValidationError
from app.database import db
from app.happy_birthday.models import Users


#Schemas to map database relationships
class UserDetailsSchema(Schema):
    username = fields.Str(required=True)
    dateOfBirth = fields.DateTime(required=True)


    @post_load
    def post_datacenter(self,data,**kwargs):
        user = Users(**data)
        db.session.add(user)
        db.session.commit()
        self.instance = user