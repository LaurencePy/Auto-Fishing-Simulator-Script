import pygetwindow as gw
import keyboard as kb
import pyautogui as ag


def selectwindow():
    try:
        gameWindow = gw.getWindowsWithTitle('Roblox')
    except Exception as e: print(e)
selectwindow()

def startscript():
    keyboard.wait(';')


def checkforgreen():
    barcolour = (83, 250, 83)
    s = pyautogui.screenshot()
    for i in range(s.width):
        for j in range(s.height):
            if s.getpixel((i, j)) == barcolour:
                pyautogui.click(x, y)
