from modules.core.base import *
from modules.core.graphic import *
from modules.core.controller import *
from time import sleep


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

GRADE_ALPHABHETS = {
    "e" : 10,
    "d" : 11,
    "c" : 12,
    "b" : 13,
    "a" : 14,
    "s" : 15
}

def get_grade(text):
    if type(text) == int:
        return text

    if not text:
        return False

    grade = text.split()[-1][-1]

    if grade in GRADE_ALPHABHETS:
        return GRADE_ALPHABHETS[grade]

    return int(grade)


def smart_refine(stack, pcs=0):
    """
    Automatically switch to luck character, if +C class is reached 
    """

    press("p")
    click_relative(75, 38)
    click_relative(75, 25)
    click_relative(35, 25)
    click_relative(75, 65)
    click_relative(75, 25)
    click_relative(75, 25)
    click_relative(75, 25)
    click_relative(25, 90)
    print("Refining.....")


    sleep(5)
    

    current_grade = get_grade(find_text(35, 31, 70, 40).lower())
    current_role = "TEC"
    total_mats = (99 * stack) + pcs

    # Complete the refine
    click_relative(50, 77)
    print(f"Total Mats: {total_mats}")

    while not current_grade == 15 or stack > 0:
        click_relative(25, 90)
        print("Refining.....")
        sleep(5)
        
        # status = find_text(25, 25, 60, 32).lower()
        # print(f"Current Status: {status}")

        new_grade = get_grade(find_text(35, 31, 70, 40).lower())

        while not new_grade:
            new_grade = get_grade(find_text(35, 31, 70, 40).lower())
        

        current_grade = get_grade(new_grade)
        print(f"Current Grade: {new_grade}")

        
        # Complete the refine
        click_relative(50, 77)

        total_mats -= 1

        if current_grade >= 12 and current_role !=  "LUK":
            print("Switching to BS LUK")
            press("ESC")
            current_role = "LUK"
            switch_character(4)
            sleep(6)

            press("p")
            click_relative(75, 38)
            click_relative(75, 25)
            click_relative(35, 25)
            click_relative(75, 65)
            click_relative(75, 25)
            click_relative(75, 25)
            click_relative(75, 25)
            click_relative(25, 90)
            print("Refining.....")

            sleep(5)
            total_mats -= 1

        elif current_grade < 12 and current_role != "TEC":
            print("Switching to BS TEC")
            press("ESC")
            current_role = "TEC"
            switch_character(3)
            sleep(6)

            press("p")
            click_relative(75, 38)
            click_relative(75, 25)
            click_relative(35, 25)
            click_relative(75, 65)
            click_relative(75, 25)
            click_relative(75, 25)
            click_relative(75, 25)
            click_relative(25, 90)
            print("Refining.....")

            sleep(5)
            total_mats -= 1

        print(f"Total Mats: {total_mats}")

    print(f"Refinement Finished, mats left {total_mats}")

        

