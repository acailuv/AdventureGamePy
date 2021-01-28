import pytest

import sys
sys.path.insert(0, '../Item')

from Item import Item
from HealingItem import HealingItem
from SupportItem import SupportItem

sys.path.insert(0, '../Player')

from Player import Player

player = Player("DUMMY")

def test_item():
    item = Item("DUMMY_ITEM", "DUMMY_DESC")
    assert item.name == "DUMMY_ITEM"
    assert item.desc == "DUMMY_DESC"

def test_healing_item():
    potion = HealingItem("POTION", "DRINK = HEAL M8", "hp", 2)
    mana_potion = HealingItem("MANA POTION", "DRINK = MANA HEAL M8", "mp", 2)
    poison = HealingItem("POISON", "DRINK = OUCHIES", "hp", -1)
    mana_poison = HealingItem("MANA POISON", "DRINK = MANA OUCHIES", "mp", -1)
    assert potion.name == "POTION"
    assert potion.desc == "DRINK = HEAL M8"
    assert potion.healing_type == "hp"
    assert potion.amount == 2
    
    player.hp -= 5
    player.mp -= 5
    
    potion.use(player)
    assert player.hp == 7

    poison.use(player)
    assert player.hp == 6

    mana_potion.use(player)
    assert player.mp == 7

    mana_poison.use(player)
    assert player.mp == 6

def test_support_item():
    might_seed = SupportItem("Might Seed", "idk but atk+", "attack", 3, 3)
    adamant_seed = SupportItem("Adamant Seed", "idk but def+", "defense", 3, 3)
    mega_nutrition = SupportItem("Mega Nutrition", "idk but max_hp+", "max_hp", 3, 3)
    ration = SupportItem("Ration", "idk but sta- I mean mp+", "max_mp", 3, 3)
    assert might_seed.name == "Might Seed"
    assert might_seed.desc == "idk but atk+"
    assert might_seed.support_type == "attack"
    assert might_seed.amount == 3
    assert might_seed.turns == 3

    might_seed.use(player)
    assert player.attack == 4

    adamant_seed.use(player)
    assert player.defense == 4

    mega_nutrition.use(player)
    assert player.max_hp == 13

    ration.use(player)
    assert player.max_mp == 13
