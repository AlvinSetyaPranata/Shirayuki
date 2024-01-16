from modules.core.base import *
from modules.core.graphic import *
from modules.core.controller import *
from time import sleep


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
    sleep(0.5)
    current_catagory = find_text(3, 41, 13, 49).strip().lower()
    expected = expected.lower()

    while current_catagory != expected:
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



def smart_proc(mat_name, mat_catagory):
    """"
    How does it work?, well it detect the material that specified and it will
    read how many mats in one slot, if the ammount of material is 1 will be skipped,
    if not then it will proc with (total_mats - 1), that makes easier to farm without being
    overrided by another material
    """

    print("Going to proc menu....")
    goto_ex_skill()


    print("Checking the bottom 3 catagory button...")
    check_catagory_btn()
    print("Checking item filter type...")
    change_mats_catagory_filter_btn(mat_catagory)

    x = 55
    y = 25
    current_column = 0
    start = False

    if not mat_name and mat_catagory:
        return

    print(f"Begining to proc with material name {mat_name} that is type of {mat_catagory} material")
    
    while True:
        if current_column == 5:
            y += 18
            x = 55
            current_column = 1

        click_relative(x, y)
        sleep(0.8)

        selected_mats_name = find_text(3, 60, 40, 66).strip().lower()

        if not selected_mats_name:
            break

        if selected_mats_name != mat_name:
            x += 10
            current_column += 1
            continue

        selected_mats_qty = find_text(30, 60, 45, 66, detect_number_only=True)

        # Check whenever the current pointer is not indicating an empty slot
        if match_image(("bag", "empty-slot.PNG"),x-7, y-7, x+3, y+7):
            break

        if not selected_mats_qty or int(selected_mats_qty) <= 1:
            print("Skipping quantity of current stack is 1")
            x += 10
            current_column += 1
            continue

        if not start:
            start = True

        if selected_mats_name != mat_name and start:
            break

        # Click process button
        click_relative(24, 35) 

        # Set to maximum total
        click_relative(87, 38)

        # Decrease by one
        click_relative(17, 38)

        # Proc now
        click_relative(50, 85)

        # Finihing proc
        click_relative(50, 80)

        x += 10
        current_column += 1

    print("Finished")
