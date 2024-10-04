from dependencies import *

def setStartingPosition():
    print('3. Moving to start location...')
    pyautogui.moveTo(500, 350, random.uniform(0.1, 1.1), random.choice(timing)) #Alora window
    pyautogui.click()
    pyautogui.press('f6') #Click F6 to open spell page
    time.sleep(1)
    pyautogui.moveTo(787, 403, random.uniform(0.1, 1.1), random.choice(timing)) #Home tp
    pyautogui.click()
    time.sleep(3)
    pyautogui.press('esc') #Click ESC to open inventory
    print('Start location reached\n')

def screenOrientation():
    print('2. Setting screen orientation...')
    pyautogui.click(825, 45)
    pyautogui.keyDown('up')
    time.sleep(2)
    pyautogui.keyUp('up')
    pyautogui.move(100, 50)
    pyautogui.click(button='right')
    pyautogui.press('ctrlleft')
    print('Screen orientation set\n')

def windowSetup():
    print('1. Setting up windows ...')
    activeWindows = pyautogui.getAllWindows()
    aloraRegex = re.compile("Alora.*")
    pythonRegex = re.compile("py\.exe.*")
    aloraClient = None
    pythonClient = None
    for activeWindow in activeWindows:
        if (re.search(aloraRegex, activeWindow.title)):
            aloraClient = activeWindow
        if (re.search(pythonRegex, activeWindow.title)):
            pythonClient = activeWindow
    print('Windows are set\n')
    if aloraClient is not None:
        aloraClient.size = (1000, 700)
        aloraClient.moveTo(0, 0)
        pythonClient.size = (600, 700)
        pythonClient.moveTo(1001, 0)
    else:
        print('Alora window is not found, shutting down')
        time.sleep(3)
   
   
def setup():
    print("Don't press any keys during the setup sequence \n")
    time.sleep(1)
    try:
        windowSetup()
        screenOrientation()
        setStartingPosition()
    except:
        print('Something went wrong.')

    print('Success, setup is finished')
    time.sleep(2)
    
setup()

