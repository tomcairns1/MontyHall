#!/usr/bin/env python3
'''
File: monty_hall_game.py

This file is used to run one simulation of the Monty Hall game show

How to execute:
$ python3 monty_hall_game.py
'''
import random


def play_game():
    '''
    Function to play the game
    return win (boolean)
    '''
    # Choose car
    car = random_choice()

    # Contestant choice
    contestant_choice = random_choice()

    # Open the door
    door = open_door(car, contestant_choice)

    # Change contestant's choice
    final_choice = change_choice(contestant_choice, door)

    # Check if a win
    win = (final_choice == car)

    return win


def random_choice():
    '''
    Function to choose a random integer between 1 and 3
    return choice (int)
    '''
    choice = random.randint(1,3)

    return choice


def open_door(car, contestant_choice):
    '''
    Function to choose a door to open
    param car: the door the car is behind (int)
    param contestant_choice: the door the contestant chose (int)
    return door (int)
    '''
    list_of_options = [1, 2, 3]

    # Decide which door to open
    if car != contestant_choice:
        for val in range(1, 4):
            if val != car and val != contestant_choice:
                door = val

    # If the contestant chooses the door the car is behind initially
    else:
        list_of_options.remove(car)
        # Decide which of the two remaining doors to open
        choice = random.randint(0, 1)
        door = list_of_options[choice]

    return door


def change_choice(contestant_choice, door):
    '''
    Function to change the contestant's choice
    param contestant_choice: iniital choice (int)
    param door: the open door (int)
    return final_decision (int)
    '''
    choices = [1, 2, 3]

    # Retain the door not already chosen
    choices.remove(door)
    choices.remove(contestant_choice)

    return choices[0]
    

if __name__ == '__main__':
    win = play_game()
