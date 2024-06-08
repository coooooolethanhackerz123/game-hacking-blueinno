from PIL import ImageGrab
import pyautogui as gui

# gui.displayMousePosition()

holes = [
    (1313,300),
    (1403,358),
    (1272,419),
    (1260,534),
    (1471,556),
    (1526,424),
    (1514,306),
    (1636,350),
    (1711,437),
    (1688,554),
]


while True:
    #mouseX,mouseY = gui.position()
    screenshot = ImageGrab.grab()
    pixels = screenshot.load()
    #print(pixels[mouseX, mouseY])

    for (x,y) in holes:
        pixel = pixels[x,y]
        r = pixel[0]
        g = pixel[1]
        b = pixel[2]

        is_black = r < 50 and g < 50 and b < 50
        if not is_black:
            gui.click(x, y)