import pyautogui as gui
import keyboard
import threading
from PIL import ImageGrab

#gui.displayMousePosition()

block_btn_pos = (1384,397)
upgrade_btn_pos = [
    (1696,331),
    (1816,335),
    (1685,397),
    (1827,402),
    (1680,468),
    (1818,467),
    (1681,530),
    (1692,288),
    (1745,292),
    (1795,291),
    (1629,292),
    (1811,531)
]


while True:
    gui.click(block_btn_pos)
    if keyboard.is_pressed("Esc"):
        break

    # for x,y in upgrade_btn_pos:
    #     r,g,b = gui.pixel(x,y)
    #     if g < 200:
    #         gui.click(x,y)