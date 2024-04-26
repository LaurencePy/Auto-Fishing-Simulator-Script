import pygetwindow as gw
import keyboard as kb
import pyautogui as pa


def selectwindow():
    try:
        gameWindow = gw.getWindowsWithTitle('Roblox')
        print(pyautogui.position())
    except Exception as e: print(e)

selectwindow()
