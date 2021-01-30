import sys
sys.path.insert(0, '../Combat')
sys.path.insert(0, '../Monster')
sys.path.insert(0, '../Player')

from Combat import Combat
from Monster import Monster
from Player import Player

Character = Player("Adventurer")
GoblinA = Monster("GoblinA", 5, 5, 1, 0, [], {})
GoblinB = Monster("GoblinB", 5, 5, 1, 0, [], {})
GoblinC = Monster("GoblinC", 5, 5, 1, 0, [], {})
Monsters = [GoblinA, GoblinB, GoblinC]

Battle = Combat(Character, Monsters)
Battle.begin_combat()