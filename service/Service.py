from flask_restful import fields, marshal_with
from repository.db import getDb
from flask import g, redirect, render_template
from domain.GildedRose import *
from repository.models import Items 

""" Parte que llora y no se si está bien """
class Service:
    
    inventoryResourceFields = {
        "name": fields.String,
        "sell_in": fields.Integer,
        "quality": fields.Integer,
    }

    """ Devuelve todos los items, o sea toda la base de datos """
    """ @marshal_with = a forma a la respuesta """
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

    """ Busca un nombre de un sell_in y te devuelve todo el valor """
    @marshal_with(inventoryResourceFields)
    def getBySellIn(sellIn):
        db = getDb()
        inventario =[]
        for item in g.Items.objects():
            if item['sell_in'] == int(sellIn):
                inventario.append(item)
        return inventario

    """ Busca un nombre de un quality y te devuelve todo el valor """
    @marshal_with(inventoryResourceFields)
    def getByQuality(quality):
        db = getDb()
        inventario =[]
        for item in g.Items.objects():
            if item['quality'] == int(quality):
                inventario.append(item)
        return inventario

    """ Crear un item y lo añade"""
    @marshal_with(inventoryResourceFields)
    def createItem(item):
        db = getDb()
        item = g.Items(name=item['name'], sell_in=item['sell_in'], quality=item['quality'])
        item.save()
        return 'Se ha añadido correctamente el item'


    """ Eliminar un item """
    def deleteItem(name):
        db = getDb()
        message = 'No existe este item'
        for item in g.Items.objects():
            if name == item['name']:
                item.delete()
                message = 'Se han borrado los objetos'
        return message
        
    """ Actualizar los items """
    def updateQuality():
        db = getDb()
        classNames = {
            'Backstage Pass' : 'Backstage',
            'Conjured Mana Cake' : 'Conjured',
            'Sulfuras, Hand of Ragnaros' : 'Sulfuras',
            'Aged Brie' : 'AgedBrie'
        }
        for item in g.Items.objects():
            itemTupla = [item['name'], item['sell_in'], item['quality']]
            try:
                className = classNames[item['name']]
            except:
                className = 'NormalItem'
            
            """ eval : encontar una clase que coincida en la string className """
            pythonObject = eval(className + str(tuple(itemTupla)))
            pythonObject.updateQuality()
            item.sell_in = pythonObject.sellIn
            item.quality = pythonObject.quality
            item.save()
        return Service.getAllItems()