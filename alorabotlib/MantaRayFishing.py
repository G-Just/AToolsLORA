import actions
import navigation
import procedure
import setup

def fish():
    actions.click(503, 338,buttonType='right', duration=[0.1, 1.1], sleepAfterClick=1, sleepBeforeClick=1) # Right click fishing spot
    x, y = actions.findImageOnScreen('fishHarpoonWindowOption.png',250,250,600,600, findConfidence=0.9)
    actions.click(x,y, sleepBeforeClick=1, humanize=False)
    while procedure.checkIfInventoryFull('rawMantaRay.png') != True:
        pass
    actions.click(887, 178, duration=[0.1, 1.1], sleepAfterClick=7, sleepBeforeClick=1) # Minimap click near bank
    actions.click(406, 446, duration=[0.1, 1.1], sleepAfterClick=3, sleepBeforeClick=1) # Click on bank
    actions.click(929, 40, duration=[0.1, 1.1], sleepAfterClick=7, sleepBeforeClick=1) # Minimap click near fishing spot
    actions.click(552, 346, duration=[0.1, 1.1], sleepAfterClick=1, sleepBeforeClick=2) # Come near fishing spot
    
def start():
    navigation.moveFromHomeToDonatorZone()
    while 1:
        fish()
        
start()
