import pyautogui
import time 
import os

os.makedirs('screenshots', exist_ok=True)

while True:
    pyautogui.screenshot(f'screenshots/screenshort_{int(time.time())}.png')

    print ('Screenshot taken!')
    print ('Waiting for 5 seconds...')

    time.sleep(10)