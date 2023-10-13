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





controll_from_map([('W', 2), ('S', 5)])
