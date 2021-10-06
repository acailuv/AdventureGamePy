from Equipment import Equipment

class Weapon(Equipment):

    def __init__(self, name, desc, effect):
        super().__init__(name, desc, effect)
    
    def equip(self, target):
        target.weapon = self
        self.apply_effect(target)

    def unequip(self, target):
        target.weapon = None
        self.deapply_effect(target)