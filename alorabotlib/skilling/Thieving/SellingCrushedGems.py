import pyautogui
import pygetwindow
import time
import random
import re
import sys
import os

sys.path.append('../../')

import Setup

os.system('cls')
timing = [pyautogui.easeInQuad, pyautogui.easeOutQuad, pyautogui.easeInOutQuad, pyautogui.easeInBounce, pyautogui.easeInElastic]

def sellingProcedure():
    print('>> Looking for the trader (this could take a moment)\n') 
    pixelFound = False
    while pixelFound == False:
        pic = pyautogui.screenshot(region=(100,100,700,400))
        width, height = pic.size
        for x in range(0,width,2):
            for y in range(0,height,2):
                r,g,b = pic.getpixel((x,y))
                if r == 255 and g == 0 and b == 255:
                    pyautogui.moveTo(100 + x, 100 + y, 0, random.choice(timing))
                    pyautogui.click(button='right')
                    pixelFound = True
                    break
            if pixelFound == True:
                print('>> Trader found\n') 
                break
    time.sleep(1)
    print('>> Looking for trade menu option (this could take a moment)\n') 
    while True:
        pic2 = pyautogui.locateCenterOnScreen('tradeWindowOption.png', region=(0,10,900,650), confidence = 0.8)
        if(pic2 is not None):
            x, y = pic2
            break
    print('>> Trading\n') 
    pyautogui.moveTo(x, y, 0)
    pyautogui.click()
    time.sleep(4)
    pyautogui.moveTo(801, 416)
    time.sleep(1)
    pyautogui.click(button='right')
    time.sleep(1)
    pyautogui.moveTo(801, 533)
    pyautogui.click()
    os.system('cls')
    
def bankingProcedure():
    print('>> Moving near the bank\n') 
    pic = pyautogui.screenshot(region=(860,85,100,60)) #Screenshot minimap
    width, height = pic.size
    pixelFound = False
    for x in range(0,width):
        for y in range(0,height):
            r,g,b = pic.getpixel((x,y))
            if r in range(120,160) and g in range(240,256) and b in range(250,256):
                pyautogui.moveTo(862 + x, 90 + y, 0, random.choice(timing))
                pyautogui.click()
                pixelFound = True
                break
        if pixelFound == True:
            break
    time.sleep(5)
    print('>> Accessing bank\n') 
    pyautogui.moveTo(507, 277, random.uniform(0.1, 1.1), random.choice(timing)) #Open bank
    pyautogui.click()
    time.sleep(1)
    pyautogui.moveTo(563, 495, random.uniform(0.1, 1.1), random.choice(timing)) #Deposit all items
    pyautogui.click()
    time.sleep(1)
    invX, invY = pyautogui.locateCenterOnScreen('crushedGem.png', region=(135,90,480,400), confidence = 0.9)
    pyautogui.moveTo(invX, invY, random.uniform(0.1, 1.1), random.choice(timing)) #take out gems
    pyautogui.click()
    time.sleep(1)
    print('>> Items deposited, returning\n')  
    pyautogui.moveTo(890, 123, random.uniform(0.1, 1.1), random.choice(timing))
    pyautogui.click()
    time.sleep(4)
    print('>> Reached the area\n')
    os.system('cls')

def start():
    print('>> Moving to the area')
    time.sleep(1)
    pyautogui.moveTo(929, 44, random.uniform(0.1, 1.1), random.choice(timing)) #Move hover from home tp to stall
    pyautogui.click()
    time.sleep(7)
    pyautogui.moveTo(913, 102, random.uniform(0.1, 1.1), random.choice(timing)) #Move hover from home tp to stall
    pyautogui.click()
    print('>> Reached the area\n')
    time.sleep(2)
    os.system('cls')
    while 1:
        bankingProcedure()
        time.sleep(0.5)
        sellingProcedure()

start()