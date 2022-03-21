""" Importación de los paquetes de flask """
from flask import Flask
from flask_restful import Resource, Api
from controllers.quality import Quality
from controllers.updateQuality import UpdateQuality
from controllers.sell_in import SellIn
""" importación de los archivos del proyecto"""
from controllers.inventario import Inventario
from controllers.item import Item

from repository.db import initApp

app = Flask(__name__)
api = Api(app)

initApp(app)


api.add_resource(Inventario,"/getAllItems")
api.add_resource(Item,"/items/<name>", "/items")
api.add_resource(SellIn,"/sellin/<sellin>", "/sellin")
api.add_resource(Quality,"/quality/<quality>", "/quality")
api.add_resource(UpdateQuality,"/updateQuality")
