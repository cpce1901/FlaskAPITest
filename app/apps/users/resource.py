from app import api, db
from flask_restx import Resource, abort, marshal
from flask_jwt_extended import jwt_required, current_user
from app.models import Users
from .schema import user_model, user_model_create_input, user_model_update_input, user_model_input_pass, user_model_input_change_admin

ns_users = api.namespace('users', description='USERS Operations')

# ready USER
@ns_users.route('/update-user')
class UserUpdate(Resource):

    method_decorators = [jwt_required()]

    @ns_users.doc(security="jsonWebToken")
    @ns_users.expect(user_model_update_input)
    def put(self):

        ''' Update Just DATA One USER BY SELF '''
        user_id = current_user.id
        user = Users.query.get(user_id)
        if user is None:
            abort(404, error='Usuario no existe en la base de datos.')
        
        username = ns_users.payload['username']

        user_exist = Users.query.filter(Users.username==username, Users.id != user_id).first()
        if user_exist:
            abort(403, error=f'Username {username} ya existe en la base de datos.')

        user.username = ns_users.payload['username']
        user.name = ns_users.payload.get('name', None),
        user.last_name = ns_users.payload.get('last_name', None),
        user.email = ns_users.payload['email']

        
        db.session.commit()

        return {
            "user": marshal(user, user_model), 
            "message": f"Usuario actualizado con exito.",  
            } , 203
    

# ready USER
@ns_users.route("/change-pass")
class UserChangePass(Resource):

    method_decorators = [jwt_required()]

    @ns_users.doc(security="jsonWebToken")
    @ns_users.expect(user_model_input_pass)
    def put(self):

        ''' Update Password USER BY SELF'''
        
        user_id = current_user.id
        user = Users.query.get(user_id)

        if user is None:
            abort(404, error="No existe usuario en la base de datos.")

        password_1 = ns_users.payload['new_password']
        password_2 = ns_users.payload['repeat_new_password']
        password_actual = ns_users.payload['actual_password']

        if not user.check_password(password_actual):
            abort(403, error="Las contraseña actual no es la correcta.")

        if password_1 != password_2:
            abort(403, error="Los campos password no coinciden.")
        
        user.password = user.set_password(password_1)
        db.session.commit()

        return {
            "message": "Contraseña actualizada correctamente.",
            "user": f"{user.username}"
            }, 203 


# ready ADMIN
@ns_users.route('/create-user')
class AdminUserCreate(Resource):

    method_decorators = [jwt_required()]

    @ns_users.doc(security="jsonWebToken")
    @ns_users.expect(user_model_create_input)
    def post(self):   

        ''' Create New USER By ADMIN '''

        username = ns_users.payload['username']
        user_exist = Users.query.filter_by(username=username).first()
        
        if user_exist:
            abort(403, 'Ya existe un usuario con este username.')
        
        if not current_user.is_admin:
            abort(403, 'Solo administradores pueden crear nuevos usuarios.')

        user = Users(
            name = ns_users.payload.get('name', None),
            last_name = ns_users.payload.get('last_name', None),
            email = ns_users.payload.get('email', None),
            username = username,
            password = ns_users.payload['password'],
            is_admin = ns_users.payload['is_admin']
            )
        
        db.session.add(user)
        db.session.commit()

        return { "message" : "Usuario creado con exito." }, 201
    

# ready ADMIN
@ns_users.route("/update-user/<id>")
class AdminUserUpdate(Resource):

    method_decorators = [jwt_required()]

    @ns_users.doc(security="jsonWebToken")
    @ns_users.expect(user_model_input_change_admin)
    def put(self, id):

        ''' Update All Data From One USER By ADMIN '''

        if not current_user.is_admin:
            abort(403, 'Solo administradores pueden eliminar usuarios.')

        user = Users.query.get(id)

        if user is None:
            abort(404, error="No existe usuario en la base de datos.")

        name = ns_users.payload.get('name', None),
        last_name = ns_users.payload.get('last_name', None),
        email = ns_users.payload.get('email', None),
        password_1 = ns_users.payload['new_password']
        password_2 = ns_users.payload['repeat_new_password']
        is_admin = ns_users.payload['is_admin']
            
        if password_1 != password_2:
            abort(403, error="Los campos password no coinciden.")
        
        user.name = name
        user.last_name = last_name
        user.email = email
        user.password = user.set_password(password_1)
        user.is_admin = is_admin
        
        db.session.commit()

        return {
            "user": marshal(user, user_model), 
            "message": f"Usuario actualizado con exito.",
            } , 203


# ready ADMIN
@ns_users.route("/delete-user/<id>")
class AdminUserDelete(Resource):

    method_decorators = [jwt_required()]

    @ns_users.doc(security="jsonWebToken")
    def delete(self, id):

        ''' Delete One USER By ADMIN '''

        if not current_user.is_admin:
            abort(403, 'Solo administradores pueden eliminar usuarios.')

        user = Users.query.get(id)
        if user is None:
            abort(404, error="No existe usuario en la base de datos.")
        
        db.session.delete(user)
        db.session.commit()

        return {}, 204


# ready ADMIN
@ns_users.route('/all-users')
class UsersAll(Resource):

    method_decorators = [jwt_required()]

    @ns_users.doc(security="jsonWebToken")
    @ns_users.marshal_list_with(user_model)
    def get(self):

        ''' Get All USERS By ADMIN '''
        if not current_user.is_admin:
            abort(403, 'Solo administradores pueden leer estos registros.')

        return Users.query.all()
    






    
    
    
    