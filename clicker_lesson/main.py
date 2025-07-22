# python 3.11.4
# pip install PyAutoGUI
# pip install keyboard
# pip install opencv-python
import keyboard
import pyautogui


def clicker():
    while True:
        x = -1374
        y = 346

        pyautogui.click(x,y)

        if keyboard.is_pressed('Esc'):
            break



if __name__ == '__main__':
    clicker()