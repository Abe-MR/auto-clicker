#A simple Python auto-clicker
#Will click constantly at current mouse position
#Cannot cancel clicking at is happens

import sys
import pyautogui
import tkinter.messagebox
from tkinter import *
from tkinter.simpledialog import askstring
from pynput.keyboard import Key, Listener

# All initial variable declarations
boxTitle = "Mouse Clicker v.1.01"
msg1 = "Press F1 to enable mouse clicker."
msg2 = "Press F2 to disable mouse clicker."
msg3 = "Press F3 to change number of clicks"
lastMsg = "Disabled. Now closing program."
root = Tk()

root.withdraw()
tkinter.messagebox.showinfo(boxTitle, msg1 + "\n" + msg2)
tkinter.messagebox.showinfo(boxTitle, "Please do not remove cursor from desired click position")

#Get the initial click count from the user
while True:
    try:
        userInput = int(askstring(boxTitle, "Enter number of desired clicks"))
        if userInput < 1:
            raise ValueError
        break
    #Error when user doesn't input an integer or an integer greater than 0
    except ValueError:
        tkinter.messagebox.showinfo(boxTitle, "Input must be an integer and/or greater than 0")

#Read keys from user
def show(key):
    global userInput
    
    #If statements to check key input from user
    if key == Key.f1:
        x, y = pyautogui.position() #Starts mouse clicking at current position
        pyautogui.click(x, y, button = "left", clicks = userInput, interval = 0.02)
    if key == Key.f2:
        return False

with Listener(on_press = show) as listener:
    listener.join()

tkinter.messagebox.showinfo(boxTitle, lastMsg)
sys.exit() #Safely quit program