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

def checkforbubbles():
    bubbles = False
    bubblecolour = (68, 252, 234)
    while True:
        s = ag.screenshot()
        for i in range(300, 1620):
            for j in range(150,750):
                if s.getpixel((i, j)) == bubblecolour:
                    print("bubble found")
                    ag.click(button='left')
                    checkforgreen()
                    break  



def automatedfishing():
    
    positioncolour = (255, 255, 255)
    s = ag.screenshot()
    if s.getpixel((870, 823)) == positioncolour:
        ag.click(button='left')
        





def checkforgreen():
    bar = False
    barcolour = (83, 250, 83)
    s = ag.screenshot()
    for i in range(750, 1150):
        for j in range(775, 880):
            if s.getpixel((i, j)) == barcolour:
                #print(i,j)
                bar = True
    
    if bar == True:
        automatedfishing()










def startscript():
    kb.wait(';')
    checkforbubbles()



def main():
    gamewindow = selectwindow()
    if not gamewindow is None:
        startscript()
    else:
        print("Failed to find the Roblox window.")

if __name__ == "__main__":
    main()
