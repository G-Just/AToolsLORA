from pynput.mouse import Listener, Button
import pyautogui

def on_click(x, y, button, pressed):
    if pressed and button == Button.right:
        pic = pyautogui.screenshot(region=(x,y,1,1))
        r,g,b = pic.getpixel((0,0))
        print(f'x= {x} || y= {y} || r = {r}, g = {g}, b = {b}, {r,g,b}')

with Listener(on_click=on_click) as listener:
    listener.join()


