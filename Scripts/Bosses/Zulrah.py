import pyautogui
import time
import random
import re
import sys
import os
import pyscreeze

sys.path.append('../../')
import Setup

os.system('cls')
timing = [pyautogui.easeInQuad, pyautogui.easeOutQuad, pyautogui.easeInOutQuad, pyautogui.easeInBounce, pyautogui.easeInElastic]

def checkHealthProcedure(): #This function checks the health bar and decides if to - eat / do nothing / tp out
    halfHealthPoint = pyautogui.screenshot(region=(755,530,1,1))
    r,g,b = halfHealthPoint.getpixel((0,0))
    if r == 51 and g == 47 and b == 41:
        print('>> Half health detected -> eating\n')
        try:
            x, y = pyautogui.locateCenterOnScreen('mantaRay.png', region=(776,395,180,250), confidence = 0.9)
            pyautogui.moveTo(x, y, 0.2) # Click on food
            time.sleep(0.1)
            pyautogui.click()
        except: #Except only triggered when no food is found
            print('>> No food detected -> leaving\n')
            pyautogui.press('f6')
            time.sleep(0.1)
            pyautogui.moveTo(788, 405) # Home tp
            time.sleep(0.1)
            pyautogui.click()
            time.sleep(1)
            pyautogui.press('esc')
            print('>> Resetting health and prayer\n')
            pyautogui.moveTo(924, 42, random.uniform(0.1, 1.1), random.choice(timing)) #Click near alter area
            pyautogui.click()
            time.sleep(7)
            pyautogui.moveTo(551, 207, random.uniform(0.1, 1.1), random.choice(timing)) #Right click on surgeon
            pyautogui.click(button='right')
            time.sleep(1)
            x, y = pyautogui.locateCenterOnScreen('healWindowOption.png', region=(435,194,250,260), confidence = 0.9)
            pyautogui.moveTo(x, y, random.uniform(0.1, 1.1)) #Click on heal
            pyautogui.click()
            time.sleep(6)
            pyautogui.moveTo(530, 316, random.uniform(0.1, 1.1), random.choice(timing)) #Click on altar
            pyautogui.click()
            raise Exception("Failsafe activated (no food + low hp)")

def preFightProcedure():
    os.system('cls')
    time.sleep(1)
    checkHealthProcedure()
    print('>> Resetting health and prayer\n')
    pyautogui.moveTo(924, 42, random.uniform(0.1, 1.1), random.choice(timing)) #Click near alter area
    pyautogui.click()
    time.sleep(7)
    pyautogui.moveTo(551, 207, random.uniform(0.1, 1.1), random.choice(timing)) #Right click on surgeon
    pyautogui.click(button='right')
    time.sleep(1)
    x, y = pyautogui.locateCenterOnScreen('healWindowOption.png', region=(435,194,250,260), confidence = 0.9)
    pyautogui.moveTo(x, y, random.uniform(0.1, 1.1)) #Click on heal
    pyautogui.click()
    time.sleep(6)
    pyautogui.moveTo(530, 316, random.uniform(0.1, 1.1), random.choice(timing)) #Click on altar
    pyautogui.click()
    time.sleep(4)
    print('>> Moving to bank\n')
    pyautogui.moveTo(651, 351, random.uniform(0.1, 1.1), random.choice(timing)) #Click on bank
    pyautogui.click()
    time.sleep(6)
    print('>> Preset activated, moving to boss\n')
    pyautogui.moveTo(849, 157, random.uniform(0.1, 1.1), random.choice(timing)) #Minimap click to wizard
    pyautogui.click()
    time.sleep(7)
    pyautogui.moveTo(466, 420, random.uniform(0.1, 1.1), random.choice(timing)) #Click on wizard
    pyautogui.click()
    time.sleep(2)
    pyautogui.moveTo(220, 413, random.uniform(0.1, 1.1), random.choice(timing)) #Click on favorite tab
    pyautogui.click()
    time.sleep(1)
    pyautogui.moveTo(357, 179, random.uniform(0.1, 1.1), random.choice(timing)) #Click on Zulrah tp
    pyautogui.click()
    time.sleep(5)
    pyautogui.moveTo(975, 91, random.uniform(0.1, 1.1), random.choice(timing)) #Click minimap near boat
    pyautogui.click()
    time.sleep(7)
    print('>> Entering boss arena\n')
    pyautogui.moveTo(554, 347, random.uniform(0.1, 1.1), random.choice(timing)) #Click on boat
    pyautogui.click()
    time.sleep(2)
    pyautogui.press('1') #Select 1st dialog option to enter Zulrah arena

def checkNorth(): # TOP SPOT
    return pyautogui.screenshot(region=(435,170,70,70))
        
def checkEast(): # RIGHT SPOT
    return pyautogui.screenshot(region=(740,150,70,70))
      
def checkWest(): # LEFT SPOT
    return pyautogui.screenshot(region=(220,170,70,70))
     
def checkSouth(): # BOTTOM SPOT
    return pyautogui.screenshot(region=(435,465,70,70))


def checkPrayerProcedure(): #This function checks the health bar and decides if to - drink pot / do nothing
    lowPrayerPoint = pyautogui.screenshot(region=(968,632,1,1))
    r,g,b = lowPrayerPoint.getpixel((0,0))
    if r == 40 and g == 35 and b == 28:
        print('>> Low prayer detected -> drinking potion\n')
        pyautogui.moveTo(927, 422) # Restore potion
        time.sleep(0.2)
        pyautogui.click()

def checkIfBossDeadProcedure():
    try:
        bossRespawnTimer = pyautogui.locateCenterOnScreen('bossRespawnTimer.png', region=(13,80,70,70), confidence = 0.9)
    except:
        bossRespawnTimer = None
    if bossRespawnTimer is not None:
        os.system('cls')
        print('>> Boss dead -> looting and leaving\n')
        pyautogui.moveTo(814, 120, random.uniform(0.2, 0.5), random.choice(timing)) # Quick Prayer
        pyautogui.click()
        pyautogui.moveTo(501, 362, random.uniform(0.1, 1.1), random.choice(timing)) #click under your feet for loot
        for i in range(0,4):
            pyautogui.click()
            time.sleep(1)
        pyautogui.press('f6')
        time.sleep(0.1)
        pyautogui.moveTo(788, 405) # Home tp
        time.sleep(0.1)
        pyautogui.click()
        time.sleep(1)
        pyautogui.press('esc')
        return True
    else:
        return False
        
def fightProcedure():
    os.system('cls')
    pyautogui.moveTo(814, 120, random.uniform(0.2, 0.5), random.choice(timing)) # Quick Prayer
    pyautogui.click()
    time.sleep(3)
    pyautogui.moveTo(498, 204, random.uniform(0.2, 0.5), random.choice(timing)) # Click on boss to engage
    pyautogui.click()
    time.sleep(2)
    print('>> Engaging in combat\n')
    currentColor = 'green' #Starting color is always green
    while checkIfBossDeadProcedure() != True:
        checkHealthProcedure()
        checkPrayerProcedure() 
        bossLocations = {'north': [checkNorth(),{'x':500,"y":196}], 'east': [checkEast(),{'x':778,'y':219}], 'west': [checkWest(),{'x':225,'y':221}], 'south':[checkSouth(),{'x':500,'y':522}]}
        pixelFound = False
        for location in bossLocations:
            if currentColor == 'green':
                width, height = bossLocations[location][0].size
                for x in range(0,width):
                    for y in range(0,height):
                        r,g,b = bossLocations[location][0].getpixel((x,y))
                        if r in range(115, 125) and g in range(25,35) and b in range(175,185): # Blue boss color
                            pyautogui.moveTo(bossLocations[location][1]['x'], bossLocations[location][1]['y'], random.uniform(0.2, 0.5), random.choice(timing)) # Click on boss
                            pyautogui.click()
                            pixelFound = True
                            currentColor = 'blue'
                            print(f'>> LOCATION: {location} || COLOR: {currentColor}\n')
                            pyautogui.press('f5')
                            time.sleep(0.1)
                            pyautogui.moveTo(825, 529, random.uniform(0.2, 0.5), random.choice(timing)) # Magic prayer
                            time.sleep(0.1)
                            pyautogui.click()
                            time.sleep(0.5)
                            pyautogui.press('esc')
                            break
                        elif r in range(190,200) and g in range(80,90) and b in range(20,30): # Red boss color
                            pyautogui.moveTo(bossLocations[location][1]['x'], bossLocations[location][1]['y'], random.uniform(0.2, 0.5), random.choice(timing)) # Click on boss
                            pyautogui.click()
                            pixelFound = True
                            currentColor = 'red'
                            print(f'>> LOCATION: {location} || COLOR: {currentColor}\n')
                            pyautogui.press('f5')
                            time.sleep(0.1)
                            pyautogui.moveTo(897, 529, random.uniform(0.2, 0.5), random.choice(timing)) # Melee prayer
                            time.sleep(0.1)
                            pyautogui.click()
                            time.sleep(0.5)
                            pyautogui.press('esc')
                            break
                    if pixelFound == True:
                        break
            elif currentColor == 'blue':
                width, height = bossLocations[location][0].size
                for x in range(0,width):
                    for y in range(0,height):
                        r,g,b = bossLocations[location][0].getpixel((x,y))
                        if r in range(90,100) and g in range(70,90) and b in range(30,40): # Green boss color
                            pyautogui.moveTo(bossLocations[location][1]['x'], bossLocations[location][1]['y'], random.uniform(0.2, 0.5), random.choice(timing)) # Click on boss
                            pyautogui.click()
                            pixelFound = True
                            currentColor = 'green'
                            print(f'>> LOCATION: {location} || COLOR: {currentColor}\n')
                            pyautogui.press('f5')
                            time.sleep(0.1)
                            pyautogui.moveTo(861, 529, random.uniform(0.2, 0.5), random.choice(timing)) # Ranged Prayer
                            time.sleep(0.1)
                            pyautogui.click()
                            time.sleep(0.5)
                            pyautogui.press('esc')
                            break
                        elif r in range(190,200) and g in range(80,90) and b in range(20,30): # Red boss color
                            pyautogui.moveTo(bossLocations[location][1]['x'], bossLocations[location][1]['y'], random.uniform(0.2, 0.5), random.choice(timing)) # Click on boss
                            pyautogui.click()
                            pixelFound = True
                            currentColor = 'red'
                            print(f'>> LOCATION: {location} || COLOR: {currentColor}\n')
                            pyautogui.press('f5')
                            time.sleep(0.1)
                            pyautogui.moveTo(897, 529, random.uniform(0.2, 0.5), random.choice(timing)) # Melee prayer
                            time.sleep(0.1)
                            pyautogui.click()
                            time.sleep(0.5)
                            pyautogui.press('esc')
                            break
                    if pixelFound == True:
                        break
            else:
                width, height = bossLocations[location][0].size
                for x in range(0,width):
                    for y in range(0,height):
                        r,g,b = bossLocations[location][0].getpixel((x,y))
                        if r in range(90,100) and g in range(70,90) and b in range(30,40): # Green boss color
                            pyautogui.moveTo(bossLocations[location][1]['x'], bossLocations[location][1]['y'], random.uniform(0.2, 0.5), random.choice(timing)) # Click on boss
                            pyautogui.click()
                            pixelFound = True
                            currentColor = 'green'
                            print(f'>> LOCATION: {location} || COLOR: {currentColor}\n')
                            pyautogui.press('f5')
                            time.sleep(0.1)
                            pyautogui.moveTo(861, 529, random.uniform(0.2, 0.5), random.choice(timing)) # Ranged Prayer
                            time.sleep(0.1)
                            pyautogui.click()
                            time.sleep(0.5)
                            pyautogui.press('esc')
                            break
                        elif r in range(115, 125) and g in range(25,35) and b in range(175,185): # Blue boss color
                            pyautogui.moveTo(bossLocations[location][1]['x'], bossLocations[location][1]['y'], random.uniform(0.2, 0.5), random.choice(timing)) # Click on boss
                            pyautogui.click()
                            pixelFound = True
                            currentColor = 'blue'
                            print(f'>> LOCATION: {location} || COLOR: {currentColor}\n')
                            pyautogui.press('f5')
                            time.sleep(0.1)
                            pyautogui.moveTo(825, 529, random.uniform(0.2, 0.5), random.choice(timing)) # Magic prayer
                            time.sleep(0.1)
                            pyautogui.click()
                            time.sleep(0.5)
                            pyautogui.press('esc')
                            break
                    if pixelFound == True:
                        break                 

def start():
    while True: 
        preFightProcedure()
        fightProcedure()

start()