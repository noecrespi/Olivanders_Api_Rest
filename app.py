from flask import Flask
from flask_restful import Resource, Api
from controllers.inventario import Inventario
from controllers.item import Item


app = Flask(__name__)
api = Api(app)


api.add_resource(Inventario,"/getAllItems")
api.add_resource(Item,"/items/<name>", "/items")


