import pyautogui
import time
pyautogui.PAUSE = 3


#pyautogui.click -> clicar
#pyautogui.press -> pressionar uma tecla
#pyautogui.write -> escrever

pyautogui.press("win")
pyautogui.write("email")
pyautogui.press("enter")
time.sleep(10)
pyautogui.click(x=236, y=255)
time.sleep(5)
pyautogui.write("dayanea061@gmail.com")
time.sleep(4)
pyautogui.press("tab")
time.sleep(4)
pyautogui.press("tab")
pyautogui.press("tab")
pyautogui.write("Te amo dms Vida!")
pyautogui.click(x=456, y=314)
pyautogui.press("enter")