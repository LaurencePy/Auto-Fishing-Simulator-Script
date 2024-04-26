import pygetwindow as gw
import keyboard as kb
import pyautogui as ag
import numpy as np


# Screen areas for checking:

# Box for bubbles:

# top left (300, 150)
# bottom left (300, 750)
# top right (1620, 150)
# bottom right (1620, 750)

# Box for green:

# top left (750, 775)
# bottom left (750, 880)
# top right (1150, 775)
# bottom right (1150, 880)

# Click indicator:
# position check: (825, 823)



def selectwindow():
    try:
        gameWindow = gw.getWindowsWithTitle('Roblox')
        return(gameWindow)
    except Exception as e: print(e)

def startscript():
    kb.wait(';')
    checkforbubbles()

def automatedfishing():
    
    positioncolour = (255, 255, 255)
    s = ag.screenshot()
    if s.getpixel((870, 820)) == positioncolour:
        ag.click(button='left')
        


def checkforbubbles():
    bubblecolour = (68, 252, 234)
    s = ag.screenshot()
    pixelarray = np.array(s)
    area = pixelarray[150:750, 300:1620]
    matches = np.where(np.all(area == bubblecolour, axis=-1))
    if matches[0].size > 0:
        ag.click(button='left')
        checkforgreen()


def checkforgreen():
    barcolour = (83, 250, 83)
    s = ag.screenshot()
    for i in range(750, 1150):
        for j in range(775, 880):
            if s.getpixel((i, j)) == barcolour:
                #print(i,j)
                automatedfishing()















def main():
    gamewindow = selectwindow()
    if not gamewindow is None:
        startscript()
    else:
        print("Failed to find the Roblox window.")

if __name__ == "__main__":
    main()
