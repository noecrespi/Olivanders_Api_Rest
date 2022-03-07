from repository.db import DB

db =  DB.init_db()

class Service:
    """ Devuelve todos los items, o sea toda la base de datos """
    def getAllItems():
        return db

    """ Busca un nombre de un item y te devuelve todo el valor """
    def getByName(name):
            
        for item in db:
            if name == item['nombre']:
                return item

    """ Crear un item """
    def createItem(item):
        db.append(item)

    """ Delete """
    def deleteItem(name):
        for item in db:
            if name == item["nombre"]:
                db.remove(item)
                return db
        return "No existe este item"



