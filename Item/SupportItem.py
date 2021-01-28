from Item import Item

class SupportItem(Item):

    def __init__(self, name, desc, support_type, amount, turns):
        super().__init__(name, desc)
        self.support_type = support_type
        self.amount = amount
        self.turns = turns
    
    def calculate_max_delta(self, max_value):
        new_max_value = max_value + self.amount
        delta = new_max_value - max_value
        return new_max_value, delta

    def use(self, target):
        if self.support_type == "max_hp":
            new_max_hp, delta = self.calculate_max_delta(target.max_hp)
            target.max_hp = new_max_hp
            target.hp += delta

        elif self.support_type == "max_mp":
            new_max_mp, delta = self.calculate_max_delta(target.max_mp)
            target.max_mp = new_max_mp
            target.mp += delta

        elif self.support_type == "attack":
            target.attack += self.amount

        elif self.support_type == "defense":
            target.defense += self.amount

        else:
            Exception("Support type is invalid.")