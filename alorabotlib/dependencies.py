import pyautogui
import re
import time
import random
import sys
import os
import pyscreeze
import playsound
import subprocess
import sys
import traceback
import datetime

timing = [pyautogui.easeInQuad, pyautogui.easeOutQuad, pyautogui.easeInOutQuad, pyautogui.easeInBounce, pyautogui.easeInElastic]
linear = pyautogui.linear

absolutePath = os.path.dirname(__file__) + '\\resources\\'

def excepthook(type, value, tback):
    '''
    This function that will be called on an uncaught exception and log the error in resources/crashLog.txt
    
    '''
    msg = '\n' + '=' * 80 + '\n'
    msg += datetime.datetime.now().astimezone().strftime("%Y-%m-%d %H:%M:%S")
    msg += '\nUncaught exception:\n'
    msg += ''.join(traceback.format_exception(type, value, tback))
    msg += '=' * 80 + '\n'
    f = open(absolutePath + 'crashLog.txt', 'w')
    f.write(msg)
    f.close()
    playsound.playsound(absolutePath + 'crashSound.mp3')

# plug our handler into the python system
sys.excepthook = excepthook

