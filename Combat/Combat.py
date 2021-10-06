class Combat:
    def __init__(self, player, enemies):
        self.player = player

        # Enemies is expected to be a list of enemies
        # [enemy1, enemy2, ...]
        self.enemies = enemies

        self.valid_actions = ['attack', 'skill', 'inventory', 'escape']

    def begin_combat(self):
        turn = 0
        while not self.check_finished():
            if turn % 2 == 0: # Even turns are player turns
                action = ''
                while not self.check_valid_action(action):
                    self.print_valid_actions()
                    action = input().lower().strip()

                if action == self.valid_actions[0]:
                    print('\nRemaining enemies:')
                    for i in range(len(self.enemies)):
                        print('{}. {}'.format(i+1, self.enemies[i].name))
                    
                    target = 0
                    while not 1 <= target <= len(self.enemies):
                        target = input('Select target: ')
                        if not target.isdigit():
                            target = 0
                        else:
                            target = int(target)
                    # Convert starting target from 1 to 0 for list lookup
                    target = target - 1

                    # Temporary damage calculation: max(player attack - enemy defense, 1)
                    damage_dealt = max(self.player.attack - self.enemies[target].defense, 1)
                    self.enemies[target].damage(damage_dealt)
                    print('\nYou dealt {} damage to {}'.format(damage_dealt, self.enemies[target].name))
                    if self.enemies[target].hp <= 0:
                        print('{} has been defeated!'.format(self.enemies[target].name))
                        del self.enemies[target] # Enemy died, remove from list
                    
                elif action == self.valid_actions[1]:
                    print('TODO: Implement skills')
                elif action == self.valid_actions[2]:
                    print('TODO: Implement Inventory')
                elif action == self.valid_actions[3]:
                    break
                
            else: # Odd turns are enemy turns
                for enemy in self.enemies:
                    # Temporary damage calculation: max(enemy attack - player defense, 1)
                    damage_dealt = max(enemy.attack - self.player.defense, 1)
                    # Player has no take damage function (yet?)
                    self.player.hp = max(0, self.player.hp - damage_dealt)
                    print('{} dealt {} damage to you!'.format(enemy.name, damage_dealt))
                    if self.player.hp <= 0: break
                    
            turn += 1

        if self.player.hp <= 0:
            print('Defeat...')
        elif not self.check_finished():
            print('You ran away...')
        else:
            print('You are victorious!')
            # Give out Experience/Money/Loot
        
    def check_finished(self):
        # Returns true if player or all enemies health <= 0
        if self.player.hp <= 0: return True

        # for enemy in self.enemies:
        #     print(enemy.name, enemy.hp)

        for enemy in self.enemies:
            if enemy.hp > 0:
                return False # one of the enemies are still alive
        return True

    def check_valid_action(self, action):
        if action in self.valid_actions:
            return True
        else:
            return False
    
    def print_valid_actions(self):
        print('\nWhat will you do?')
        print('Your health: {}/{}'.format(self.player.hp, self.player.max_hp))
        print('Valid actions: {}'.format(', '.join(self.valid_actions)))
