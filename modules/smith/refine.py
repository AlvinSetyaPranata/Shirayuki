from modules.core.base import *
from modules.core.graphic import *
from modules.core.controller import *


"""
ALL TEMPLATES IS BASED ON 960x540 

"""


# TEMPLATES = {
#     "AUTO-ITEMS" : (3, 62),
#     "BAG-LEFT" : (8, 62),
#     "PRESENT" : (13, 62),
#     "PLAYER" : (82, 91),
#     "BAG-RIGHT" : (87, 91),
#     "ORB" : (92, 91),
#     "SETTINGS" : (97, 91),
#     "SOCIAL" : (82, 81),
#     "QUEST" : (87, 81)
# }

def smart_refine():
    """
    Automatically switch to luck character, if +C class is reached 

    """
    change = False
    succcess = False

    print(detect_color(grab_image_in(40, 25, 50, 40)))

    # while not succcess:
    #     press("p")
    #     click_relative(75, 38)
    #     click_relative(75, 33)

        # if detect_color(grab_image_in(40, 25, 50, 40)):
        #     pass
        

    #     switch_character(1)
    

    



def refine_luck():
    pass