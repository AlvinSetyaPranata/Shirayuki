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

TEMPLATES = {
    "AUTO-ITEMS" : (3, 62),
    "BAG" : (8, 62),
    "PRESENT" : (13, 62)
}

hwnd = FindWindowEx(None, None, None, "ToramOnline")

x, y, w, h = GetWindowRect(hwnd)
w = w - x
h = h - y


left = x +  7
top = y + 30
bottom = top + h - 35
right = left + w - 15
inner_width = right - left
inner_height = bottom - top

mid_x = (inner_width // 2)
mid_y = (inner_height // 2)



def click(pos_x, pos_y):
    # Click to specific coordinate

    pos_x = left + pos_x
    pos_y = top + pos_y

    if pos_x < left and pos_x > right:
        return

    elif pos_y > bottom and pos_y < top:
        return
    
    gui.moveTo(pos_x, pos_y)
    gui.click()


def get_relative_pos(relX, relY):
    pos_x = round(relX / 100 * inner_width) + left
    pos_y = round(relY / 100 * inner_height) + top

    if pos_x < left and pos_x > right:
        return False, False

    elif pos_y > bottom and pos_y < top:
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


def grab_image(img_src):
    image = np.array(IG.grab(bbox=(left, top, right, bottom)))
    

    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    temp_ = cv2.imread(img_src, 0).copy()

    
    res =  cv2.matchTemplate(image, temp_, cv2.TM_CCOEFF_NORMED)

    threshold = 0.8
    coord = np.where(res >= threshold)

    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)


    temp_height, temp_width = temp_.shape

    loc = (max_loc[0] + (temp_width // 2), max_loc[1] + (temp_height // 2))

    click(*loc)
    

def get_interval(custom_time=(0.8, 0.9, 1)):
    return random.choice(custom_time)





    


