import cv2
from os.path import isfile
import numpy as np
import pyautogui as gui
from time import sleep
from win32gui import FindWindow, GetWindowRect


def locate_coordinate(image_name):
        temp_ = cv2.imread(image_name, 0).copy()
        image = cv2.imread("D:\\temp-projects\\gabut\\Toram Bot\\auto-refine\\assets\\testing_switch_char2.png", 0).copy()
        #image = np.array(ImageGrab.grab(all_screens=True))
        cv2.imshow('Results', image)

        w_handle = FindWindow(None, "Results")
        x, y, win_w, win_h = GetWindowRect(w_handle)

        res = cv2.matchTemplate(image, temp_, cv2.TM_CCOEFF_NORMED)

        threshold = 0.8
        coord = np.where(res >= threshold)

        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

        w = temp_.shape[1]
        h = temp_.shape[0]

        loc = max_loc
        #mid = (x + win_w, y + win_h)
        #mid = ((loc[0] + 2), (loc[1] + h))
        #mid = (x, y)
        
        #gui.moveTo(*mid)
        bot_right = (max_loc[0] + w, max_loc[1] + h)
        cv2.rectangle(image, loc, bot_right, 255, 5)
        

        cv2.imshow('Results', image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        


def test(image_name):
    print(isfile(image_name))
    
    image = cv2.imread(image_name, 0)

    cv2.imshow('Results', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()



locate_coordinate("D:\\temp-projects\\gabut\\Toram Bot\\auto-refine\\assets\\6.png")

