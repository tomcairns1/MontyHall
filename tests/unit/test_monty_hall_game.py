#!usr/bin/env python3
''' Test suite for the monty_hall_game.py script '''

from monty_hall_game import random_choice, open_door, change_choice


def test_random_choice():
    ''' Function to test random_choice '''
    possible_values = [1, 2, 3]

    # Test
    test_val = random_choice()
    assert test_val in possible_values


def test_open_door_chose_car():
    ''' Function to test which door to open if car == contestant's choice '''
    car = 1
    contestant_choice = 1
    possible_values = [2, 3]
    door = open_door(car, contestant_choice)

    # test
    assert door in possible_values


def test_open_door_did_not_choose_car():
    ''' Function to test door to open if car != contestant's choice '''
    # test 1
    car = 1
    contestant_choice = 3
    door = open_door(car, contestant_choice)
    assert door == 2

    # test 2
    car = 2
    contestant_choice = 1
    door = open_door(car, contestant_choice)
    assert door == 3


def test_change_choice():
    ''' Function to test the change of door '''
    contestant_choice = 1
    door = 2
    new_choice = change_choice(contestant_choice, door)

    assert new_choice == 3
