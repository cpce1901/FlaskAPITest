from app import db
from sqlalchemy import Integer, String, Column, Text, Boolean, ForeignKey
from werkzeug.security import generate_password_hash, check_password_hash

users_clases = db.Table('users_clases',
    Column('users_id', Integer, ForeignKey('users.id')),
    Column('clases_id', Integer, ForeignKey('clases.id'))
)


class Users(db.Model):

    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(32), nullable=True)
    last_name = Column(String(32), nullable=True)
    email = Column(String(32), nullable=True)
    username = Column(String(32), nullable=False, unique=True)
    password = Column(Text, nullable=False)
    is_admin = Column(Boolean, nullable=False, default=False)
    all_clases = db.relationship('Clases', secondary=users_clases, backref='all_clases')

    def __init__(self, username, password, email=None, name=None, last_name=None, is_admin=False):
        self.name = name
        self.last_name = last_name
        self.username = username
        self.email = email
        self.password = self.set_password(password)
        self.is_admin = is_admin

    def set_password(self, password):
        return generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)
    
    
    def __repr__(self):
        return f"<{self.id}  {self.name} {self.last_name} - {self.email} - {self.username} >"
    
    
    def __str__(self):
        return f"<{self.name} {self.last_name} - {self.email} - {self.username} >"
    

class Clases(db.Model):

    __tablename__ = 'clases'

    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    description = Column(Text)


    def __init__(self, title, description):
        self.title = title,
        self.description = description

 
    def __repr__(self):
        return f'<User: {self.title} >'