import pyautogui as gui
import keyboard
import threading
from PIL import ImageGrab

# gui.displayMousePosition()

red_btn_pos = (1351,417)
upgrade_btn_pos = [
    (1810,321),
    (1826,410),
    (1822,475),
    (1832,536),
    (1809,600)
]

while True:
    gui.click(red_btn_pos)

    if keyboard.is_pressed("Esc"):
        break

    # for x,y in upgrade_btn_pos:
    #     r,g,b = gui.pixel(x,y)
    #     if g > 200:
    #         gui.click(x,y)
