
from service.Service import Service
from flask_restful import Resource, reqparse
""" es para obtener los datos del body """
from flask import request

class Quality(Resource):
    """ OBTENER """
    def get(self, quality):
        return Service.getByQuality(quality)
    