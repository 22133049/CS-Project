
import tkinter as tk
from tkinter import messagebox
import pickle
import random
from Account import SignUpScreen
from Nav import goto

 
from LogIn import LogInScreen


def MainScreen():

    root = tk.Tk()

    root.geometry("300x300")
    

    MainScreen = tk.Label(root, text = "Welcome!", font = "Arial", anchor = "center")
    MainScreen.grid(row = 0, column = 0, columnspan = 2)


    SignUpButton = tk.Button(root, text = "Sign Up!", command = lambda: goto(root,SignUpScreen))
    SignUpButton.grid(row = 3, column = 0)

    filler = tk.Label(text = "      ")
    filler.grid(row = 3, column = 1)

    LogInButton = tk.Button(root, text= "Log In!", command = lambda: goto(root,LogInScreen))
    LogInButton.grid(row = 3, column= 2)


    root.mainloop()

if __name__ == "__main__":
     MainScreen()

