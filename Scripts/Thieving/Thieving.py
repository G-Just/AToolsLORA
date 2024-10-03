import pyautogui
import pygetwindow
import time
import random
import re
import sys
import os
import keyboard

sys.path.append('../../')

import Setup

os.system('cls')
timing = [pyautogui.easeInQuad, pyautogui.easeOutQuad, pyautogui.easeInOutQuad, pyautogui.easeInBounce, pyautogui.easeInElastic]

def human_format(num):
    num = float('{:.3g}'.format(num))
    magnitude = 0
    while abs(num) >= 1000:
        magnitude += 1
        num /= 1000.0
    return '{}{}'.format('{:f}'.format(num).rstrip('0').rstrip('.'), ['', 'K', 'M', 'B', 'T'][magnitude])

def thieveLoop():
    pyautogui.moveTo(random.randint(580, 600), random.randint(300, 320), random.uniform(0.1, 0.6), random.choice(timing)) #Hover over stall
    pyautogui.click()
    time.sleep(random.uniform(0.1, 1))
    
def bankAllItemsFromStall(thievingIteration, crushedGemCount):
    print('>> Banking\n')
    pyautogui.moveTo(927, 90, random.uniform(0.1, 1.1), random.choice(timing)) #Move to bank from the stall
    pyautogui.click()
    time.sleep(5)
    pyautogui.moveTo(507, 277, random.uniform(0.1, 1.1), random.choice(timing)) #Open bank
    pyautogui.click()
    time.sleep(1)
    pyautogui.moveTo(563, 495, random.uniform(0.1, 1.1), random.choice(timing)) #Deposit all items
    pyautogui.click()
    print('>> Items deposited\n')
    time.sleep(1)
    print('>> Returning to stall\n')  
    pyautogui.moveTo(880, 132, random.uniform(0.1, 1.1), random.choice(timing)) #Minimap go back to stall
    pyautogui.click()
    time.sleep(5)
    os.system('cls')
    print(f'Starting next iteration. \nIteration count : [{thievingIteration}]\nCrushed gems banked : ~[{crushedGemCount}] = ~{human_format(crushedGemCount * 10000)} gp') 

def checkIfInventoryFull(): #checks if last inv spot is white
    if pyautogui.locateOnScreen('crushedGem.png', region=(910,614, 953, 648), confidence = 0.8) == None:
        return True
    else:
        print('>> Inventory is full\n')
        return False
def pause_script():
    if keyboard.is_pressed('page up'):
        print('>> Script paused [Page_Down to resume]')
        while True:
            if keyboard.is_pressed('page down'):
                print('>> Script resumed [hold Page_up to pause]')      
                break
def init():
        thievingIteration = 0
        crushedGemCount = 0
        print('>> Moving to the stall \n')
        time.sleep(1)
        pyautogui.moveTo(929, 44, random.uniform(0.1, 1.1), random.choice(timing)) #Move hover from home tp to stall
        pyautogui.click()
        time.sleep(7)
        print('>> Reached stall position\n')
        time.sleep(1)
        os.system('cls')
        print('>> Starting || Hold Page_up to pause script\n')
        while 1:
            while checkIfInventoryFull() is True:
                thieveLoop()
                pause_script()
            thievingIteration += 1
            crushedGemCount += 28
            bankAllItemsFromStall(thievingIteration, crushedGemCount)



time.sleep(1)
init()

