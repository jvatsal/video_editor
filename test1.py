import pyautogui
import time

screenWidth, screenHeight = pyautogui.size()
print(screenWidth, screenHeight)
pyautogui.moveTo(80, 900)

# # The path to the image file of the Notes app icon
# icon_path = '/Users/vatsaljoshi/Desktop/mhacks2024/hello.png'

# pyautogui.keyDown('command')
# pyautogui.press('space')
# pyautogui.keyUp('command')

# # Wait a bit for the Spotlight search field to focus
# time.sleep(1)
# # Type 'Notes' into the Spotlight search field
# pyautogui.write('Notes', interval=0.1)

# # Adding a brief pause before trying to locate and click might be helpful
# time.sleep(1)

# # Now find the Notes app icon in the Spotlight results and press enter to open it
# pyautogui.press('enter') 

# pyautogui.write('Penis banana', interval=0.1)
