"""
DESC:

Files that includes all function related to eyes of the bot
"""

import pyautogui as gui
from PIL import ImageGrab as IG
from time import sleep
from win32gui import FindWindowEx, GetWindowRect, SetForegroundWindow, SetWindowPos
import numpy as np
import cv2
import random



# CONSTANS



hwnd = FindWindowEx(None, None, None, "ToramOnline")

x, y, w, h = GetWindowRect(hwnd)
w = w - x
h = h - y


LEFT = x +  7
TOP = y + 30
BOTTOM = TOP + h - 35
RIGHT = LEFT + w - 15
inner_width = RIGHT - LEFT
inner_height = BOTTOM - TOP

mid_x = (inner_width // 2)
mid_y = (inner_height // 2)



def click(pos_x, pos_y):
    # Click to specific coordinate using absolute position

    pos_x = LEFT + pos_x
    pos_y = TOP + pos_y

    if pos_x < LEFT and pos_x > RIGHT:
        return

    elif pos_y > BOTTOM and pos_y < TOP:
        return
    
    gui.moveTo(pos_x, pos_y)
    gui.click()


def get_relative_pos(relX, relY):
    # Click to speciific coordinate using relative position
    
    pos_x = round(relX / 100 * inner_width) + LEFT
    pos_y = round(relY / 100 * inner_height) + TOP

    if pos_x < LEFT and pos_x > RIGHT:
        return False, False

    elif pos_y > BOTTOM and pos_y < TOP:
        return False, False

    return pos_x, pos_y


def click_relative(relX, relY):
    # Click to specific coordinate using percentage
    """
    for eg:

    relX = 20 => 20% of innerScreenWidth
    relY = 30 => 30% of innerScreenHeight
    """

    pos_x, pos_y = get_relative_pos(relX, relY)

    if not pos_x:
        return

    gui.moveTo(pos_x, pos_y, 0.8)

    sleep(0.4)
    
    gui.click()



def get_interval(custom_time=(0.8, 0.9, 1)):
    return random.choice(custom_time)


def get_pos_by_dim():
    click_relative(29, 90)
    print("Waiting to complete process...")
    sleep(5)
    click_relative(45, 78)


def press(key):
    gui.press(key)