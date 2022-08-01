
##import keyboard
## used a duckyscript to python thing for the basic portions
import pyautogui
import time
import webbrowser
time.sleep(3)
pyautogui.hotkey("winleft")
time.sleep(0.4) #best timing so it doesn't miss from lag
pyautogui.hotkey( "T")
time.sleep(.01) #can be very fast since it's just opening
pyautogui.hotkey("enter")
time.sleep(0.3) #longer for term to open    
pyautogui.typewrite("neofetch", interval=0.0)
pyautogui.hotkey("enter")
webbrowser.open("https://youtu.be/0UqjvVaU7B4?t=46") #using normal python stuff with auto gui
pyautogui.hotkey(("space"))

exit()