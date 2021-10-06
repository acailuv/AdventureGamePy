import sys
sys.path.insert(0, '../Utils')

from Utils import Constants # pylint: disable=import-error

class Equipment:

    def __init__(self, name, desc, effect):
        self.name = name
        self.desc = desc
        self.effect = effect

        if effect.__class__.__name__ != 'defaultdict':
            raise Exception('Effect has invalid data type:', effect.__class__.__name__, 'Expected: defaultdict')

    def apply_effect(self, target):
        target.max_hp += self.effect[Constants.Statuses.MAX_HP]
        target.max_mp += self.effect[Constants.Statuses.MAX_MP]
        target.attack += self.effect[Constants.Statuses.ATTACK]
        target.defense += self.effect[Constants.Statuses.DEFENSE]
    
    def deapply_effect(self, target):
        target.max_hp -= self.effect[Constants.Statuses.MAX_HP]
        target.max_mp -= self.effect[Constants.Statuses.MAX_MP]
        target.attack -= self.effect[Constants.Statuses.ATTACK]
        target.defense -= self.effect[Constants.Statuses.DEFENSE]
