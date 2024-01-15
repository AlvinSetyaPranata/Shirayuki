"""
DESC:

Files contains all functions that related to socials work, e.g
Gift, Trade, Etc.

"""
from modules.core.base import click_relative, write
from modules.core.graphic import grab_image_in
from time import sleep

# EMPTY_SLOT_TEMP = cv2.imread("assets\\empty_slot.png")


def auto_gift(max_mats):
    for _ in range(max_mats):
        grab_image("assets\\sendgift.png")
        sleep(0.8)
        print("send gift 1")
        grab_image("assets\\selectplayer.png")
        print("select player")
        sleep(0.8)
        grab_image("assets\\player_gift_list\\hayasaka_ai.png")
        print("player")
        sleep(0.8)
        grab_image("assets\\selectgift.png")
        print("select gift")
        sleep(0.8)
    
        click_relative(55, 25)
        click_relative(55, 25)
        print("mats 1")
        sleep(get_interval())
        click_relative(72, 45)
        print("quantiy")
        sleep(get_interval())
        click_relative(55, 75)
        print("select")
        sleep(get_interval())
        click_relative(28, 43)
        print("confirm")
        sleep(get_interval())
        grab_image("assets\\sendgift2.png")
        sleep(get_interval())
        grab_image("assets\\ok.png")
        sleep(get_interval())

# def is_empty(pos_x, pos_y):
#     pos_x, pos_y = get_relative_pos(pos_x, pos_y)

#     if not pos_x:
#         return
    
#     image = np.array(IG.grab(bbox=(pos_x -35, pos_y - 35, pos_x, pos_y)))
#     temp_ = np.array(EMPTY_SLOT_TEMP).copy()

#     res =  cv2.matchTemplate(image, temp_, cv2.TM_CCOEFF_NORMED)

#     threshold = 0.8
#     coord = np.where(res >= threshold)

#     min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

    
#     print(max_val)


def auto_chat():
    p = grab_image_in(1, 70, 28, 90, development=True)
    # click_relative(15, 91)
    # sleep(1)
    # write("Hello worlds")