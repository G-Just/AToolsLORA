import pyautogui

pyautogui.PAUSE = 0

count = 0
while count < 2000:
    pyautogui.click(802,413)
    pyautogui.click(842,415)
    count += 1