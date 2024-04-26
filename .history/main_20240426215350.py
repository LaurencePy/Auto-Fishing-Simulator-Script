import pygetwindow as gw
import keyboard as kb
import pyautogui as ag
import time
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
    bubblecolour = (68, 252, 234)
    while True:  # Continuously check for bubbles
        s = ag.screenshot()
        bubble_found = False
        
        for i in range(300, 1620):
            for j in range(150, 750):
                if s.getpixel((i, j)) == bubblecolour:
                    print("Bubble found")
                    ag.click(button='left')
                    checkforgreen()
                    bubble_found = True
                    break
            if bubble_found:  # This will ensure the outer loop also breaks
                break

        if bubble_found:
            print("Waiting 2 seconds before re-checking...")
            time.sleep(2)  # Wait 2 seconds to prevent immediate re-detection
        else:
            print("No bubbles detected, rechecking immediately...")
            time.sleep(0.5)  # You can adjust this time based on actual game dynamics

        if kb.is_pressed(','):
            print("Stopping bubble checks...")
            break

            




def automatedfishing():
    
    positioncolour = (255, 255, 255)
    s = ag.screenshot()
    if s.getpixel((870, 823)) == positioncolour:
        ag.click(button='left')
    checkforbubbles()
        

def checkforgreen():
    bar = False
    barcolour = (83, 250, 83)
    s = ag.screenshot()
    for i in range(750, 1150):
        for j in range(775, 880):
            if s.getpixel((i, j)) == barcolour:
                #print(i,j)
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
