import pytest

import sys
sys.path.insert(0, '../Player')
sys.path.insert(0, '../Item')

from Item import Item # pylint: disable=import-error
from HealingItem import HealingItem # pylint: disable=import-error
from SupportItem import SupportItem # pylint: disable=import-error
from Player import Player # pylint: disable=import-error

player = Player('DUMMY')

def test_item_inventory():
    item = Item('DUMMY_ITEM', 'DUMMY_DESC', 0)
    player.inventory.add_item(item)
    assert player.inventory.items[item.name][0].name == 'DUMMY_ITEM'
    assert player.inventory.items[item.name][0].desc == 'DUMMY_DESC'
    assert player.inventory.items[item.name][1] == 1

    player.inventory.remove_item(item)
    assert player.inventory.items[item.name][1] == 0

    try:
        # No item in the inventory to remove
        player.inventory.remove_item(Item('A', 'B'))
        assert False
    except:
        assert True
