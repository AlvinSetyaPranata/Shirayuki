import pyautogui as gui
from win32gui import FindWindowEx, GetWindowRect, SetForegroundWindow, SetWindowPos
import numpy as np
from PIL import ImageGrab as IG
import cv2
from time import sleep
import random



__all__ = [
    "smith"
]

TEMPLATES = {
    "AUTO-ITEMS" : (3, 62),
    "BAG" : (8, 62),
    "PRESENT" : (13, 62)
}

# CONSTANS
EMPTY_SLOT_TEMP = cv2.imread("..\\assets\\empty_slot.png")


hwnd = FindWindowEx(None, None, None, "ToramOnline")

x, y, w, h = GetWindowRect(hwnd)
w = w - x
h = h - y

# Window border excluded

left = x +  7
top = y + 30
bottom = top + h - 35
right = left + w - 15
innerW = right - left
innerH = bottom - top

midX = (innerW // 2)
midY = (innerH // 2)
_flag_interrupt = 0

def click(posX, posY):
    # Click to specific coordinate

    posX = left + posX
    posY = top + posY

    if posX < left and posX > right:
        return

    elif posY > bottom and posY < top:
        return
    
    gui.moveTo(posX, posY)
    gui.click()


def getRelativePos(relX, relY):
    posX = round(relX / 100 * innerW) + left
    posY = round(relY / 100 * innerH) + top

    if posX < left and posX > right:
        return False, False

    elif posY > bottom and posY < top:
        return False, False

    return posX, posY


def clickRelative(relX, relY):
    # Click to specific coordinate using percentage
    """
    for eg:

    relX = 20 => 20% of innerScreenWidth
    relY = 30 => 30% of innerScreenHeight
    """

    posX, posY = getRelativePos(relX, relY)

    if not posX:
        return

    gui.moveTo(posX, posY, 0.8)

    sleep(0.4)
    
    gui.click()


def grabImage(img_src):
    image = np.array(IG.grab(bbox=(left, top, right, bottom)))
    

    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    temp_ = cv2.imread(img_src, 0).copy()

    
    res =  cv2.matchTemplate(image, temp_, cv2.TM_CCOEFF_NORMED)

    threshold = 0.8
    coord = np.where(res >= threshold)

    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

    print(max_val)

    temp_h, temp_w = temp_.shape

    loc = (max_loc[0] + (temp_w // 2), max_loc[1] + (temp_h // 2))


    click(*loc)

def getInterval():
    return random.choice((0.8, 0.9, 1))


def auto_gift(max_mats):
    for _ in range(max_mats):
        grabImage("..\\assets\\sendgift.png")
        sleep(0.8)
        grabImage("..\\assets\\selectplayer.png")
        sleep(0.8)
        grabImage("..\\assets\\player_gift_list\\hayasaka_ai.png")
        sleep(0.8)
        grabImage("..\\assets\\selectgift.png")
        sleep(0.8)
    
        clickRelative(55, 25)
        clickRelative(55, 25)
        sleep(getInterval())
        clickRelative(72, 45)
        sleep(getInterval())
        clickRelative(55, 75)
        sleep(getInterval())
        clickRelative(28, 43)
        sleep(getInterval())
        grabImage("..\\assets\\sendgift2.png")
        sleep(getInterval())
        grabImage("..\\assets\\ok.png")
        sleep(getInterval())

def is_empty(posX, posY):
    posX, posY = getRelativePos(posX, posY)

    if not posX:
        return
    
    image = np.array(IG.grab(bbox=(posX -35, posY - 35, posX, posY)))
    temp_ = np.array(EMPTY_SLOT_TEMP).copy()

    res =  cv2.matchTemplate(image, temp_, cv2.TM_CCOEFF_NORMED)

    threshold = 0.8
    coord = np.where(res >= threshold)

    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

    

def auto_claim_gift(max_gift):
    grabImage("..\\assets\\checkgift.png")
    sleep(getInterval())
    
    for _ in range(max_gift):
        grabImage("..\\assets\\receive_gift.png")
        sleep(getInterval())
        grabImage("..\\assets\\receive_gift2.png")
        sleep(getInterval())
        



# Monitoring keyboard

def on_press(key):
    global _flag_interrupt
    
    if key == keyboard.Key.f4:
        _flag_interrupt = 1
        return False


def auto_proc(max_mats):
    clickRelative(38, 34)

    
    y = 25
    x = 55
    # 25, 43, 61, 79, 97

    for _ in range(max_mats):

        
        if _flag_interrupt == 1:
            return

        
        if is_empty(x, y):
            continue
        
        clickRelative(x, y)


        x += 10

        if x == 105:
            x = 55
            y += 18

        if y == 97:
            y = 43

            gui.scroll(-100)
            gui.scroll(-100)
            gui.scroll(-100)
            gui.scroll(-100)
            gui.scroll(-100)
            gui.scroll(-100)
            gui.scroll(-100)
            gui.scroll(-100)


    
    clickRelative(23, 34)

    clickRelative(50, 80)
    clickRelative(50, 80)


#auto_claim_gift(17)
#auto_proc(38)
