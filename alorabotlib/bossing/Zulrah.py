import actions
import navigation
import procedure
import setup

try:
    def preFight():
        navigation.moveFromHomeToStalls()
        procedure.restoreHpAndPrayer()
        navigation.moveFromStallsAltarToStallsBank()
        navigation.moveFromStallsBankToZulrah()
        procedure.quickPrayer()
        procedure.useBuffItem()
        procedure.summonGhost()

    def checkNorth(): # TOP SPOT
        return actions.getScreenshot(435, 170, 70, 70)
            
    def checkEast(): # RIGHT SPOT
        return actions.getScreenshot(740, 150, 70, 70)
        
    def checkWest(): # LEFT SPOT
        return actions.getScreenshot(220, 170, 70, 70)
        
    def checkSouth(): # BOTTOM SPOT
        return actions.getScreenshot(435, 465, 70, 70)
            
    def fight():
        actions.click(498, 204, duration = [0.2, 0.5], sleepAfterClick = 2) # Click on boss to engage
        actions.formatPrint('Engaging in combat')
        currentColor = 'green' #Starting color is always green
        while procedure.checkIfBossDead('ZulrahBossRespawnTimer.png', True) == False:
            procedure.checkIfPlayerDead()
            procedure.checkHealth()
            procedure.checkPrayer()
            bossLocations = {'north': [checkNorth(),{'x':500,"y":196}], 'east': [checkEast(),{'x':778,'y':219}], 'west': [checkWest(),{'x':225,'y':221}], 'south':[checkSouth(),{'x':500,'y':522}]}
            pixelFound = False
            for location in bossLocations:
                if currentColor == 'green':
                    width, height = bossLocations[location][0].size
                    for x in range(0,width):
                        for y in range(0,height):
                            r,g,b = actions.getPixelColor(x, y, bossLocations[location][0])
                            if r in range(115, 125) and g in range(25,35) and b in range(175,185): # Blue boss color
                                actions.click(bossLocations[location][1]['x'], bossLocations[location][1]['y'], duration = [0.2, 0.5]) # Click on boss
                                pixelFound = True
                                currentColor = 'blue'
                                actions.formatPrint(f'LOCATION: {location} || COLOR: {currentColor}')
                                actions.press('f5', 0.1)
                                actions.click(825, 529, duration = [0.2, 0.5], sleepAfterClick = 0.6) # Magic prayer                  
                                actions.press('esc')
                                procedure.checkForSpecialAttack()
                                break
                            elif r in range(190,200) and g in range(80,90) and b in range(20,30): # Red boss color
                                actions.click(bossLocations[location][1]['x'], bossLocations[location][1]['y'], duration = [0.2, 0.5]) # Click on boss
                                pixelFound = True
                                currentColor = 'red'
                                actions.formatPrint(f'LOCATION: {location} || COLOR: {currentColor}')
                                actions.press('f5', 0.1)
                                actions.click(897, 529, duration = [0.2, 0.5], sleepAfterClick = 0.6) # Melee prayer                  
                                actions.press('esc')
                                break
                        if pixelFound == True:
                            break
                elif currentColor == 'blue':
                    width, height = bossLocations[location][0].size
                    for x in range(0,width):
                        for y in range(0,height):
                            r,g,b = bossLocations[location][0].getpixel((x,y))
                            if r in range(90,100) and g in range(70,90) and b in range(30,40): # Green boss color
                                actions.click(bossLocations[location][1]['x'], bossLocations[location][1]['y'], duration = [0.2, 0.5]) # Click on boss
                                pixelFound = True
                                currentColor = 'green'
                                actions.formatPrint(f'LOCATION: {location} || COLOR: {currentColor}')
                                actions.press('f5', 0.1)
                                actions.click(861, 529, duration = [0.2, 0.5], sleepAfterClick = 0.6) # Ranged Prayer                  
                                actions.press('esc')
                                break
                            elif r in range(190,200) and g in range(80,90) and b in range(20,30): # Red boss color
                                actions.click(bossLocations[location][1]['x'], bossLocations[location][1]['y'], duration = [0.2, 0.5]) # Click on boss
                                pixelFound = True
                                currentColor = 'red'
                                actions.formatPrint(f'LOCATION: {location} || COLOR: {currentColor}')
                                actions.press('f5', 0.1)
                                actions.click(897, 529, duration = [0.2, 0.5], sleepAfterClick = 0.6) # Melee prayer                  
                                actions.press('esc')
                                break
                        if pixelFound == True:
                            break
                else:
                    width, height = bossLocations[location][0].size
                    for x in range(0,width):
                        for y in range(0,height):
                            r,g,b = bossLocations[location][0].getpixel((x,y))
                            if r in range(90,100) and g in range(70,90) and b in range(30,40): # Green boss color
                                actions.click(bossLocations[location][1]['x'], bossLocations[location][1]['y'], duration = [0.2, 0.5]) # Click on boss
                                pixelFound = True
                                currentColor = 'green'
                                actions.formatPrint(f'LOCATION: {location} || COLOR: {currentColor}')
                                actions.press('f5', 0.1)
                                actions.click(861, 529, duration = [0.2, 0.5], sleepAfterClick = 0.6) # Ranged Prayer                  
                                actions.press('esc')
                                break
                            elif r in range(115, 125) and g in range(25,35) and b in range(175,185): # Blue boss color
                                actions.click(bossLocations[location][1]['x'], bossLocations[location][1]['y'], duration = [0.2, 0.5]) # Click on boss
                                pixelFound = True
                                currentColor = 'blue'
                                actions.formatPrint(f'LOCATION: {location} || COLOR: {currentColor}')
                                actions.press('f5', 0.1)
                                actions.click(825, 529, duration = [0.2, 0.5], sleepAfterClick = 0.6) # Magic prayer                  
                                actions.press('esc')
                                procedure.checkForSpecialAttack()
                                break
                        if pixelFound == True:
                            break                 

    def start():
        while True: 
            preFight()
            actions.clearConsole()
            fight()

    start()
except:
    actions.playsound('crashSound.mp3', 30)

start()
