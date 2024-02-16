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

# Structure for show one user
user_model = api.model("Users", {
    "id": fields.Integer(readonly=True, description='The unique identifier'),
    "name": fields.String(max_length=32, description='The name of user'),
    "last_name": fields.String(max_length=32, description='The last name of user'),
    "email": fields.String(max_length=32, description='The email of user'),
    "username": fields.String(required=True, max_length=32, description='The username of user'),
    "is_admin": fields.Boolean(required=True, description='Level new user')
})

# Structure for create userself
user_model_create_input = api.model("UserCreateInput", {
    "username": fields.String(required=True, max_length=32, description='The username of user'),
    "password": fields.String(required=True, description='The password of user'),
    "is_admin": fields.Boolean(required=True, description='Level new user')
})

# Structure for update userself
user_model_update_input = api.model("UsersUpdateInput", {
    "name": fields.String(max_length=32, description='The name of user'),
    "last_name": fields.String(max_length=32, description='The last name of user'),
    "email": fields.String(max_length=32, description='The email of user'),
    "username": fields.String(required=True, max_length=32, description='The username of user'),
})

# Structure for update password by userself
user_model_input_pass = api.model("UsersInputPass", {
    "new_password": fields.String(required=True, description='The password of user'),
    "repeat_new_password": fields.String(required=True, description='Confirmed New PassWord'),
    "actual_password": fields.String(required=True, description='Confirmed with actual password'),
})

# Structure for update data of user my admin user
user_model_input_change_admin = api.model("UserInputChangeAdmin", {
    "name": fields.String(max_length=32, description='The name of user'),
    "last_name": fields.String(max_length=32, description='The last name of user'),
    "email": fields.String(max_length=32, description='The email of user'),
    "new_password": fields.String(description='The password of user'),
    "repeat_new_password": fields.String(description='Confirmed New PassWord'),
    "is_admin": fields.Boolean(description='Level new user')
})



