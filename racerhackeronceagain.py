import pyautogui as gui
import keyboard
import threading
from PIL import ImageGrab

#gui.displayMousePosition()

block_btn_pos = (565,457)
store_btn_pos = (449,613)
space_btn_pos = (530,446)
race_btn_pos = (529,613)

upgrade_btn_pos = [
 (444,567),#up1
 (515,567),#up2
 (587,567),#up3
]

ads_btn_pos = [
 (453,546),#1ad
 (522,546),#2ad
 (591,546),#3ad
]

while True:
    # Constant clicks
    gui.click(block_btn_pos)
    gui.click(space_btn_pos)
    if keyboard.is_pressed("Esc"):
        break

    # Check if "Race" button clickable
    race_x, race_y = race_btn_pos
    r,g,b = gui.pixel(race_x,race_y)
    if r == 248 and g == 139 and b == 90:            
        gui.click(race_x,race_y)


    for i in range(len(upgrade_btn_pos)):
        upg_x, upg_y = upgrade_btn_pos[i]

        r,g,b = gui.pixel(upg_x, upg_y)
        upg_clickable = b > 230

        if upg_clickable:
            ads_x, ads_y = ads_btn_pos[i]
            r,g,b = gui.pixel(ads_x, ads_y)
            ads_button_exists = r >= 230 and g >= 230 and  b >= 230
            if ads_button_exists:
                print('ads exists')
            else:
                print("clicking upgrade")
                gui.click(upg_x, upg_y)