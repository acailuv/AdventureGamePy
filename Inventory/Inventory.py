class Inventory:

    def __init__(self):
        self.items = {}
        # Key is item.name
        # Value is [item, quantity]
    
    def item_exist(self, item):
        if item.name in self.items:
            return True
        else:
            return False
    
    def item_sufficient(self, item, amount):
        if self.item_exist(item):
            if self.items[item.name][1] >= amount:
                return True
            else:
                return False
        else:
            return False

    def add_item(self, item, amount=1):
        if not self.item_exist(item):
            self.items[item.name] = [item, amount]
        else:
            self.items[item.name][1] += amount

    def remove_item(self, item, amount=1):
        if not self.item_exist(item):
            raise Exception("There is not any", item.name, "in the inventory to remove.")
        else:
            if self.item_sufficient(item, amount):
                self.items[item.name][1] -= amount
