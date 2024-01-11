import cv2
import numpy as np
from PIL import ImageGrab as IG
from .base import get_relative_pos

def detect_color(image):

    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    lower_red = np.array([0, 100, 100])
    upper_red = np.array([10, 255, 255])

    mask1 = cv2.inRange(hsv_image, lower_red, upper_red)

    lower_red = np.array([160, 100, 100])
    upper_red = np.array([180, 255, 255])

    mask2 = cv2.inRange(hsv_image, lower_red, upper_red)

    color_mask = cv2.bitwise_or(mask1, mask2)


    result = cv2.bitwise_and(image, image, mask=color_mask)

    # cv2.imshow('Original Image', cv2.imread(image_path))

        

    # binary_result = cv2.cvtColor(result, cv2.COLOR_BGR2GRAY)
    # ret, binary_results = cv2.threshold(binary_result, 1, 255, cv2.THRESH_BINARY)

    # cv2.imshow('Red Color Detection Result', binary_result)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()



    return np.any(color_mask)


def grab_image_in(left, top, right, bottom):
    image = np.array(IG.grab(bbox=(*get_relative_pos(left, top), *get_relative_pos(right, bottom),)))
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # cv2.imshow('Results', image)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    return image


def grab_image(img_src):
    image = np.array(IG.grab(bbox=(LEFT, TOP, RIGHT, BOTTOM)))
    

    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    temp_ = cv2.imread(img_src, 0).copy()

    
    res =  cv2.matchTemplate(image, temp_, cv2.TM_CCOEFF_NORMED)

    threshold = 0.8
    coord = np.where(res >= threshold)

    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)


    temp_height, temp_width = temp_.shape

    loc = (max_loc[0] + (temp_width // 2), max_loc[1] + (temp_height // 2))

    click(*loc)
    