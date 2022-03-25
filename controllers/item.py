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
        args = self.parseRequest()
        Service.createItem(args)
        return "Se ha añadido"
    
    """ Delete """
    def delete(self,name):
        return 

    """ llamas la función ya la request, 
    compruba si teiene las propiedades (tres, name, sell_in, quality) 
    Dice el tipo de objeto que a de ser
    Se puede marcar si queremos que algun valor sea obligatorio
    envia un mensaje en el caso que algo falle"""
    def parseRequest(self):
        parser = reqparse.RequestParser(bundle_errors=True)
        parser.add_argument('name', type=str, required=True,
                            help='introduce el nombre')
        parser.add_argument('sell_in', type=int, required=True,
                            help='introduce un sellIn')
        parser.add_argument('quality', type=int, required=True,
                            help='introduce una quality')
        return parser.parse_args()
