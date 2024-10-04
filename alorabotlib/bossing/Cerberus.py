import pyautogui
import time
import random
import re
import sys
import os
import pyscreeze
from playsound import playsound

os.system('cls')
timing = [pyautogui.easeInQuad, pyautogui.easeOutQuad, pyautogui.easeInOutQuad, pyautogui.easeInBounce, pyautogui.easeInElastic]

try:
    def checkHealthProcedure(): #This function checks the health bar and decides if to - eat / do nothing / tp out
        halfHealthPoint = pyautogui.screenshot(region=(755,530,1,1))
        r,g,b = halfHealthPoint.getpixel((0,0))
        if r == 51 and g == 47 and b == 41:
            print('>> Half health detected -> eating\n')
            try:
                x, y = pyautogui.locateCenterOnScreen('../Common/mantaRay.png', region=(776,395,180,250), confidence = 0.9)
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
                x, y = pyautogui.locateCenterOnScreen('../Common/healWindowOption.png', region=(435,194,250,260), confidence = 0.9)
                pyautogui.moveTo(x, y, random.uniform(0.1, 1.1)) #Click on heal
                pyautogui.click()
                time.sleep(6)
                pyautogui.moveTo(530, 316, random.uniform(0.1, 1.1), random.choice(timing)) #Click on altar
                pyautogui.click()
                raise Exception("Failsafe activated (no food + low hp)")

    def checkPrayerProcedure(): #This function checks the health bar and decides if to - drink pot / do nothing
        lowPrayerPoint = pyautogui.screenshot(region=(968,632,1,1))
        r,g,b = lowPrayerPoint.getpixel((0,0))
        if r == 40 and g == 35 and b == 28:
            print('>> Low prayer detected -> drinking potion\n')
            pyautogui.moveTo(927, 422) # Restore potion
            time.sleep(0.2)
            pyautogui.click()
          
    def checkForSpecialAttackProcedure(): #This function checks the special bar and decides if to - use spec / do nothing
        lowSpecPoint = pyautogui.screenshot(region=(837,180,1,1))
        r,g,b = lowSpecPoint.getpixel((0,0))
        if r == 52 and g == 170 and b == 199:
            notFullHealthPoint = pyautogui.screenshot(region=(755,482,1,1))
            r1,g1,b1 = notFullHealthPoint.getpixel((0,0))
            if r1 == 51 and g1 == 47 and b1 == 41:
                print('>> Using special attack\n')
                pyautogui.moveTo(838,185) # Special attack widget
                time.sleep(0.1)
                pyautogui.click()
            
    def checkIfPlayerDeadProcedure():
        playerNoHealthPoint = pyautogui.screenshot(region=(546,646,1,1))
        r,g,b = playerNoHealthPoint.getpixel((0,0))
        if r == 38 and g == 34 and b == 28:
            print('>> You died.\n')
            playsound('deathSound.mp3')
            time.sleep(10)
            raise Exception("You died")
    
    def checkIfBossDeadProcedure():
        try:
            bossRespawnTimer = pyautogui.locateCenterOnScreen('bossRespawnTimer.png', region=(19,46,188,133), confidence = 0.9)
        except:
            bossRespawnTimer = None
        if bossRespawnTimer is not None:
            os.system('cls')
            print('>> Boss dead -> looting and leaving\n')
            pyautogui.moveTo(814, 120, random.uniform(0.2, 0.5), random.choice(timing)) # Quick Prayer
            pyautogui.click()
            pyautogui.moveTo(500, 284, random.uniform(0.1, 1.1), random.choice(timing)) #click up where drop appears
            pyautogui.click()
            time.sleep(2)
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
    
    def preFightProcedure():
        os.system('cls')
        time.sleep(1)
        print('>> Resetting health and prayer\n')
        pyautogui.moveTo(924, 42, random.uniform(0.1, 1.1), random.choice(timing)) #Click near alter area
        pyautogui.click()
        time.sleep(7)
        pyautogui.moveTo(551, 207, random.uniform(0.1, 1.1), random.choice(timing)) #Right click on surgeon
        pyautogui.click(button='right')
        time.sleep(1)
        while pyautogui.locateCenterOnScreen('../Common/healWindowOption.png', region=(435,194,250,260), confidence = 0.9) is not None:
            x, y = pyautogui.locateCenterOnScreen('../Common/healWindowOption.png', region=(435,194,250,260), confidence = 0.9)
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
        pyautogui.moveTo(218, 240, random.uniform(0.1, 1.1), random.choice(timing)) #Click on bosses tab
        pyautogui.click()
        time.sleep(1)
        pyautogui.moveTo(365, 299, random.uniform(0.1, 1.1), random.choice(timing)) #Click on cerberus tp
        pyautogui.click()
        time.sleep(4)
        pyautogui.moveTo(130, 45, random.uniform(0.1, 1.1), random.choice(timing)) #Click on wench (door to arena)
        pyautogui.click()
        time.sleep(9)
        pyautogui.moveTo(130, 45, random.uniform(0.1, 1.1), random.choice(timing)) #Click on wench (door to arena)
        pyautogui.click()
        time.sleep(3.5)
        pyautogui.moveTo(802, 414, random.uniform(0.1, 1.1), random.choice(timing)) #Click on first slot (buff item)
        pyautogui.click()
        time.sleep(1)
        pyautogui.moveTo(905, 55, random.uniform(0.1, 1.1), random.choice(timing)) #Click on minimap to boss
        pyautogui.click()
        time.sleep(3.5)
        pyautogui.press('f6')
        pyautogui.moveTo(825, 563, random.uniform(0.1, 1.1), random.choice(timing)) #Click on ghost spell
        pyautogui.click()
        time.sleep(0.3)
        pyautogui.press('esc')
        pyautogui.moveTo(814, 120, random.uniform(0.2, 0.5), random.choice(timing)) # Quick Prayer
        pyautogui.click()
        
    def fightProcedure():
        os.system('cls')
        print('>> Engaging in combat\n')
        while checkIfBossDeadProcedure() != True:
            checkHealthProcedure()
            checkPrayerProcedure()
            checkForSpecialAttackProcedure()
            checkIfPlayerDeadProcedure()

    def start():
        while True: 
            preFightProcedure()
            fightProcedure()

    start()
except:
    playsound('crashSound.mp3')
    time.sleep(30)
