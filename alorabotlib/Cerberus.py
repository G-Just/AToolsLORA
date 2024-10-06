import actions
import navigation
import procedure
import setup

def preFight():
    navigation.moveFromHomeToStalls()
    procedure.restoreHpAndPrayer()
    navigation.moveFromStallsAltarToStallsBank()
    navigation.moveFromStallsBankToCerberus()
    procedure.useBuffItem()
    actions.click(905, 35, duration=[0.1, 1.1], sleepAfterClick=6) #Click on minimap to boss
    procedure.clickQuickPrayer()
    procedure.summonGhost()
    actions.click(500, 285, duration=[0.1, 1.1]) #Click on minimap to boss
    

def fight():
    actions.formatPrint('Engaging in combat')
    while procedure.checkIfBossDead('CerberusBossRespawnTimer.png', True) != True:
        procedure.checkHealth()
        procedure.checkPrayer()
        procedure.checkForSpecialAttack()
        procedure.checkIfPlayerDead()
    actions.click(500, 284, duration=[0.1, 1.1], sleepAfterClick=2) #click offset to boss location
    for i in range(0,3):
        actions.click(501, 362, duration=[0.1, 1.1], sleepAfterClick=0.2) #click under your feet for loot  
    actions.teleportHome(1)
    
def start():
    while True: 
        preFight()
        actions.clearConsole()
        fight()
start()


