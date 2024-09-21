import pygetwindow
import pyautogui
import re

activeWindows = pyautogui.getAllWindows()
regex = re.compile("Alora.*")
aloraClient = None
for activeWindow in activeWindows:
    if (re.search(regex, activeWindow.title)):
        aloraClient = activeWindow

if aloraClient is not None:
    aloraClient.size = (1000, 700)
    aloraClient.moveTo(0, 0)
else:
    print('Alora window is not found')
    input('Press any button to continue...')