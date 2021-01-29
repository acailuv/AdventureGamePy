class Combat:
    def __init__(self, player, enemies):
        self.player = player

        # Enemies is expected to be a list of enemies
        # [enemy1, enemy2, ...]
        self.enemies = enemies

        self.valid_actions = ["attack", "defend", "skill"]

    def begin_combat(self):
        turn = 0
        while not check_finished():
            if turn % 2 == 0: # Even turns are player turns
                action = ''
                while not self.check_valid_action(action):
                    print_valid_actions()
                    action = input()
                if action == self.valid_actions[0]:
                    print("Remaining enemies:")
                    for enemy in self.enemies:
                        print(enemy.name)
                    target = 0
                    while not 1 <= target <= len(self.enemies):
                        target = input("Select target: ")
                    # Temporary damage calculation: max(player attack - enemy defence, 1)
                    damage_dealt = max(self.player.attack - self.enemies[target].defence, 1)
                    self.enemies[target].damage(damage_dealt)
                    if self.enemies[target].hp <= 0:
                        del self.enemies[target]
                elif action == self.valid_actions[1]:
                    print("TODO: Implement defend")
                elif action == self.valid_actions[2]:
                    print("TODO: Implement skills")
            else: # Odd turns are enemy turns
                pass
            turn += 1
        
    def check_finished(self):
        # Returns true if player or all enemies health <= 0
        if self.player.hp <= 0: return True
        for enemy in self.enemies:
            if enemy.hp > 0:
                return False # one of the enemies are still alive
        return True

    def check_valid_action(self, action):
        if action.lower().strip() in self.valid_actions:
            return True
        else:
            return False
    
    def print_valid_actions(self):
        print("What will you do?")
        print("Valid actions: {}".format(','.join(self.valid_actions)))
