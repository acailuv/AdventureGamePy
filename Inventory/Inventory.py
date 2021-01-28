class Inventory:
    def __init__(self):
        self.items = {}
        # Key is item.name
        # Value is [item, quantity]

    def add_item(self, item):
        if item.name not in self.items:
            self.items[item.name] = [item, 1]
        else:
            self.items[item.name][1] += 1

    def remove_item(self, item):
        if item.name not in self.items:
            self.items[item.name] = 1
        else:
            self.items[item.name] -= 1
