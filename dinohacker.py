import pyautogui as gui
from PIL import ImageGrab

#gui.displayMousePosition()
gui.PAUSE = 0.2

left = 1058
right = 1080
top = 390
bottom = 433

while True:
    screenshot = ImageGrab.grab(
        bbox =(left,top,right,bottom)
    )
    is_green = False
    pixels = screenshot.load()
    for x in range(screenshot.width):
        for y in range(screenshot.height):
            px = pixels[x,y]
            r = px[0]
            g = px[1]
            b = px[2]
            if (g>100) and (r<100) and (b<100):
                is_green = True
                break
        if is_green:
            gui.press('space')