
##import keyboard

## used a duckyscript to python thing for the basic portions


## [wastes 100% of cpu when doing if --> ]if keyboard.is_pressed('left alt'):
import pyautogui
import time
pyautogui.hotkey("win","T")
pyautogui.hotkey("enter")
time.sleep(0.1)
pyautogui.typewrite("neofetch", interval=0.02)
pyautogui.hotkey("enter")
exit()