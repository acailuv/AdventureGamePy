import sys
sys.path.insert(0, '../Inventory')

from Inventory import Inventory

class Player:

    def __init__(self, name):
        # Stats
        self.name = name
        self.level = 1
        self.max_hp = 10
        self.hp = 10
        self.max_mp = 10
        self.mp = 10
        self.attack = 1
        self.defense = 1

        # Currency
        self.gold = 0

        # Inventory
        self.inventory = Inventory()

        # Equipment slots
        self.armor = None
        self.weapon = None

        # Location
        self.location = None
    
    def sufficient_funds(self, amount, print_notification=True):
        if self.gold >= amount:
            return True
        else:
            if (print_notification):
                print("Insufficient Funds")
            return False
