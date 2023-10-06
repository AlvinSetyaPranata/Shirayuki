import pyautogui as gui
from win32gui import FindWindowEx, GetWindowRect, SetForegroundWindow, SetWindowPos
import numpy as np
from PIL import ImageGrab as IG
import cv2
from time import sleep

TEMPLATES = {
    "AUTO-ITEMS" : (3, 62),
    "BAG" : (8, 62),
    "PRESENT" : (13, 62)
}



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

def clickRelative(relX, relY):
    # Click to specific coordinate using percentage
    """
    for eg:

    relX = 20 => 20% of innerScreenWidth
    relY = 30 => 30% of innerScreenHeight
    """

    posX = round(relX / 100 * innerW) + left
    posY = round(relY / 100 * innerH) + top

    if posX < left and posX > right:
        return

    elif posY > bottom and posY < top:
        return

    gui.moveTo(posX, posY)
    gui.click()


def grabImage(img_src):
    image = np.array(IG.grab(bbox=(left, top, right, bottom)))
    

    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    temp_ = cv2.imread(img_src, 0).copy()

    
    res =  cv2.matchTemplate(image, temp_, cv2.TM_CCOEFF_NORMED)

    threshold = 0.8
    coord = np.where(res >= threshold)

    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

    if (int(max_val * 100) < 99):
        print("No match")

        return

    temp_h, temp_w = temp_.shape

    loc = (max_loc[0] + (temp_w // 2), max_loc[1] + (temp_h // 2))


    click(*loc)

def colorIdentification(image):
    #image = np.array(IG.grab(bbox=(left, top, right, bottom)))
    image = cv2.imread(image, 0).copy()

     
    #image = cv2.cvtColor(image, cv2.COLOR_RGB2HSV)

    """
    # lower mask (0-10)
    lower_red = np.array([0,50,50])
    upper_red = np.array([10,255,255])
    mask0 = cv2.inRange(image, lower_red, upper_red)

    # upper mask (170-180)
    lower_red = np.array([170,50,50])
    upper_red = np.array([180,255,255])
    mask1 = cv2.inRange(image, lower_red, upper_red)

    # join my masks
    mask = mask0+mask1

    color_image = cv2.bitwise_and(image, image, mask=mask)
    """
    
    cv2.imshow("results", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def auto_proc():
    pass
