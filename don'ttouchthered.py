import pyautogui as gui
from PIL import ImageGrab
#gui.displayMousePosition()

gui.PAUSE = 0.3
hx = 1371
jx = 1474
kx = 1585
lx = 1690
y = 646


while True:
    
    screenshot = ImageGrab.grab()
    pixels = screenshot.load()

    ph = pixels[hx, y]
    pj = pixels[jx, y]
    pk = pixels[kx, y]
    pl = pixels[lx, y]

    if ph[1] > 200:
        gui.press('h')
        # gui.click(hx,y)

    if pj[1] > 200:
        gui.press('j')
        # gui.click(jx,y)

    if pk[1] > 200:
        gui.press('k')
        # gui.click(kx,y)

    if pl[1] > 200:
        gui.press('l')
        #gui.click(lx,y)

        