import actions
import pyautogui
import navigation
import procedure
from pynput import keyboard

actions.getScreenshot(1704, 746, 186, 100, True)

def switchToMele(startX, startY):
    actions.clearConsole()
    actions.formatPrint('Currently selected: MELE')
    xHelmet, yHelmet = actions.findImageOnScreen('MeleVoidHelmet.png', 1704, 746, 186, 257, findConfidence=0.9, tries=1, turnOffMessages=True)
    xOsm, yOsm = actions.findImageOnScreen('MeleOsmFang.png', 1704, 746, 186, 257, findConfidence=0.9, tries=1, turnOffMessages=True)
    xBoots, yBoots = actions.findImageOnScreen('MeleDBoots.png', 1704, 746, 186, 257, findConfidence=0.9, tries=1, turnOffMessages=True)
    xDefender, yDefender = actions.findImageOnScreen('MeleDefender.png', 1704, 746, 186, 257, findConfidence=0.9, tries=1, turnOffMessages=True)

    if xHelmet is not False:
        actions.click(xHelmet,yHelmet, humanize=False)
    if xOsm is not False:
        actions.click(xOsm, yOsm, humanize=False)
    if xBoots is not False:
        actions.click(xBoots, yBoots, humanize=False)
    if xDefender is not False:
        actions.click(xDefender, yDefender, humanize=False)
    pyautogui.moveTo(startX, startY)    


def switchToRange(startX, startY):
    actions.clearConsole()
    actions.formatPrint('Currently selected: RANGE')
    xHelmet, yHelmet = actions.findImageOnScreen('RangeVoidHelmet.png', 1704, 746, 186, 257, findConfidence=0.9, tries=1, turnOffMessages=True)
    xBlowpipe, yBlowpipe = actions.findImageOnScreen('RangeBlowpipe.png', 1704, 746, 186, 257, findConfidence=0.9, tries=1, turnOffMessages=True)
    xBoots, yBoots = actions.findImageOnScreen('RangePBoots.png', 1704, 746, 186, 257, findConfidence=0.9, tries=1, turnOffMessages=True)
    
    if xHelmet is not False:
        actions.click(xHelmet, yHelmet, humanize=False)
    if xBlowpipe is not False:
        actions.click(xBlowpipe, yBlowpipe, humanize=False)
    if xBoots is not False:
        actions.click(xBoots, yBoots, humanize=False)
    pyautogui.moveTo(startX, startY)    


def switchToMage(startX, startY):
    actions.clearConsole()
    actions.formatPrint('Currently selected: MAGE')
    xHelmet, yHelmet = actions.findImageOnScreen('MageVoidHelmet.png', 1704, 746, 186, 257, findConfidence=0.9, tries=1, turnOffMessages=True)
    xTrident, yTrident = actions.findImageOnScreen('MageTrident.png', 1704, 746, 186, 257, findConfidence=0.9, tries=1, turnOffMessages=True)
    xDefender, yDefender = actions.findImageOnScreen('MeleDefender.png', 1704, 746, 186, 257, findConfidence=0.9, tries=1, turnOffMessages=True)


    if xHelmet is not False:
            actions.click(xHelmet, yHelmet, humanize=False)
    if xTrident is not False:
        actions.click(xTrident, yTrident, humanize=False)
    if xDefender is not False:
        actions.click(xDefender, yDefender, humanize=False)
    pyautogui.moveTo(startX, startY)    


def on_press(key):
    try:
        k = key.char  # single-char keys
    except:
        k = key.name  # other keys
    if k in ['1', '2', '3']:  # keys of interest
        x, y = pyautogui.position()
        if k == '1':
            switchToMele(x, y)
        elif k == '2':
            switchToRange(x, y)
        elif k == '3':
            switchToMage(x, y)

listener = keyboard.Listener(on_press=on_press)
listener.start()  # start to listen on a separate thread
listener.join()  # remove if main thread is polling self.keys