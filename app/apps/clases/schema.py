from app import api
from flask_restx import fields

clases_model = api.model("Clases", {
    "id": fields.Integer(readonly=True, description='The unique identifier'),
    "title": fields.String(description='The title unique identifier'),
    "description": fields.String(description='The description of class')
})

clases_model_input = api.model("ClasesInput", {
    "title": fields.String(min=10, description='The title unique identifier'),
    "description": fields.String(min=40, description='The description of class')
})