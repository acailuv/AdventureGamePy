import sys
sys.path.insert(0, '../Utils')

from Utils import Constants # pylint: disable=import-error
from Item import Item

class HealingItem(Item):

    def __init__(self, name, desc, price, healing_type, amount):
        super().__init__(name, desc, price)
        self.healing_type = healing_type
        self.amount = amount
    
    def use(self, target):
        if self.healing_type == Constants.Statuses.HP:
            target.hp = min(target.max_hp, target.hp + self.amount)
        elif self.healing_type == Constants.Statuses.MP:
            target.mp = min(target.max_mp, target.mp + self.amount)
        else:
            raise Exception('Healing type is invalid.')
