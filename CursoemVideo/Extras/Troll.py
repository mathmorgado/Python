import pyautogui as gui
import random, string, time

str = string.ascii_lowercase
quantidade = int(input('Quantidade: '))

time.sleep(5)

for i in range(quantidade):
    str = string.ascii_lowercase
    message = ''.join(random.sample(str, quantidade))
    gui.typewrite(message)
    gui.press('Enter')
