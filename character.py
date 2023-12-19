import random
import math

class Character():
    def __init__(self, name, level=1, strength=10, constitution=10, dexterity=10, wisdom=10, intelligence=10, focus=10):
        self.name = name
        self.level = level
        self.xp = 0
        self.xp_to_lvl = 100*self.level
        self.strength = strength
        self.constitution = constitution
        self.dexterity = dexterity
        self.wisdom = wisdom
        self.intelligence = intelligence
        self.focus = focus
        self.health = self.constitution*10
        self.mana = self.focus*10
        self.stamina = (self.strength + self.dexterity)//2

    # allocates initial base stat points
    def allocate_start_stats(self):
        points = 6
        while points > 0:
            print(f'1 - Strength = {self.strength}')
            print(f'2 - Constitution = {self.constitution}')
            print(f'3 - Dexterity = {self.dexterity}')
            print(f'4 - Wisdom = {self.wisdom}')
            print(f'5 - Intelligence = {self.intelligence}')
            print(f'6 - Focus = {self.focus}')
            user_in = input(f'You have {points} remaining, press the respective number to distribute 2 points the attribute: ')
            if user_in == '1':
                self.strength += 2
                points -= 2
            if user_in == '2':
                self.constitution += 2
                points -= 2           
            if user_in == '3':
                self.dexterity += 2
                points -= 2
            if user_in == '4':
                self.wisdom += 2
                points -= 2
            if user_in == '5':
                self.intelligence += 2
                points -= 2
            if user_in == '6':
                self.focus += 2
                points -= 2
            else:
                print("Enter a valid number")

    # updates health, mana and stamina derived from attributes
    def update_derived_stats(self):
        self.health = self.constitution*10
        self.mana = self.focus*10
        self.stamina = (self.strength + self.dexterity)//2
        self.xp_to_lvl = 100*self.level
    
    # checks xp and levels up character after a battle
    def level_up(self, xp_gained):
        self.xp += xp_gained
        if self.xp >= self.xp_to_lvl:
            self.level += 1
            self.update_derived_stats()

class Fighter(Character):
    def __init__(self, name):
        super().__init__(name, level=1, strength=10, constitution=10, dexterity=10, wisdom=10, intelligence=10, focus=10)

class Rogue(Character):
    def __init__(self, name):
        super().__init__(name, level=1, strength=10, constitution=10, dexterity=10, wisdom=10, intelligence=10, focus=10)

class Sorcerer(Character):
    def __init__(self, name):
        super().__init__(name, level=1, strength=10, constitution=10, dexterity=10, wisdom=10, intelligence=10, focus=10)

class Cleric(Character):
    def __init__(self, name):
        super().__init__(name, level=1, strength=10, constitution=10, dexterity=10, wisdom=10, intelligence=10, focus=10)
