import pyautogui
import time

message = "modyar koe tak hack!!!"
n = 100

time.sleep(2)

for i in range(n):
    pyautogui.typewrite(message + '\n')
