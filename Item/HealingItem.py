from Item import Item

class HealingItem(Item):

    def __init__(self, name, desc, healing_type, amount):
        super().__init__(name, desc)
        self.healing_type = healing_type
        self.amount = amount
    
    def use(self, target):
        if self.healing_type == "hp":
            target.hp += self.amount
        elif self.healing_type == "mp":
            target.mp += self.amount
        else:
            raise Exception("Healing type is invalid.")
