import sys

sys.path.insert(0, '../Location')

from Location import Location # pylint: disable=import-error
from Inn import Inn # pylint: disable=import-error
from Shop import Shop # pylint: disable=import-error

sys.path.insert(0, '../Player')

from Player import Player # pylint: disable=import-error

sys.path.insert(0, '../Item')

from Item import Item # pylint: disable=import-error

player = Player('DUMMY')

def test_location():
    loc = Location('LOCATION 01', 'DESCRIPTION')
    assert loc.name == 'LOCATION 01'
    assert loc.desc == 'DESCRIPTION'

    loc.enter(player)
    assert player.location == loc

def test_inn():
    player.hp = 5
    player.mp = 5
    player.gold = 100

    inn = Inn('INN', 'INN DESC', 10)
    inn.rent(player)

    assert player.hp == player.max_hp
    assert player.mp == player.max_mp
    assert player.gold == 90

    player.hp = 5
    player.mp = 5

    # Not enough gold
    inn2 = Inn('INN 2', 'INN DESC 2', 1000)
    inn2.rent(player)

    assert player.hp == 5
    assert player.mp == 5
    assert player.gold == 90

def test_shop():
    item = Item('DUMMY_ITEM', 'ITEM DESC', 100)
    player.gold = 100

    shop_catalog = {
        item.name: [item, item.price]
    }
    shop = Shop('DUMMY_SHOP', 'SHOP DESC', shop_catalog)
    shop.buy(player, item)

    assert player.inventory.item_exist(item)
    assert player.gold == 0

    player.inventory.remove_item(item, 1)
    player.inventory.add_item(item, 1)
    shop.sell(player, item)

    assert player.inventory.items[item.name][1] == 0
    assert player.gold == 100

    player.gold = 0
    player.inventory.add_item(item, 10)
    shop.sell(player, item,  10)

    assert player.inventory.items[item.name][1] == 0
    assert player.gold == 1000

    shop.buy(player, item, 10)

    assert player.inventory.items[item.name][1] == 10
    assert player.gold == 0
