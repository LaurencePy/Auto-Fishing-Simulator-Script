import pygetwindow as gw
import keyboard as kb
import pyautogui as pygetwindow


def selectwindow():
    try:
        gameWindow = gw.getWindowsWithTitle('Roblox')
    except:
        print(exception)