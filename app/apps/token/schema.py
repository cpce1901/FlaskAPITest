from app import api
from flask_restx import fields

'''
    id: Int
    name: Str
    last_name: Str
    username: Str
    email: Str
    password: Str

'''

login_model_input = api.model("LoginUser",{
    "username": fields.String(required=True ,min_length=4, max_length=32, description='The description of class'),
    "password": fields.String(required=True ,min_length=4, description='The description of class'),
})


# Structure for show one user
user_model = api.model("Users", {
    "id": fields.Integer(readonly=True, description='The unique identifier'),
    "name": fields.String(max_length=32, description='The name of user'),
    "last_name": fields.String(max_length=32, description='The last name of user'),
    "email": fields.String(max_length=32, description='The email of user'),
    "username": fields.String(required=True, max_length=32, description='The username of user'),
    "is_admin": fields.Boolean(required=True, description='Level new user')
})