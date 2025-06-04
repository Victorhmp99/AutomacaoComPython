import pyautogui
pyautogui.PAUSE = 2

#pyautogui.click -> clicar
#pyautogui.press -> pressionar uma tecla
#pyautogui.write -> escrever

pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
pyautogui.click(x=461, y=941)
pyautogui.write("https://youtu.be/B8u3mDemb7Q?si=q1LprQfFkrREBOHu")
pyautogui.press("enter")
time.sleep(2) #pausa para clicar
pyautogui.click(x=1279, y=807)
pyautogui.click(x=1279, y=807)
