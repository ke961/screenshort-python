import pyautogui
import  time 
import os
import tkinter as tk
from tkinter import messagebox

os.makedirs('screenshots', exist_ok=True)


def take_screenshot():
   
    File_name=(f"screenshots/screenshot_{int(time.time())}.png.png")
    pyautogui.screenshot(File_name)


    messagebox.showinfo("Successfull", "Screenshot has beentaken successfully!")


def Dashboard():
    root = tk.Tk()
    root.title("Screenshot App")
    root.geometry("500x500")
    background_color = "#98976b"
    root.configure(bg=background_color)

   



    lable= tk.Label(root, 
                    text= "Click the button below to take a screenshot",
                    font= ("Arial", 14)
                    ,bg=background_color

                      )
    
    lable.pack(pady=20)

    


    def on_button_click():
       take_screenshot()


    button = tk.Button(root, text="Take Screenshot", command=on_button_click ,
                       fg="Black", font=("Arial", 12))
    button.pack(pady=20)

    button_show= tk.Button(root, text="Show Screenshots", fg="Black",font=("Arial", 12),
                           command=lambda: os.startfile('screenshots'))
    button_show.pack(pady=10)

    button_exit = tk.Button(root, text="Exit", 
                            fg="Black", font=("Arial", 12),
                            command=root.destroy)
    button_exit.pack(pady=10)


    root.mainloop()

Dashboard()