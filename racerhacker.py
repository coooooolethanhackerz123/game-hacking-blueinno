import pyautogui as gui
import keyboard
import threading
from PIL import ImageGrab

#gui.displayMousePosition()

block_btn_pos = (565,457)
upgrade_btn_pos = [
 (465,567),#clickspace
 (535,567),#up1
 (601,565),#up2
 (477,619),#up3
 (544,541),#store
 (576,614),#race
 (455,539),#1ad
 (525,537),#2ad
 (598,537),#3ad
]

while True:
    gui.click(block_btn_pos)
    if keyboard.is_pressed("Esc"):
        break

    

    for x,y in upgrade_btn_pos:
        r,g,b = gui.pixel(x,y)
    if r == 248 and g == 139 and b == 90:            
        gui.click(x,y)

    for x,y in upgrade_btn_pos:
        r,g,b = gui.pixel(x,y)           
        if b == 207:
                gui.click(x,y)

    for x,y in upgrade_btn_pos:
        r,g,b = gui.pixel(x,y)  
        upg_clickable = b == 207
        ads_button_exists = r == 3 and b == 10 and  b == 32
        if upg_clickable:
            if ads_button_exists:
                print('ads are inbound')
            else:     
                gui.click(x,y)

    
        

    

        


