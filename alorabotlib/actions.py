from dependencies import *

pyautogui.FAILSAFE = False

def click(x: int, y: int, buttonType: str = 'left', duration: list = [0,0], sleepBeforeClick: float = 0, sleepAfterClick: float = 0, humanize: bool = True) -> None:
    '''
    This function executes a mouse move and click with custom parameters
    
    :param x: coordinate on the screen
    :param y: coordinate on the screen
    :param buttonType: what mouse button to press
    :param duration: random duration based on entered min and max range
    :param sleepBeforeClick: how long should the script wait before clicking the button (in seconds)
    :param sleepAfterClick: how long should the script wait after clicking the button (in seconds)
    :param humanize: should the mouse move apply a curve to randomize the path 

    '''
    time.sleep(sleepBeforeClick)
    pyautogui.moveTo(x, y, random.uniform(duration[0], duration[1]), random.choice(timing) if humanize else linear)
    pyautogui.click(button = buttonType)
    time.sleep(sleepAfterClick)
    
def press(button: str, sleep: float = 0) -> None:
    '''
    This function presses a provided button
    
    :param button: button to press
    :param sleep: wait time after the button press (in seconds)

    '''
    pyautogui.press(button)
    time.sleep(sleep)

def getScreenshot(x: int, y: int, length: int = 1, height: int = 1, save: bool = False):
    '''
    This function takes a screenshot 
    
    :param x: coordinate on the screen
    :param y: coordinate on the screen
    :param length: length of the screenshot window
    :param height: height of the screenshot window
    :param save: should the screenshot be saved in C:/Users/Public/Pictures/Screenshot.png

    '''
    screenshot = pyautogui.screenshot(region=(x, y, length, height))
    if (save):
        screenshot.save(r'C:\Users\Public\Pictures\Screenshot.png')
    return screenshot

def getPixelColor(x: int, y: int, screenshot):
    '''
    This function returns a color of the pixel
    
    :param x: coordinate on the attached object
    :param y: coordinate on the attached object
    :param screenshot: a screenshot taken with getScreenshot function

    '''
    red, green, blue = screenshot.getpixel((x,y))
    return red, green, blue

def formatPrint(message: str, newLine: bool = True) -> None:
    '''
    This function prints a message in the console
    
    :param message: message to be displayed
    :param newLine: should it have a new line after the message

    '''
    newLineChar = "\n"
    print(f'>> {message} {newLineChar if newLine else ""}')
    
def findImageOnScreen(resource: str, x: int, y: int, length: int, height: int, findConfidence: float = 1, tries: int = 10, turnOffMessages: bool = False):
    '''
    This function locates x and y of the provided image on the specified region, returns false if not found
    
    :param resource: image or a file you want to search for (must be in resources folder)
    :param x: coordinate on the screen
    :param y: coordinate on the screen
    :param length: length of the screenshot window
    :param height: height of the screenshot window
    :param findConfidence: how much should the images match (0 - 1)
    :param tries: how many times to try before timing out
    :param turnOffMessages: should the message be outputted about the return of this function

    '''
    while tries > 0:
        try:
            x, y = pyautogui.locateCenterOnScreen(absolutePath + resource, region=(x , y, length, height), confidence = findConfidence)
            if (x is not None and y is not None):
                if (turnOffMessages is False):
                    formatPrint(f'{resource} found!')
                return x, y
        except:
            if (turnOffMessages is False):
                formatPrint(f'Unable to find {resource} -> looking again | {tries - 1} tries remaining', False)
                formatPrint(f'Make sure such file exists within \'resources\' folder')
            tries -= 1
            time.sleep(1.5)
    return False, False # 2 false because we need to return 2 values

def teleportHome(sleepAfterClick: float = 0):
    '''
    This function teleports the player home
    
    :param sleepAfterClick: how long should the script wait after clicking the button (in seconds)

    '''
    press('f6', 0.15) # Open spell book
    click(788,405, sleepBeforeClick = 0.1, humanize = False) # click on home tp
    press('esc') # click on home tp
    time.sleep(sleepAfterClick)
    
def findColorInRegion(x: int, y: int, length: int, height: int, red: int, green: int, blue: int, tries: int = 10):
    '''
    This function finds the given color in given region
    
    :param x: coordinate on the screen
    :param y: coordinate on the screen
    :param length: length of the screenshot window
    :param height: height of the screenshot window
    :param red: red color value to search for
    :param green: green color value to search for
    :param blue: blue color value to search for
    :param tries: how many times to try before timing out
    
    '''
    innerScreenshot = getScreenshot(x, y, length, height)
    while tries > 0:
        for xCord in range(0,height):
            for yCord in range(0,height):
                r, g, b = getPixelColor(xCord, yCord, innerScreenshot)
                if r == red and g == green and b == blue:
                    formatPrint(f'Specified color found!')
                    return x + xCord, y + yCord
        formatPrint(f'Unable to find specified color -> looking again | {tries - 1} tries remaining', False)
        innerScreenshot = getScreenshot(x, y, length, height)
        tries -= 1
        time.sleep(1.5)
    return False, False # 2 false because we need to return 2 values

def playSound(resource: str, sleepAfterSound: float = 0):
    '''
    This function plays a sound
    
    :param resource: sound or a file you want to search for (must be in resources folder)
    :param sleepAfterSound: how long should the script wait after clicking the button (in seconds)

    '''
    playsound.playsound(absolutePath + resource)
    time.sleep(sleepAfterSound)

def clearConsole():
    '''
    This function clears the console

    '''
    os.system('cls')
    
def moveCursorToCenter():
    '''
    This function moves the cursor to the center of the screen

    '''
    pyautogui.moveTo(501, 362)
    
def typeToChat(Message: str):
    '''
    This function types a message in the chat

    '''
    pyautogui.press('Enter')
    pyautogui.typewrite(Message,0.1)
    time.sleep(0.5)
    pyautogui.press('Enter')