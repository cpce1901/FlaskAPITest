from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restx import Api
from flask_jwt_extended import JWTManager

db = SQLAlchemy()
api = Api(
        version='1.0', 
        title='CLASES MVC API',
        description='A simple CLASES MVC API',
        validate=True
        )
jwt = JWTManager()

def create_app():

    app= Flask(__name__)
    app.config.from_object('config.LocalConfig')

    db.init_app(app)
    api.init_app(app)
    jwt.init_app(app)

    from .apps.admin.views import bp_admin
    app.register_blueprint(bp_admin)

    from .apps.users.resource import ns_users
    from .apps.clases.resource import ns_clases
    from .apps.token.resource import ns_token
    from .models import Users
    api.add_namespace(ns_users)
    api.add_namespace(ns_clases)
    api.add_namespace(ns_token)

    @jwt.user_identity_loader
    def user_identity_lookup(user):
        return user
       
    
    @jwt.user_lookup_loader
    def user_lookup_callback(_jwt_header, jwt_data):
        identity = jwt_data["sub"]
        return Users.query.filter_by(id=identity).one_or_none()

    
    with app.app_context():
        db.create_all()

    return app