from ast import Delete
from service.Service import Service
from flask_restful import Resource, reqparse
""" es para obtener los datos del body """
from flask import request

class Item(Resource):
    """ OBTENER """
    def get(self, name):
        return Service.getByName(name)
    
    """ CREAR """
    def post(self):
        args = request.get_json()
        Service.createItem(args)
        return "Se ha añadido"
    
    """ Delete """
    def delete(self,name):
        return Service.deleteItem(name)
