import pytest

import sys
sys.path.insert(0, '../Player')
sys.path.insert(0, '../Item')

from Item import Item
from HealingItem import HealingItem
from SupportItem import SupportItem
from Player import Player

player = Player("DUMMY")

def test_item_inventory():
    item = Item("DUMMY_ITEM", "DUMMY_DESC")
    player.inventory.add_item(item)
    assert player.inventory.items[item.name][0].name == "DUMMY_ITEM"
    assert player.inventory.items[item.name][0].desc == "DUMMY_DESC"
    assert player.inventory.items[item.name][1] == 1
