import pyautogui as gui
import pytesseract
from PIL import ImageGrab

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
FILE_NAME = 'words.png'
text = pytesseract.image_to_string(FILE_NAME, lang = 'eng')
print(text)