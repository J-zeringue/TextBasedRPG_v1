from character import*
import random
import math
def main():
    run = True

    while run:
        print('Welcome, are you ready to create your character and cross the Holy Desert Raraku in search of the fabled house of the Azath Tremorlor?')
        start_game = input('Press y to proceed to character creation. Press n to exit:')
        if start_game == 'n':
            run = False
        else:
            name = input('Enter your name: ')
            player_character = Character(name)
            player_character.allocate_start_stats()







main()