import cv2
import numpy as np
from PIL import ImageGrab as IG
from .base import get_relative_pos
from PIL import Image
import pytesseract


pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

def detect_red(image):

    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    lower_red = np.array([0, 100, 100])
    upper_red = np.array([10, 255, 255])

    mask1 = cv2.inRange(hsv_image, lower_red, upper_red)

    lower_red = np.array([160, 100, 100])
    upper_red = np.array([180, 255, 255])

    mask2 = cv2.inRange(hsv_image, lower_red, upper_red)

    color_mask = cv2.bitwise_or(mask1, mask2)



    # result = cv2.bitwise_and(image, image, mask=color_mask)

    # cv2.imshow('Original Image', cv2.imread(image_path))

        

    # binary_result = cv2.cvtColor(result, cv2.COLOR_BGR2GRAY)
    # ret, binary_results = cv2.threshold(binary_result, 1, 255, cv2.THRESH_BINARY)

    # cv2.imshow('Red Color Detection Result', binary_result)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()



    return np.any(color_mask)


def detect_blue(image):
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    lower_blue = np.array([100, 50, 50])
    upper_blue = np.array([130, 255, 255])

    blue_mask = cv2.inRange(hsv_image, lower_blue, upper_blue)

    return np.any(blue_mask)



def grab_image_in(left, top, right, bottom, development=False):
    image = np.array(IG.grab(bbox=(*get_relative_pos(left, top), *get_relative_pos(right, bottom),)))
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    if development:
        cv2.imshow('Results', image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    return image


def find_image(image_path):
    image_data = grab_image_in(0, 0, 100, 100)

    image_data = cv2.cvtColor(image_data, cv2.COLOR_BGR2GRAY)
    temp_ = cv2.imread(image_path, 0).copy()

    
    res =  cv2.matchTemplate(image_data, temp_, cv2.TM_CCOEFF_NORMED)

    threshold = 0.8
    coord = np.where(res >= threshold)

    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)


    temp_height, temp_width = temp_.shape

    loc = (max_loc[0] + (temp_width // 2), max_loc[1] + (temp_height // 2))

    return loc    


def find_text(left, top, right, bottom, development=False):
    image_data = grab_image_in(left, top, right, bottom)

    text = pytesseract.image_to_string(image_data)

    if development:
        cv2.imshow('Results', image_data)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    return text