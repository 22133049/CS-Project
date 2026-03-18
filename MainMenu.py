import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from Order import placeOrder, cancelOrder
from ViewReviews import leaveReview
from Account import EditAccount, deleteAccount, LogOut



def MenuScreen():

    menu = tk.Tk()
    menu.title("Main Menu")

    menu.configure(bg = "pink")

    style = ttk.Style()
    style.theme_use("clam")

    style.configure("Button.TButton",background = "white",foreground = "black",bordercolor = "#C2185B",
                    borderwidth = 2)

    style.configure("Label.TLabel",background = "pink", foreground = "White")

    

    menu.geometry("500x500")

    welcome = ttk.Label(menu,text = "Welcome!",font = ("Arial",30,'bold'),style = "Label.TLabel",anchor = "center")
    welcome.grid(row=0,column = 0)
    menu.grid_columnconfigure(0, weight=1)

    filler = ttk.Label(menu,text = "",style = "Label.TLabel")
    filler.grid(row = 1, column = 0)

    option = ttk.Label(menu,text ="What would you like to do?", font = ("Arial",20,'italic'),style = "Label.TLabel",justify = "center")
    option.grid(row = 2, column = 0)

    filler2 = ttk.Label(menu,text = "",style = "Label.TLabel")
    filler2.grid(row = 3, column = 0)


    orderButton = ttk.Button(menu,text= "Place Order",style = "Button.TButton", command = lambda: placeOrder())
    orderButton.grid(row = 4, column = 0,padx = 5, pady = 5)

    ttk.Label(menu,text="",style = "Label.TLabel").grid(row=5,column=0)

    editButton = ttk.Button(menu, text = "View or Edit Details",style = "Button.TButton", command = lambda: EditAccount())
    editButton.grid(row = 6, column = 0, padx = 5, pady = 5)

    ttk.Label(menu,text="",style = "Label.TLabel").grid(row=7,column=0)

    ttk.Button(menu,text = "Cancel Order",style = "Button.TButton", command = lambda:cancelOrder()).grid(row = 8, column = 0)


    ttk.Label(menu,text="",style = "Label.TLabel").grid(row=9,column=0)

    ttk.Button(menu,text = "Leave Review",style = "Button.TButton", command = lambda:leaveReview()).grid(row = 10, column = 0)

    ttk.Label(menu,text="",style = "Label.TLabel").grid(row=11,column=0)
    

    deleteButton = ttk.Button(menu, text ="Delete Account",style = "Button.TButton",command = lambda: deleteAccount(menu))
    deleteButton.grid(row = 12, column = 0,padx = 5, pady =5)

    ttk.Label(menu,style = "Label.TLabel", text="").grid(row = 13, column = 0)

    ttk.Button(menu,style= "Button.TButton", text = "Log Out",command = lambda: LogOut(menu)).grid(row = 14, column = 0)

    

    menu.mainloop()


if __name__ == "__main__":
    
    MenuScreen()



