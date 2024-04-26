import pygetwindow as gw
import keyboard as kb
import pyautogui as pygetwindow


def selectwindow():
    try:
        window = gw.getWindowsWithTitle('Roblox')
    except:
        print("error")