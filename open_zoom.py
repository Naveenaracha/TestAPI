import pyautogui
import pygetwindow as gw
import time
import datetime
import subprocess
import pyperclip
import re

def open_zoom(topic):
    zoom_path = "C:\\Users\\Chirag Tiwari\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe"

    try:
        subprocess.Popen(zoom_path) 
    except FileNotFoundError:
        print(f"Zoom not found at {zoom_path}. Please verify the path.")
        exit()

    time.sleep(5)

    zoom_window = None
    for window in gw.getWindowsWithTitle("Zoom"):
        if "Zoom" in window.title:
            zoom_window = window
            break

    if zoom_window:
        zoom_window.activate()  
    else:
        print("Zoom window not found.")
        exit()

    schedule_button_x, schedule_button_y = 623, 607  

    pyautogui.moveTo(schedule_button_x, schedule_button_y)
    pyautogui.click()  

    time.sleep(2)

    pyautogui.write(f"Lecture on {topic}", interval=0.1)

    pyautogui.moveTo(816, 338)
    pyautogui.click()  

    pyautogui.write((datetime.datetime.now() + datetime.timedelta(minutes=1)).strftime('%H:%M'), interval=0.1)


    pyautogui.moveTo(1037, 342)
    pyautogui.click()  

    pyautogui.write((datetime.datetime.now() + datetime.timedelta(minutes=6)).strftime('%H:%M'), interval=0.1)

    pyautogui.moveTo(1316, 953)
    pyautogui.click()

    time.sleep(4)
    pyautogui.keyDown('ctrl') 
    pyautogui.press('w')

    time.sleep(2)


    pyautogui.moveTo(1877, 466)
    pyautogui.click()


    pyautogui.moveTo(1699, 576)
    pyautogui.click()

    copied_info = pyperclip.paste()
    zoom_link_pattern = r"(https://[^\s]+)"
    zoom_link = re.search(zoom_link_pattern, copied_info)
    if zoom_link:
        link = zoom_link[0]

    time.sleep(3)
    pyautogui.moveTo(1877, 486)
    pyautogui.click()

    time.sleep(2)

    pyautogui.moveTo(1876, 464)
    pyautogui.click()

    pyautogui.moveTo(1722, 518)
    pyautogui.click()

    time.sleep(5)
    pyautogui.click()

    pyautogui.moveTo(1221, 486)
    pyautogui.doubleClick()

    time.sleep(2)
    pyautogui.moveTo(939, 1044)
    pyautogui.click()

    time.sleep(1)

    pyautogui.moveTo(434, 534)
    pyautogui.click()


    pyautogui.moveTo(954, 954)
    pyautogui.click()

    return link
