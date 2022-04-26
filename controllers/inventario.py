from flask_restful import Resource, reqparse
from service.Service import Service


class Inventario(Resource):

    def get(self):
        return Service.getAllItems()

