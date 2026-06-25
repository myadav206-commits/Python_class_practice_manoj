# from datetime import datetime

# current=datetime.now().today()
# print(current)

# from datetime import datetime

# current=datetime.now().strftime("%A %d-%B-%Y,%H:%M:%S")
# print(current)

import pyautogui
import time
time.sleep(4)
for i in range(10):
    pyautogui.typewrite("hello how are you",interval=0.5)