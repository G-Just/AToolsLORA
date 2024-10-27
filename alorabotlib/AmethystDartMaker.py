import actions
import procedure
import navigation
import pyautogui
import time

def clickOnRockLib(sequence: int):
    if sequence == 1:
        actions.click(584, 324, duration=[0.1, 1.1], sleepAfterClick=3) # Clicks on the second rock with ore from first
    elif sequence == 2:
        actions.click(531, 327, duration=[0.1, 1.1], sleepAfterClick=2) # Clicks on the third rock with ore from second
    elif sequence == 3:
        actions.click(529, 483, duration=[0.1, 1.1], sleepAfterClick=3) # Clicks on the fourth rock with ore from third
    elif sequence == 4:
        actions.click(498, 415, duration=[0.1, 1.1], sleepAfterClick=3) # Clicks on the fifth rock with ore from fourth
    elif sequence == 5:
        actions.click(416, 176, duration=[0.1, 1.1], sleepAfterClick=4) # Clicks on the first rock with ore from fifth
    
def mine(fullInventoryCount):
    rockToMine = 0
    actions.formatPrint('Starting mining')
    actions.click(314, 132, duration=[0.1, 1.1], sleepAfterClick=8) # Clicks on the first rock with ore
    oreHasAmethyst, y = actions.findImageOnScreen('beginToSwingMessage.png', 22, 625, 400, 15, findConfidence = 0.9, tries = 1, turnOffMessages = True)
    startedMining, y = actions.findImageOnScreen('mineSomeMessage.png', 22, 625, 400, 15, findConfidence = 0.9, tries = 1, turnOffMessages = True)
    if oreHasAmethyst is not False or startedMining is not False:
        print('checked and found')
        pass
    else:
        print('checked and not found')
        rockToMine += 1
        if rockToMine == 6:
            rockToMine = 1
        clickOnRockLib(rockToMine)
    inventoryFull, y = actions.findImageOnScreen('inventoryFullForOresMessage.png', 22, 625, 400, 15, findConfidence = 0.9, tries = 1, turnOffMessages = True)
    while inventoryFull is False:
        rockEmpty, y = actions.findImageOnScreen('rockOutOfOresMessage.png', 22, 625, 166, 15, findConfidence = 0.9, tries = 1, turnOffMessages = True)
        if rockEmpty is not False:
            actions.formatPrint('Ore empty clicking next ore')
            rockToMine += 1
            if rockToMine == 6:
                rockToMine = 1
            clickOnRockLib(rockToMine)
            timeOut = time.time() + 60 * 2
        inventoryFull, y = actions.findImageOnScreen('inventoryFullForOresMessage.png', 22, 625, 300, 15, findConfidence = 0.9, tries = 1, turnOffMessages = True)
    bank(rockToMine, fullInventoryCount)
            
def bank(rockLoction, fullInventoryCount):
    fullInventoryCount -= 1
    if rockLoction == 1:
        actions.click(609, 628, duration=[0.1, 1.1], sleepAfterClick=6) # Clicks on the bank from second rock
    elif rockLoction == 2:
        actions.click(577, 628, duration=[0.1, 1.1], sleepAfterClick=6) # Clicks on the bank from third rock
    elif rockLoction == 3:
        actions.click(671, 487, duration=[0.1, 1.1], sleepAfterClick=6) # Clicks on the bank from fourth rock
    elif rockLoction == 4:
        actions.click(589, 420, duration=[0.1, 1.1], sleepAfterClick=6) # Clicks on the bank from fifth rock
    else:
        actions.click(708, 630, duration=[0.1, 1.1], sleepAfterClick=6) # Clicks on the bank from first rock

    actions.click(563, 494, duration=[0.1, 1.1], sleepAfterClick=1) # Deposit all items
    actions.click(605, 48, duration=[0.1, 1.1], sleepAfterClick=2) # Closes the bank before mining
    if fullInventoryCount == 0:
        return
    mine(fullInventoryCount)

def craft():
    actions.formatPrint('Crafting')
    actions.click(468, 362, duration=[0.1, 1.1], sleepAfterClick=1) # Open bank
    actions.click(559, 85, duration=[0.1, 1.1], sleepAfterClick=1) # Open last tab
    actions.click(452, 499, duration=[0.1, 1.1], sleepAfterClick=1) # Click quantity all
    # actions.click(265, 500, duration=[0.1, 1.1], sleepAfterClick=1) # Click withdraw item
    chisX, chisY = actions.findImageOnScreen('chisel.png', 155, 105, 400, 100, findConfidence = 0.9, tries = 1, turnOffMessages=True)
    actions.click(chisX, chisY, duration=[0.1, 1.1], sleepAfterClick=1) # Click on chisel (in bank)
    x, y = actions.findImageOnScreen('amethystOre.png', 155, 105, 400, 100, findConfidence = 0.9, tries = 1, turnOffMessages=True)
    while x != False:
        actions.click(x, y, duration=[0.1, 1.1], sleepAfterClick=1) # Click on amethyst (in bank)
        actions.click(605, 48, duration=[0.1, 1.1], sleepAfterClick=1) # Close the bank
        chisX, chisY = actions.findImageOnScreen('chisel.png', 776, 395, 180, 255, findConfidence = 0.9, tries = 1, turnOffMessages=True) # Finding feather in inventory
        amethX, amethY = actions.findImageOnScreen('amethystOre.png', 776, 395, 180, 255, findConfidence = 0.9, tries = 1, turnOffMessages=True) # Finding amethystDartTip in inventory
        actions.click(chisX, chisY, sleepAfterClick=1) # Click on chisel
        actions.click(amethX, amethY, sleepAfterClick=1.5) # Click on amethyst ore
        actions.press('4')
        actions.click(468, 362, duration=[0.1, 1.1], sleepBeforeClick=35, sleepAfterClick=1) # Open bank
        actions.click(559, 85, duration=[0.1, 1.1], sleepAfterClick=1) # Open last tab
        x, y = actions.findImageOnScreen('amethystOre.png', 155, 105, 400, 100, findConfidence = 0.9, tries = 1, turnOffMessages=True)
    fletch()

def fletch():
    actions.formatPrint('Fletching')
    # actions.click(468, 362, duration=[0.1, 1.1], sleepAfterClick=1) # Open bank
    # actions.click(559, 85, duration=[0.1, 1.1], sleepAfterClick=1) # Open last tab
    actions.click(452, 499, duration=[0.1, 1.1], sleepAfterClick=1) # Click quantity all
    actions.click(563, 494, duration=[0.1, 1.1], sleepAfterClick=1) # Deposit all items
    # actions.click(265, 500, duration=[0.1, 1.1], sleepAfterClick=1) # Click withdraw item
    feathX, feathY = actions.findImageOnScreen('feather.png', 155, 105, 400, 100, findConfidence = 0.9, tries = 1, turnOffMessages=True)
    actions.click(feathX, feathY, duration=[0.1, 1.1], sleepAfterClick=1) # Click on feather
    amethX, amethY = actions.findImageOnScreen('amethystDartTip.png', 155, 105, 400, 100, findConfidence = 0.9, tries = 1, turnOffMessages=True)
    actions.click(amethX, amethY, duration=[0.1, 1.1], sleepAfterClick=1) # Click on amethyst dart tip (in bank)
    actions.click(605, 48, duration=[0.1, 1.1], sleepAfterClick=2) # Close the bank
    feathX, feathY = actions.findImageOnScreen('feather.png', 776, 395, 180, 255, findConfidence = 0.9, tries = 1, turnOffMessages=True) # Finding feather in inventory
    amethX, amethY = actions.findImageOnScreen('amethystDartTip.png', 776, 395, 180, 255, findConfidence = 0.9, tries = 1, turnOffMessages=True) # Finding amethystDartTip in inventory
    actions.click(amethX, amethY, sleepBeforeClick=2, sleepAfterClick=2, humanize=False)
    pyautogui.PAUSE = 0.01
    # while feathX is not False and amethX is not False:
    for i in range(0,1200):
        actions.click(amethX, amethY, humanize=False) # Click on amethystDartTip
        actions.click(feathX, feathY, humanize=False) # Click on feather
        # feathX, feathY = actions.findImageOnScreen('feather.png', 776, 395, 180, 255, findConfidence = 0.9, tries = 1, turnOffMessages=True) # Finding feather in inventory
        # amethX, amethY = actions.findImageOnScreen('amethystDartTip.png', 776, 395, 180, 255, findConfidence = 0.9, tries = 1, turnOffMessages=True) # Finding amethystDartTip in inventory
    pyautogui.PAUSE = 0.1
    actions.click(468, 362, duration=[0.1, 1.1], sleepAfterClick=1, sleepBeforeClick=2) # Open bank
    actions.click(563, 494, duration=[0.1, 1.1], sleepAfterClick=1) # Deposit all items
    actions.click(605, 48, duration=[0.1, 1.1], sleepAfterClick=2) # Close the bank



def start():
    actions.formatPrint('Game chat tab has to be open for this bot to work')
    actions.click(46, 675, duration=[0.1, 1.1], sleepAfterClick=0.2, sleepBeforeClick=3) # Clicks on all chat tab
    actions.click(104, 675, duration=[0.1, 1.1], sleepAfterClick=1) # Opens Game chat tab
    actions.clearConsole()
    while 1:
        howManyInventoriesBeforeFletching = 100
        mine(howManyInventoriesBeforeFletching)
        craft()

start()