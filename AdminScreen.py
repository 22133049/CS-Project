import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from Account import regStaff, LogOut
from Product import addProd,editProd,deleteProd
from Inventory import openInv
from ViewAccounts import viewAccounts
from ViewReviews import viewReviews
from Order import viewOrders




def AdminScreen():

    menu = tk.Tk()

    menu.title("Admin Menu")
    menu.configure(bg = "black")

    style = ttk.Style()
    style.theme_use("clam")
    style.configure("BWhite.TLabel",background = "black",foreground = "white", font = ("Arial",30,"bold"))
    style.configure("FWhite.TLabel",background="black")
    style.configure("MWhite.TLabel",background = "black",foreground = "white", font = ("Arial",20,"bold"))

    style.configure("Button.TButton", background = "white",foreground = "black")

    menu.geometry("500x600")

    welcome = ttk.Label(menu,style = "BWhite.TLabel", text = "Welcome!",anchor = "center")
    welcome.grid(row=0,column = 0)
    menu.grid_columnconfigure(0, weight=1)

    filler = ttk.Label(menu,style = "FWhite.TLabel",text = "")
    filler.grid(row = 1, column = 0)

    option = ttk.Label(menu,style = "MWhite.TLabel",text ="What would you like to do?", font = ("Arial",20,'italic'),justify = "center")
    option.grid(row = 2, column = 0)

    filler2 = ttk.Label(menu,style = "FWhite.TLabel",text = "")
    filler2.grid(row = 3, column = 0)


    regButton = ttk.Button(menu,style = "Button.TButton",text= "Register New Staff Account", command = lambda: regStaff())
    regButton.grid(row = 4, column = 0)

    ttk.Label(menu,style = "FWhite.TLabel",text="").grid(row=5,column=0)

    addButton = ttk.Button(menu,style = "Button.TButton", text = "Add Product", command = lambda: addProd() )
    addButton.grid(row = 6, column = 0)

    ttk.Label(menu,style = "FWhite.TLabel",text="").grid(row=7,column=0)

    editButton = ttk.Button(menu,style = "Button.TButton", text = "Edit Products", command = lambda: editProd())
    editButton.grid(row = 8, column = 0)

    ttk.Label(menu,style = "FWhite.TLabel",text="").grid(row=9,column=0)

    deleteButton = ttk.Button(menu,style = "Button.TButton", text = "Delete a Product", command = lambda: deleteProd())
    deleteButton.grid(row = 10, column = 0)

    ttk.Label(menu,style = "FWhite.TLabel",text="").grid(row=11,column=0)

    ordButton = ttk.Button(menu,style = "Button.TButton",text = "View Orders", command = lambda: viewOrders() )
    ordButton.grid(row = 12, column = 0)

    
    ttk.Label(menu,style = "FWhite.TLabel",text="").grid(row=13,column=0)

    accButton = ttk.Button(menu,style = "Button.TButton",text = "View All Accounts",command = lambda: viewAccounts())
    accButton.grid(row = 14,column = 0)

    ttk.Label(menu,style = "FWhite.TLabel",text="").grid(row=15,column=0)

    revButton = ttk.Button(menu,style = "Button.TButton",text = "View All Accounts",command = lambda: viewReviews())
    revButton.grid(row = 16,column = 0)



    ttk.Label(menu,style = "FWhite.TLabel", text="").grid(row = 17, column = 0)

    invButton = ttk.Button(menu,style = "Button.TButton",text = "Add to/View Inventory", command = lambda: openInv() )
    invButton.grid(row = 18, column = 0)

    ttk.Label(menu,style = "FWhite.TLabel", text="").grid(row = 19, column = 0)

    ttk.Button(menu,style= "Button.TButton", text = "Log Out",command = lambda: LogOut(menu)).grid(row = 20, column = 0)


    

    menu.mainloop()


if __name__ == "__main__":
    
    AdminScreen()


