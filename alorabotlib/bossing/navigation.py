import actions

def moveFromHomeToStalls():
    '''
    This function navigates the player from home checkpoint to stalls checkpoint
    
    '''
    actions.formatPrint('Moving to stalls')
    actions.click(924, 42, duration=[0.1, 1.1], sleepAfterClick=7, sleepBeforeClick=1.5 ) # Click on stalls area in minimap

def moveFromStallsAltarToStallsBank():
    '''
    This function navigates the player from home checkpoint to stalls checkpoint
    
    '''
    actions.formatPrint('Moving to bank')
    actions.click(646, 347, duration=[0.1, 1.1], sleepAfterClick=1, buttonType='right') # Click stalls bank
    x, y=actions.findImageOnScreen('bankOption.png', 500, 250, 325, 200, 0.9, 20)
    if (x is not None and y is not None):
        actions.click(x, y, duration=[0.1, 1.1], sleepAfterClick=4, humanize=False)
    
def moveFromStallsBankToZulrah():
    '''
    This function navigates the player from stalls bank checkpoint to Zulrah arena

    '''
    actions.formatPrint('Moving from bank to Zulrah')
    actions.click(849, 157, duration=[0.1, 1.1], sleepAfterClick=7, sleepBeforeClick=1) #Minimap click to wizard
    actions.click(466, 420, duration=[0.1, 1.1], sleepAfterClick=2 ) #Click on wizard
    actions.click(220, 413, duration=[0.1, 1.1], sleepAfterClick=1 ) #Click on favorite tab
    actions.click(357, 179, duration=[0.1, 1.1], sleepAfterClick=5 ) #Click on Zulrah tp
    actions.click(975, 91, duration=[0.1, 1.1], sleepAfterClick=7 ) #Click minimap near boat
    actions.formatPrint('Entering boss arena')
    actions.click(554, 347, duration=[0.1, 1.1], sleepAfterClick=2 ) #Click on boat
    actions.press('1') #Select 1st dialog option to enter Zulrah arena

def moveFromStallsBankToCerberus():
    actions.formatPrint('Moving from bank to Cerberus')
    actions.click(849, 157, duration=[0.1, 1.1], sleepAfterClick=7, sleepBeforeClick=1) #Minimap click to wizard
    actions.click(466, 420, duration=[0.1, 1.1], sleepAfterClick=2 ) #Click on wizard
    actions.click(218, 240, duration=[0.1, 1.1], sleepAfterClick=1) #Click on bosses tab
    actions.click(365, 299, duration=[0.1, 1.1], sleepAfterClick=4) #Click on cerberus tp
    actions.click(130, 45, duration=[0.1, 1.1], sleepAfterClick=13) #Click on wench (door to arena)
    