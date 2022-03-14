from flask_restful import fields, marshal_with
from repository.db import getDb
from flask import g 




db =  []

class Service:
    
    inventoryResourceFields = {
        "name": fields.String,
        "sell_in": fields.Integer,
        "quality": fields.Integer,
    }

    """ Devuelve todos los items, o sea toda la base de datos """
    @marshal_with(inventoryResourceFields)
    def getAllItems():
        db = getDb()
        inventario = []
        for item in g.Items.objects():
            inventario.append(item)
        return inventario

    """ Busca un nombre de un item y te devuelve todo el valor """
    @marshal_with(inventoryResourceFields)
    def getByName(name):
        db = getDb()
        inventario =[]
        for item in g.Items.objects():
            if name == item['name']:
                inventario.append(item)
        return inventario
    
    """ Crear un item y lo añade"""
    def createItem(item):
        db.append(item)

    """ Eliminar un item """
    def deleteItem(name):
        for item in db:
            if name == item["nombre"]:
                db.remove(item)
                return db
        return "No existe este item"
