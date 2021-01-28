from Equipment import Equipment

class Armor(Equipment):

    def __init__(self, name, desc, effect):
        super().__init__(name, desc, effect)       
    
    def equip(self, target):
        target.armor = self
        self.apply_effect(target)

    def unequip(self, target):
        target.armor = None
        self.deapply_effect(target)