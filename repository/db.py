from pydoc import cli
from flask import g
from mongoengine import connect
from repository.models import Items
""" Crea un comando """
import click
from flask.cli import with_appcontext



defaultItems = [
    {
        "name": "Aged Brie",
        "sell_in": 2,
        "quality": 0,
    },
    {
        "name": "+5 Dexterity Vest",
        "sell_in": 10,
        "quality": 20,
    },
    {
        "name": "Elixir of the Mongoose",
        "sell_in": 5,
        "quality": 7,
    },
    {
        "name": "Sulfuras, Hand of Ragnaros",
        "sell_in": 0,
        "quality": 80,
    },
    {
        "name": "Sulfuras, Hand of Ragnaros",
        "sell_in": -1,
        "quality": 80,
    },
    {
        "name": "Backstage Pass",
        "sell_in": 15,
        "quality": 20,
    },
    {
        "name": "Backstage Pass",
        "sell_in": 10,
        "quality": 49,
    },
    {
        "name": "Backstage Pass",
        "sell_in": 5,
        "quality": 49,
    },
    {
        "name": "Conjured Mana Cake",
        "sell_in": 3,
        "quality": 6,
    },
]


""" Da acceso a al abase de datos  """
def getDb():
    if 'db' not in g:
        g.db = connect(
            db = 'items',
            host = 'mongodb+srv://items:items@items.ozyma.mongodb.net/myFirstDatabase?retryWrites=true&w=majority'
            )
        g.Items = Items
        return g.db

""" Iniciar la base de datos y poblarlo """
def initDb():
    db = getDb()
    Items.drop_collection()
    for item in defaultItems:
        Items(
            name = item['name'],
            sell_in = item['sell_in'],
            quality = item['quality']
        ).save() 
        """ .save() : es una función guarda el objeto que hay en momoria en la base de dados  """

@click.command('initDB')
@with_appcontext
def initDbConmmand():
    initDb()
    click.echo('La base de datos se ha poblado bien')

def close_db():
    db = g.pop('db', None)

    if db is not None:
        db.close()

def initApp(app):
    app.cli.add_command(initDbConmmand)
    
