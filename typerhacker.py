import pyautogui as gui
import pytesseract
from PIL import ImageGrab
import time

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# gui.displayMousePosition()

left = 1040
right = 1864
top = 450
bottom = 490

gui.click(left,top)

time.sleep(0.5)

FILE_NAME = "words.png"
screenshot = ImageGrab.grab(bbox=(left,top,right,bottom))
screenshot.save(FILE_NAME)

height = (bottom - top) + 20
top += height
bottom += height

while True:
    text = pytesseract.image_to_string(FILE_NAME, lang = 'eng')
    print(text)
    
    gui.typewrite(text, interval=0)
    gui.typewrite(' ')

    screenshot = ImageGrab.grab(bbox=(left,top,right,bottom))
    screenshot.save(FILE_NAME)