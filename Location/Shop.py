from Location import Location

class Shop(Location):

    def __init__(self, name, desc, catalog):
        super().__init__(name, desc)

        self.catalog = catalog
        # catalog = dictionary
        # { item_name : [item_obj, price] }

    def buy(self, target, item, amount=1):
        if item.name not in self.catalog:
            raise Exception('Item:', item.name, 'is not registered at this shop')
        else:
            if target.sufficient_funds(self.catalog[item.name][1] * amount):
                target.inventory.add_item(item, amount)
                target.gold -= self.catalog[item.name][1] * amount
    
    def sell(self, target, item, amount=1):
        if not target.inventory.item_sufficient(item, amount):
            raise Exception('Item does not exist in player inventory: ', item.name)
        else:
            target.inventory.remove_item(item, amount)
            target.gold += item.price * amount
            print('Item:', item.name, 'is sold for:', item.price * amount, 'gold pieces')
