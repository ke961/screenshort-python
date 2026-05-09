import pyautogui
import  time 
import os
import tkinter as tk
from tkinter import messagebox

os.makedirs('screenshots', exist_ok=True)


def take_screenshot():
   
    File_name=(f"screenshots/screenshot_{int(time.time())}.png1")
    pyautogui.screenshot(File_name)


    messagebox.showinfo("Successfull", "Screenshot has beentaken successfully!")


def Dashboard():
    root = tk.Tk()
    root.title("Screenshot App")
    root.geometry("300x200")





    root.mainloop()

Dashboard()