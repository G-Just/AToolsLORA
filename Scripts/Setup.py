import pygetwindow
import pyautogui
import re
import time

print("Don't press any keys during the setup sequence.")

def ScreenOrientation():
    print('Setting screen orientation...')
    pyautogui.click(825, 45)
    pyautogui.keyDown('up')
    time.sleep(2)
    pyautogui.keyUp('up')
    print('Screen orientation set')
    input('Press any button to continue...')

print('Searching for Alora window...')
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

if aloraClient is not None:
    print('Alora window found, resizing')
    aloraClient.size = (1000, 700)
    aloraClient.moveTo(0, 0)
    pythonClient.size = (600, 700)
    pythonClient.moveTo(1001, 0)
    ScreenOrientation()
else:
    print('Alora window is not found')
    input('Press any button to continue...')