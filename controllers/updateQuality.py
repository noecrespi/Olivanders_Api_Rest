from service.Service import Service
from flask_restful import Resource, reqparse
""" es para obtener los datos del body """
from flask import request

"""Resource: clase que da flash par que indique que es un controlador """
class UpdateQuality(Resource):

    def get(self):
        return Service.updateQuality()
