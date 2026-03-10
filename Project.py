
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import pickle
import random
from Account import SignUpScreen
from Nav import goto

 
from LogIn import LogInScreen

#MASTER FILE RUN PROJECT FROM THIS FILE
def MainScreen():

    root = tk.Tk()
    root.title("Daydreams and Party Things")
    root.configure(bg = "pink")

    

    style = ttk.Style()
    style.theme_use("clam")

    style.configure("Button.TButton",background = "white",foreground = "black",bordercolor = "#C2185B",
                    borderwidth = 2)

    style.configure("Label.TLabel",background = "pink", foreground = "White")
    

    MainScreen = ttk.Label(root, text = "Welcome!",style = "Label.TLabel", font = ("Arial",20,"bold"), anchor = "center")
    MainScreen.grid(row = 0, column = 0, columnspan = 2)


    SignUpButton = ttk.Button(root, text = "Sign Up!", style = "Button.TButton", command = lambda: goto(root,SignUpScreen))
    SignUpButton.grid(row = 3, column = 0)

    filler = ttk.Label(root,text = "      ",style = "Label.TLabel")
    filler.grid(row = 3, column = 1)

    LogInButton = ttk.Button(root, text= "Log In!", style = "Button.TButton", command = lambda: goto(root,LogInScreen))
    LogInButton.grid(row = 3, column= 2)


    root.mainloop()

if __name__ == "__main__":
     MainScreen()


