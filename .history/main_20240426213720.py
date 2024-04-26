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
    while True:  # Continues checking until the function is explicitly exited
        s = ag.screenshot()
        bubble_found = False  # Flag to indicate a bubble is found
        
        for i in range(300, 1620):
            if bubble_found:
                break  # Exit the outer loop if bubble is found
            for j in range(150, 750):
                if s.getpixel((i, j)) == bubblecolour:
                    print("Bubble found")
                    ag.click(button='left')
                    checkforgreen()
                    bubble_found = True  # Set the flag to True
                    break  # Break the inner loop if a bubble is found
        
        if bubble_found:
            print("Waiting for next bubbles to appear...")
            time.sleep(10)  # Add a delay before checking again if needed, adjust as per the game's requirements

        # Add a condition to break the while True loop if necessary
        # For example, checking for a key press to stop the loop
        if keyboard.is_pressed('#'):
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
