""" Importación de los paquetes de flask """
from flask import Flask
from flask_restful import Resource, Api
""" importación de los archivos del proyecto"""
from controllers.inventario import Inventario
from controllers.item import Item

from repository.db import initApp

app = Flask(__name__)
api = Api(app)

initApp(app)


api.add_resource(Inventario,"/getAllItems")
api.add_resource(Item,"/items/<name>", "/items")


