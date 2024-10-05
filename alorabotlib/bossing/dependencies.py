import pyautogui
import re
import time
import random
import sys
import os
import pyscreeze
from playsound import playsound
import subprocess
import sys
import traceback
from time import gmtime, strftime

timing = [pyautogui.easeInQuad, pyautogui.easeOutQuad, pyautogui.easeInOutQuad, pyautogui.easeInBounce, pyautogui.easeInElastic]
linear = pyautogui.linear

absolutePath = os.path.dirname(__file__) + '\\resources\\'

# the function that will be called on an uncaught exception
def excepthook(type, value, tback):
    msg = '\n' + '=' * 80 + '\n'
    msg += strftime("%Y-%m-%d %H:%M:%S", gmtime())
    msg += '\nUncaught exception:\n'
    msg += ''.join(traceback.format_exception(type, value, tback))
    msg += '=' * 80 + '\n'
    f = open(absolutePath + 'crashLog.txt', 'w')
    f.write(msg)
    f.close()

# plug our handler into the python system
sys.excepthook = excepthook

