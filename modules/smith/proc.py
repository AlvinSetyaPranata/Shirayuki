from . import clickRelative
import pyautogui as gui


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
