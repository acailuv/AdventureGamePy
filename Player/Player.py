import sys
sys.path.insert(0, '../Inventory')

from Inventory import Inventory

class Player:

    def __init__(self, name):
        self.name = name
        self.level = 1
        self.max_hp = 10
        self.hp = 10
        self.max_mp = 10
        self.mp = 10
        self.attack = 1
        self.defense = 1

        # Inventory
        self.inventory = Inventory()

        # Equipment slots
        self.armor = None
        self.weapon = None
