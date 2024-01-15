"""
NOTE: This contains all of keyboard functionality that used to controll the player


MAPPING STRUCTURES:

map must be itterable that contains an array which includes the direction
W ( Forward ), S ( Backward ), A ( Left ), D ( Right ).

and the second value is the duration of how long that direction is being held in
seconds

[('W', 2), ('S', 5)]

"""

from pyautogui import hold as keyboard_hold, sleep
from .base import *


# Constans 
FORWARD = 'W'
LEFT = 'A'
RIGHT = 'D'
BACKWARD = 'S'


def load_map(file):
    if not os.isfile(file):
        return "No file found"


    return json.load(file)


def controll_from_map(maps):
    # Controll the player from given map
    sleep(3)

    for coord in maps:
        if not coord[0] in (FORWARD, LEFT, RIGHT, BACKWARD):
            return f"Unknown Direction {coord[0]}!"

        with keyboard_hold(coord[0]):
            sleep(coord[1])


def switch_character(id):
    '''
    ID begin from 1
    coordinate = 75 (x), 23 + 14 * id - 1
    '''
    # Open menu
    press('p')

    # Switch Character button
    click_relative(80, 80)  


    # Char character button
    click_relative(75, 23 + 14 * (id - 1))

    # Switch Character
    click_relative(20, 90)


def exit_game():
    press("ESC")
    click_relative(50, 83)
    click_relative(60, 83)



def goto_ex_skill():
    press("p")
    click_relative(75,  38)
    click_relative(75, 25)
    click_relative(20, 25)
    click_relative(50, 55)