class Equipment:

    def __init__(self, name, desc, effect):
        self.name = name
        self.desc = desc
        self.effect = effect

        if effect.__class__.__name__ != "defaultdict":
            raise Exception("Effect has invalid data type:", effect.__class__.__name__, "Expected: defaultdict")

    def apply_effect(self, target):
        target.max_hp += self.effect["max_hp"]
        target.max_mp += self.effect["max_mp"]
        target.attack += self.effect["attack"]
        target.defense += self.effect["defense"]
    
    def deapply_effect(self, target):
        target.max_hp -= self.effect["max_hp"]
        target.max_mp -= self.effect["max_mp"]
        target.attack -= self.effect["attack"]
        target.defense -= self.effect["defense"]
