from flask import render_template, Blueprint
from app import db
from app.models import Users, Clases


bp_admin = Blueprint('admin', __name__, url_prefix='/admin')


@bp_admin.route("/login")
def login():
    return render_template('admin/login.html')


@bp_admin.route("/")
def admin():
    return render_template('admin/admin.html')