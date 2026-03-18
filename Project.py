
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import pickle
import random

from Account import SignUpScreen,LogInScreen
from Nav import goto

 

#MASTER FILE RUN PROJECT FROM THIS FILE
def MainScreen():

    root = tk.Tk()
    root.title("Daydreams and Party Things")
    root.configure(bg = "pink")
    root.geometry("600x400")
    root.columnconfigure(0, weight=1)
    root.columnconfigure(1, weight=1)
    root.columnconfigure(2, weight=1)

    

    style = ttk.Style()
    style.theme_use("clam")

    style.configure("Button.TButton",background = "white",foreground = "black",bordercolor = "#C2185B",
                    borderwidth = 2)

    style.configure("Label.TLabel",background = "pink", foreground = "White")
    

    MainScreen = ttk.Label(root, text = "Welcome!",style = "Label.TLabel", font = ("Arial",40,"bold"), anchor = "center")
    MainScreen.grid(row = 0, column = 0, columnspan = 3,pady = 40)


    SignUpButton = ttk.Button(root, text = "Sign Up!", style = "Button.TButton", command = lambda: goto(root,SignUpScreen))
    SignUpButton.grid(row = 3, column = 0,padx = 40,pady = 20,ipadx = 20,ipady = 10)

    filler = ttk.Label(root,text = "      ",style = "Label.TLabel")
    filler.grid(row = 3, column = 1)

    LogInButton = ttk.Button(root, text= "Log In!", style = "Button.TButton", command = lambda: goto(root,LogInScreen))
    LogInButton.grid(row = 3, column= 2,padx = 40,pady = 20,ipadx = 20,ipady = 10)


    root.mainloop()

if __name__ == "__main__":
     MainScreen()


