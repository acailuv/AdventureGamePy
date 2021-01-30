from Location import Location

class Inn(Location):

    def __init__(self, name, desc, price):
        super().__init__(name, desc)
        self.price = price

    def rent(self, target):
        if target.sufficient_funds(self.price):
            target.hp = target.max_hp
            target.mp = target.max_mp
            target.gold -= self.price
