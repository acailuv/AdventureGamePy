class Monster:
    def __init__(self, name, hp, max_hp, attack, defence, loot):
        self.name = name
        self.max_hp = max_hp
        self.hp = hp
        self.attack = attack
        self.defence = defence

        # Loot can be either a list or a dict (for probability drops)
        self.loot = loot
    
    def damage(self, damage):
        self.hp = self.hp - damage

    def heal(self, healing):
        self.hp = max(self.max_hp, self.hp + healing)
    