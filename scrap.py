import pyautogui
import time
import subprocess
import platform
import pyperclip
import re
from PIL import ImageChops, Image


link_count =50
default_tab_count = 19


def append_to_file():
 
    with open("output.txt", "a", encoding="utf-8") as f:
        f.write(pyperclip.paste())

    print("Copied text saved to output.txt")
    pyperclip.copy('');

def tab_navigate(default_tab_count):
    while(default_tab_count > 0):
        pyautogui.press('tab')
        default_tab_count -= 1
        
    


def enter_grab_exit():
    
    
    pyautogui.hotkey('shift', 'f10', 'o')
    append_to_file()
    time.sleep(1)
    pyautogui.press('tab')
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

def screenshots_are_same(img1, img2):
    diff = ImageChops.difference(img1, img2)
    return not diff.getbbox()  # None means images are identical


pyperclip.copy('')

# Step 1: Open Microsoft Edge
if platform.system() == "Windows":
    subprocess.Popen("start msedge", shell=True)
else:
    raise Exception("This script currently supports only Windows for Edge.")

# Step 2: Wait for Edge to fully launch
time.sleep(2.5)

# Step 3: Focus the URL bar (Ctrl + L)
pyautogui.hotkey("ctrl", "l")

# Step 4: Type the desired URL
pyautogui.write("https://www.facebook.com/groups/joins/", interval=0.05)

# Step 5: Press Enter to navigate
pyautogui.press("enter")

time.sleep(2)
pyautogui.moveTo(190, 300) 

time.sleep(3)

last_screenshot = pyautogui.screenshot()
scroll_amount = -300  # scroll down


while True:
    pyautogui.hotkey('ctrl','-')
    new_screenshot = pyautogui.screenshot()
    if screenshots_are_same(last_screenshot, new_screenshot):
        print("Ultimate zoom out achieved")
        
        break

    last_screenshot = new_screenshot


while True:
    pyautogui.scroll(scroll_amount)
    time.sleep(1)  # wait for content to load/render

    new_screenshot = pyautogui.screenshot()
    if screenshots_are_same(last_screenshot, new_screenshot):
        print("Reached bottom — no more content loaded.")
        
        break

    last_screenshot = new_screenshot

print("Done scrolling.")
time.sleep(2)
tab_navigate(default_tab_count)

while(link_count > 0):
    
    enter_grab_exit()
    
    link_count-=1

# Step 1: Open Microsoft Edge
if platform.system() == "Windows":
    subprocess.Popen("python build_html.py", shell=True)
else:
    raise Exception("This script currently supports only Windows for Edge.")