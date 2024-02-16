from app import api, db
from .schema import clases_model, clases_model_input
from flask_restx import Resource, abort
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models import Clases

authorizations = {
    "jsonWebToken":{
        "type": "apiKey",
        "in": "header",
        "name": "Authorization"
    }
}

ns_clases = api.namespace('clases', authorizations=authorizations, description='CLASES Operations')

@ns_clases.route('/')
class ClasesResources(Resource):

    method_decorators = [jwt_required()]

    @ns_clases.doc(security="jsonWebToken")
    @ns_clases.marshal_list_with(clases_model)
    def get(self):

        ''' Get all CLASES '''

        return Clases.query.all()
    
    @ns_clases.doc(security="jsonWebToken")
    @ns_clases.expect(clases_model_input)
    @ns_clases.marshal_with(clases_model)
    def post(self):
        
        ''' Create New CLASE '''

        clase = Clases(
            title=ns_clases.payload['title'],
            description=ns_clases.payload['description']
            )
        
        db.session.add(clase)
        db.session.commit()
        return clase, 201
    

@ns_clases.route('/<int:id>')
class ClasesResourceDetail(Resource):

    method_decorators = [jwt_required()]

    @ns_clases.doc(security="jsonWebToken")
    @ns_clases.marshal_with(clases_model)
    def get(self, id):

        ''' Get Just One CLASES '''

        clase = Clases.query.get(id)
        if clase is None:
            abort(404, error='Usuario no existe en la base de datos.')
        
        return clase    

    @ns_clases.doc(security="jsonWebToken")
    @ns_clases.expect(clases_model_input)
    @ns_clases.marshal_with(clases_model)
    def put(self, id):

        ''' Update Just One CLASES '''

        clase = Clases.query.get(id)
        if clase is None:
            abort(404, error='Usuario no existe en la base de datos.')
        
        clase.title=ns_clases.payload['title'],
        clase.description=ns_clases.payload['description']
        db.session.commit()

        return clase
    
    @ns_clases.doc(security="jsonWebToken")
    def delete(self, id):

        ''' Delete Just One CLASES '''

        clase = Clases.query.get(id)
        if clase is None:
            abort(404, error='Usuario no existe en la base de datos.')
        
        db.session.delete(clase)
        db.session.commit()
        return {}, 204
    
