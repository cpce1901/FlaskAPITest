from app import api
from flask_restx import Resource, marshal
from flask_jwt_extended import create_access_token, create_refresh_token, get_jwt_identity, jwt_required
from app.models import Users
from .schema import login_model_input, user_model

ns_token = api.namespace('auth', description='TOKEN Operations')


@ns_token.route("/login")
class LoginResources(Resource):

    @ns_token.expect(login_model_input)
    def post(self):

        ''' LOGIN APP '''

        user_login = ns_token.payload['username']
        password_login = ns_token.payload['password']

        user = Users.query.filter_by(username = user_login).first()

        if not user or not user.check_password(password_login):
            return {"error": "Credenciales ingresadas no validas." }, 403

        return {
            "user": marshal(user, user_model),
            "keys": {
            "access_token": create_access_token(user.id),
            "refresh_token": create_refresh_token(user.id),
            }
        }


@ns_token.route("/refresh")
class RefreshResource(Resource):

    method_decorators = [jwt_required(refresh=True)]

    @ns_token.doc(security="jsonWebToken")
    def post(self):

        ''' REFRESH TOKEN APP '''

        identity = get_jwt_identity()
        access_token = create_access_token(identity=identity)

        return {
           "access_token": access_token
        }