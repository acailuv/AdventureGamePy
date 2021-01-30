from Location import Location

class Shop(Location):

    def __init__(self, name, desc, catalog):
        super().__init__(name, desc)

        self.catalog = catalog
        # catalog = dictionary
        # { item_obj : price }

    def buy(self, target, item):
        if item not in catalog:
            raise Exception("Item is not registered at this shop.")
        else:
            if target.sufficient_funds(self.catalog[item]):
                target.inventory.add_item(item)
                target.gold -= self.catalog[item]
            else:
                print("Insufficient Funds")
    
    def sell(self, target, item):
        if not target.inventory.item_exist(item):
            raise Exception("Item does not exist in player inventory: ", item, ".")
        else:
            pass
