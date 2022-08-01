import pyautogui
import time

time.sleep(5)

while (1 < 2):
    ##locateOnScreen('calc7key.png')
    pyautogui.keyDown('w')
    pyautogui.mouseDown(button='left')
    if keyboard.is_pressed('right alt'):
        break
