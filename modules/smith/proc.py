from modules.core.base import *
from modules.core.graphic import *


def auto_proc():
    
    y = 25
    x = 55
    # 25, 43, 61, 79, 97

    for _ in range(1):

        
        if _flag_interrupt == 1:
            return

        
        if is_empty(x, y):
            continue
        
        clickRelative(x, y)
        print("s")

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

    
    #clickRelative(23, 34)

    #clickRelative(8, 34)


def change_mats_catagory_filter_btn(expected):
    current_catagory = find_text(3, 41, 13, 49).strip().lower()
    expected = expected.lower()

    # Fix

    while current_catagory != expected:
        print(current_catagory, expected)
        click_relative(7, 35)
        sleep(1)
        current_catagory = find_text(3, 41, 13, 49).strip().lower()


def check_catagory_btn():

    # Equipment filter button
    if detect_blue(grab_image_in(48, 90, 65, 98)):
        click_relative(58, 94)

    # Tools filter button
    if detect_blue(grab_image_in(65, 90, 81, 98)):
        click_relative(70, 94)

    # Collectibles filter button
    if not detect_blue(grab_image_in(81, 90, 98, 98)):
        click_relative(90, 94)



def smart_proc():
    check_catagory_btn()

