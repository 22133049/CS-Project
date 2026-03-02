import tkinter as tk
from tkinter import messagebox
from Order import placeOrder
from Account import EditAccount, deleteAccount



def MenuScreen():

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


    orderButton = tk.Button(menu,text= "Place Order", command = lambda: placeOrder(),padx = 5, pady = 5)
    orderButton.grid(row = 4, column = 0)

    tk.Label(menu,text="").grid(row=5,column=0)

    editButton = tk.Button(menu, text = "View or Edit Details", command = lambda: EditAccount(), padx = 5, pady = 5)
    editButton.grid(row = 6, column = 0)

    tk.Label(menu,text="").grid(row=7,column=0)


    tk.Label(menu,text="").grid(row=8,column=0)

    deleteButton = tk.Button(menu, text ="Delete Account",command = lambda: deleteAccount(menu),padx = 5, pady =5)
    deleteButton.grid(row = 9, column = 0)

    

    menu.mainloop()


if __name__ == "__main__":
    
    MenuScreen()



