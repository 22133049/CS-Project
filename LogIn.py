import tkinter as tk
from tkinter import messagebox
import Account
import pickle
from MainMenu import MenuScreen
from AdminScreen import AdminScreen

def LogInScreen():

    root = tk.Tk()

    LogIn = tk.Label(root, text = "Log In", font =("Arial",20))
    LogIn.grid(row = 0, column = 0, columnspan = 2)

    eMailLabel = tk.Label(root, text = "E-Mail:")
    eMailLabel.grid(row = 1, column = 1)
    eMail = tk.Entry(root)
    eMail.grid(row = 1, column = 2)

    pWordLabel = tk.Label(root, text = "Password:")
    pWordLabel.grid(row = 2, column = 1)
    pWord = tk.Entry(root, show = "*")
    pWord.grid(row = 2, column = 2)


    Filler = tk.Label(root)
    Filler.grid(row = 7, column = 1, columnspan = 2)


    def LogIn():
        eMailentry = eMail.get()
        pWordentry = pWord.get()

        try:

            with open ("customers.pkl","rb") as file:
                my_objects = list(pickle.load(file))

        except EOFError:
            tk.messagebox.showerror("Error","File is empty, cannot read")
            return

        try:


            with open("staff.pkl","rb") as staff:
                my_staff = list(pickle.load(staff))

        except EOFError:
            tk.messagebox.showerror("Error","Staff file is empty, cannot read")
            return



        found = False

        for customer in my_objects:
            if customer.eMail == eMailentry and customer.pWord == pWordentry and found == False:
                found = True
                tk.messagebox.showinfo("Success","Logged In")
                with open("current_user.pkl","wb") as file:
                    pickle.dump(customer,file)
                root.destroy()


                MenuScreen()

                return

                
        for staff in my_staff:
            if staff.eMail == eMailentry and staff.pWord == pWordentry and found == False:
                found = True
                tk.messagebox.showinfo("success","Logged in")
                with open("current_user.pkl","wb") as file:
                    pickle.dump(staff,file)
                root.destroy()
                AdminScreen()
                return
                
                

        if found == False:
            tk.messagebox.showerror("Incoorect,""Username or Password incorrect")
                
            
        
            
            
            

    tk.Button(root, text = "Log In", command = lambda: LogIn()).grid(row = 8, column = 1, columnspan = 2)
    




