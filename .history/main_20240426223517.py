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
    while True:
        s = ag.screenshot()
        bubble_found = False
        
        for i in range(300, 1620):
            for j in range(150, 750):
                if s.getpixel((i, j)) == bubblecolour:
                    print("Bubble found")
                    ag.click(button='left')
                    automatedfishing()
                    bubble_found = True
                    break
            if bubble_found:
                break

        if kb.is_pressed(','):
            print("Stopping bubble checks...")
            break

def automatedfishing():
    positioncolour = (255, 255, 255)
    barcolour = (83, 250, 83)
    position = (877, 815)  # Confirmed correct position
    print("Starting automated fishing...")
    while True:
        s = ag.screenshot()
        current_color = s.getpixel(position)
        print(f"Checking color at {position}: {current_color}")  # Debug output to verify color check

        if current_color == positioncolour:
            print("White bar detected - clicking...")
            ag.click(button='left')
        elif current_color not in (positioncolour, barcolour):
            checkforbubbles()



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