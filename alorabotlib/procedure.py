import actions
import navigation

def restoreHpAndPrayer():
    '''
    This function clicks on surgeon and altar (must be standing on stalls checkpoint)
    
    '''
    x, y = actions.findColorInRegion(425, 161, 300, 200, 255, 0, 255)
    if (x is not None and y is not None):
        actions.click(x, y, buttonType='right', duration = [0.2, 1])
        x, y = actions.findImageOnScreen('healWindowOption.png', 425, 161, 300, 200, 0.9, 20)
        if (x is not None and y is not None):
            actions.click(x, y, duration = [0.1, 1.1], sleepBeforeClick = 0.5, sleepAfterClick = 3, humanize = False) # Click on heal option
            actions.click(529, 314, duration = [0.1, 1.1], sleepBeforeClick = 0.5, sleepAfterClick = 1) # Click on altar

def checkPrayer():
    '''
    This function checks for prayer and acts accordingly
    
    '''
    lowPrayerPoint = actions.getScreenshot(968, 632, 1, 1)
    r,g,b = actions.getPixelColor(0, 0, lowPrayerPoint)
    if r == 40 and g == 35 and b == 28:
        actions.formatPrint('Low prayer detected -> drinking potion')
        actions.click(927,  417, duration = [0.1,0.5], sleepAfterClick = 0.2) # Restore potion

def checkForSpecialAttack():
    '''
    This function checks for special attack and acts accordingly
    
    '''
    lowSpecPoint = actions.getScreenshot(837, 180, 1, 1)
    r,g,b = actions.getPixelColor(0, 0, lowSpecPoint)
    if r == 52 and g == 170 and b == 199:
        actions.formatPrint('Using special attack')
        actions.click(838, 185, duration = [0.1,0.5],sleepAfterClick = 0.1) # Special attack widget

def checkIfPlayerDead():
    '''
    This function checks if player is dead and acts accordingly
    
    '''
    playerNoHealthPoint = actions.getScreenshot(546, 646, 1, 1)
    r,g,b = actions.getPixelColor(0, 0, playerNoHealthPoint)
    if r == 38 and g == 34 and b == 28:
        actions.formatPrint('You died.')
        actions.playSound('deathSound.mp3', 10)
        raise Exception("You died")

def checkHealth():
    '''
    This function checks for health and acts accordingly
    
    '''
    halfHealthPoint = actions.getScreenshot(755, 530)
    red, green, blue = actions.getPixelColor(0, 0, halfHealthPoint)
    if red == 51 and green == 47 and blue == 41:
        actions.formatPrint('Low health detected -> eating')
        # TODO: needs to be able to search for different food?
        x, y = actions.findImageOnScreen('mantaRay.png', 776, 395, 180, 255, findConfidence = 0.9, tries = 1) # Finding food in inventory

        # Only triggered when food is found
        if x is not False and y is not False: 
            actions.click(x, y, sleepBeforeClick = 0.1, humanize = False) # Click on food
            return
        # Only triggered when no food is found
        if x is False or y is False: 
            actions.formatPrint('No food detected -> leaving')
            actions.teleportHome(2)
            navigation.moveFromHomeToStalls()
            restoreHpAndPrayer()
            raise Exception("Failsafe activated (no food + low hp)")

def clickQuickPrayer():
    '''
    This function clicks on quick Prayer
    
    '''
    actions.click(814, 120, duration = [0.2, 0.5], sleepBeforeClick = 0.3) # Quick Prayer

def useBuffItem():
    '''
    This function clicks on buff item (1st slot)
    
    '''
    actions.click(802, 414, duration = [0.1, 1.1], sleepAfterClick = 0.5) #Click on first slot (buff item)

def summonGhost():
    '''
    This function clicks on summon ghost (blue)
    
    '''
    actions.press('f6')
    actions.click(825, 563, duration = [0.1, 1.1], sleepAfterClick = 0.2) #Click on ghost spell
    actions.press('esc')

def checkIfBossDead(bossIcon: str, pturnOffMessages: bool = False):
    '''
    This function returns if the provided boss timer is on the screen
    
    '''
    bossRespawnTimer, y = actions.findImageOnScreen(bossIcon, 19, 46, 200, 133, findConfidence = 0.9, tries = 1, turnOffMessages = pturnOffMessages)
    if bossRespawnTimer is not False:
        actions.formatPrint('Boss dead -> looting and leaving')
        clickQuickPrayer()
        return True
    else:
        return False

