from Location import Location

class Inn(Location):

    def __init__(self, name, desc):
        super().__init__(name, desc)

    def rent(self, target, price):
        if target.sufficient_funds(price):
            target.hp = target.max_hp
            target.mp = target.max_mp
            target.gold -= price
