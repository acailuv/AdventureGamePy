import sys
sys.path.insert(0, '../Player')

from Player import Player

sys.path.insert(0, '../Equipment')

from Equipment import Equipment
from Armor import Armor
from Weapon import Weapon

from collections import defaultdict

player = Player("Player")

effects = defaultdict(int)
effects["max_hp"] = 1
effects["max_mp"] = 1
effects["attack"] = 1
effects["defense"] = 1

def test_equipment():
    equipment = Equipment("DUMMY_EQUIPMENT", "DUMMY_DESC", effects)
    assert equipment.name == "DUMMY_EQUIPMENT"
    assert equipment.desc == "DUMMY_DESC"
    assert equipment.effect == effects

def test_armor():
    armor = Armor("Chestplate", "ThinkThonkStronk", effects)
    armor.equip(player)
    assert player.armor == armor
    assert player.max_hp == 11
    assert player.max_mp == 11
    assert player.attack == 2
    assert player.defense == 2
    
    armor.unequip(player)
    assert player.armor == None
    assert player.max_hp == 10
    assert player.max_mp == 10
    assert player.attack == 1
    assert player.defense == 1

def test_weapon():
    weapon = Weapon("Sword", "SwishSwooshSlash", effects)
    weapon.equip(player)
    assert player.weapon == weapon
    assert player.max_hp == 11
    assert player.max_mp == 11
    assert player.attack == 2
    assert player.defense == 2
    
    weapon.unequip(player)
    assert player.weapon == None
    assert player.max_hp == 10
    assert player.max_mp == 10
    assert player.attack == 1
    assert player.defense == 1
