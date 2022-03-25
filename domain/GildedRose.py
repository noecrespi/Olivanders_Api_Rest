class Updateable():

    def updateQuality(self):
        pass
    
class Item(Updateable):

    """ NO instancia los objetos, en este caso se usa como contructor """
    def __init__(self, name, sellIn, quality):
        self.name = name
        self.sellIn = sellIn
        self.quality = quality

    def recalcularQuality(self, cantidad):
        if self.quality + cantidad >= 0:
            self.quality += cantidad
        else: 
            self.quality = 0 
    
class NormalItem(Item):
    
    """ Constructor del padre (Item) """
    def __init__(self, name, sellIn, quality):
        Item.__init__(self, name, sellIn, quality)
    
    def updateQuality(self):
        if self.sellIn <= 0:
            self.recalcularQuality(-2)
        else:
            self.recalcularQuality(-1)
        self.sellIn -= 1
    
class Conjured(Item):
    
    def __init__(self, name, sellIn, quality):
        Item.__init__(self, name, sellIn, quality)

    def updateQuality(self):
        if self.sellIn <= 0:
            self.recalcularQuality(-4)
        else:
            self.recalcularQuality(-2)
        self.sellIn -= 1

class Sulfuras(Item):

    def __init__(self, name, sellIn, quality):
        Item.__init__(self, name, sellIn, quality)

    def updateQuality(self):
        pass

class Backstage(Item):

    def __init__(self, name, sellIn, quality):
        Item.__init__(self, name, sellIn, quality)

    def updateQuality(self):
        if self.sellIn >= 10:
            self.recalcularQuality(-1)
        elif self.sellIn < 10: 
            self.recalcularQuality(-2)
        elif self.sellIn < 5: 
            self.recalcularQuality(-3)
        else:
            self.quality = 0
        self.sellIn -= 1 

class AgedBrie(Item):

    def __init__(self, name, sellIn, quality):
        Item.__init__(self, name, sellIn, quality)

    def updateQuality(self):
        if self.sellIn <= 0:
            self.recalcularQuality(2)
        else:
            self.recalcularQuality(1)
        self.sellIn -= 1
