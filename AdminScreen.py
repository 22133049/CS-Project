import tkinter as tk
from tkinter import messagebox
from Account import regStaff
from Product import addProd,editProd
from Inventory import openInv
from ViewAccounts import viewAccounts
from Order import viewOrders




def AdminScreen():

    menu = tk.Tk()

    menu.geometry("500x500")

    welcome = tk.Label(menu,text = "Welcome!",font = ("Arial",30,'bold'),anchor = "center")
    welcome.grid(row=0,column = 0)
    menu.grid_columnconfigure(0, weight=1)

    filler = tk.Label(menu,text = "")
    filler.grid(row = 1, column = 0)

    option = tk.Label(menu,text ="What would you like to do?", font = ("Arial",20,'italic'),justify = "center")
    option.grid(row = 2, column = 0)

    filler2 = tk.Label(menu,text = "")
    filler2.grid(row = 3, column = 0)


    regButton = tk.Button(menu,text= "Register New Staff Account", command = lambda: regStaff(),padx = 5, pady = 5)
    regButton.grid(row = 4, column = 0)

    tk.Label(menu,text="").grid(row=5,column=0)

    addButton = tk.Button(menu, text = "Add Product", command = lambda: addProd(), padx = 5, pady = 5)
    addButton.grid(row = 6, column = 0)

    tk.Label(menu,text="").grid(row=7,column=0)

    editButton = tk.Button(menu, text = "Edit Products", command = lambda: editProd(), padx =5, pady = 5)
    editButton.grid(row = 8, column = 0)

    tk.Label(menu,text="").grid(row=9,column=0)

    ordButton = tk.Button(menu,text = "View Orders", command = lambda: viewOrders(), padx = 5, pady = 5)
    ordButton.grid(row = 10, column = 0)

    
    tk.Label(menu,text="").grid(row=11,column=0)

    accButton = tk.Button(menu,text = "View All Accounts",command = lambda: viewAccounts(), padx = 5,pady = 5)
    accButton.grid(row = 12,column = 0)

    tk.Label(menu,text="").grid(row=13,column=0)



    tk.Label(menu, text="").grid(row = 14, column = 0)

    invButton = tk.Button(menu,text = "Add to/View Inventory", command = lambda: openInv(), padx = 5, pady = 5)
    invButton.grid(row = 15, column = 0)


    

    menu.mainloop()


if __name__ == "__main__":
    
    AdminScreen()


