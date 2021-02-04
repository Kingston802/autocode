import sys
import pyautogui
import keyboard 

if __name__ == "__main__":
    file = []
    if len(sys.argv) == 2:
        file = sys.argv[1]
        with open(file) as file:
            file = file.readlines()
    else:
        print("USAGE: python3 autocode.py filename")

    for line in file:
        keyboard.wait('up')
        pyautogui.write(line + '\n')

