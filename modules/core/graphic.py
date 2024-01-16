import cv2
import numpy as np
from PIL import ImageGrab as IG
from .base import get_relative_pos
from PIL import Image
import pytesseract
from pathlib import Path
from os.path import isfile

"""
Support OCR for detecting text and numbers
"""


pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

def detect_red(image):

    hsv_image = cv2.cvtColor(image, cv2.COLOR_RGB2HSV)

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
    hsv_image = cv2.cvtColor(image, cv2.COLOR_RGB2HSV)

    lower_blue = np.array([100, 50, 50])
    upper_blue = np.array([130, 255, 255])

    blue_mask = cv2.inRange(hsv_image, lower_blue, upper_blue)


    return np.any(blue_mask)



def grab_image_in(left, top, right, bottom, development=False):
    image = np.array(IG.grab(bbox=(*get_relative_pos(left, top), *get_relative_pos(right, bottom),)))
    
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


def find_text(left, top, right, bottom, development=False, detect_number_only=False):
    image_data = grab_image_in(left, top, right, bottom)
    options = ""


    if detect_number_only:
        options = r'--oem 3 --psm 6 outputbase digits'

    text = pytesseract.image_to_string(image_data, config=options)

    if development:
        cv2.imshow('Results', image_data)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    return text

def match_image(image_path, left, top, right, bottom):

    filename = Path("assets", *image_path).resolve()

    sift = cv2.SIFT_create()
    target = cv2.cvtColor(grab_image_in(left, top, right, bottom), cv2.COLOR_RGB2GRAY)
    template = cv2.imread(fr'{filename}', 0)

    # Find keypoints and descriptors with SIFT
    kp1, des1 = sift.detectAndCompute(target, None)
    kp2, des2 = sift.detectAndCompute(template, None)

    # FLANN parameters
    FLANN_INDEX_KDTREE = 1
    index_params = dict(algorithm=FLANN_INDEX_KDTREE, trees=5)
    search_params = dict(checks=50)

    # FLANN-based matcher
    flann = cv2.FlannBasedMatcher(index_params,search_params)
    matches = flann.knnMatch(des1, des2, k=2)

    # Need to draw only good matches, so create a mask
    matchesMask = [[0,0] for _ in range(len(matches))]

    # ratio test as per Lowe's paper
    for i,(m,n) in enumerate(matches):
        if m.distance < 0.7 * n.distance:
            matchesMask[i]=[1,0]

    if len(matchesMask) == 2:
        return True

    return False
    
