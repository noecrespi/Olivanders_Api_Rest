from mongoengine import StringField, IntField, Document


class Items(Document):
    name = StringField(required=True)
    sell_in = IntField()
    quality = IntField()
