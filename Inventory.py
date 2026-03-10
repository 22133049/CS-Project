import tkinter as tk
from tkinter import messagebox, ttk, END
import pickle
from Classes.Stock import Stock


def openInv():
    root = tk.Tk()
    root.title("Inventory")
    root.configure(bg = "black")
    root.geometry("300x300")
    style = ttk.Style(root)
    style.theme_use("clam")
    style.configure("Text.TLabel",background = "black",foreground = "white", font = ("Arial",20,"bold"))
    style.configure("BButton.TButton",background = "white",foreground = "black", bordercolor = "#000000")

    ttk.Label(root,style = "Text.TLabel", text = "Inventory").grid(row = 0, column = 0, anchor = "center")

                    

    Stocklist = tk.Listbox(root,height = 10, width = 15)

    try:

        with open("inventory.pkl","rb") as inv:
            stock = list(pickle.load(inv))

    except:
        stock = []

    if not stock:
        listbox.insert(0,"No Stock, please click Add Stock")

    else:
        
        CurrentStock = {}
        for obj in stock:
            CurrentStock[obj.name] = obj.quantity
    
        for name,qty in CurrentStock.items():
            
            Stocklist.insert(END,f"{name} ({qty})")

    Stocklist.grid(row = 1, column = 0)



    
    
        

    
    


    def getStock():

        with open("inventory.pkl","rb") as inv:
            stock = list(pickle.load(inv))

        tk.messagebox.showinfo("Current Stock",
                           "\n".join(str(item) for item in stock))

        root.destroy()


    def addStock():

        addmenu = tk.Toplevel(root)
        NameLabel = tk.Label(addmenu, text = "Name:")
        NameLabel.grid(row = 0, column = 0)
        Name = tk.Entry(addmenu)
        Name.grid(row = 0, column = 1)

        QuantityLabel = tk.Label(addmenu, text = "Quantity:")
        QuantityLabel.grid(row = 1, column = 0)
        Quantity = tk.Entry(addmenu)
        Quantity.grid(row = 1, column = 1)

        confirmButton = tk.Button(addmenu, text = "Confirm", command = lambda: confirm())
        confirmButton.grid(row = 2, column = 1, columnspan= 2)

        

        

        def confirm():

            name = Name.get()
            try:

                quantity = int(Quantity.get())

            except ValueError:
                tk.messagebox.showinfo("Failure","Quantity must be number")
                return

            

            
            temp = Stock(name,quantity)

            stockExists = False

            try:

                with open("inventory.pkl","rb") as file:
                    my_objects = list(pickle.load(file))

            except:
                my_objects = []
            
            for obj in my_objects:
                if obj.name == temp.name:
                    obj.quantity = obj.quantity + temp.quantity
                    stockExists = True

            if stockExists == False:
                my_objects.append(temp)

            
        
            with open("inventory.pkl","wb+") as file:
                pickle.dump(my_objects,file)

            tk.messagebox.showinfo("Success","Stock Added")

            addmenu.destroy()
            root.destroy()

 


    addButton = ttk.Button(root,style = "BButton.TButton", text = "Add Stock", command = lambda: addStock())
    addButton.grid(row = 1, column = 2)

    getButton = ttk.Button(root,style = "BButton.TButton", text = "Get Stock", command = lambda: getStock())
    getButton.grid(row = 1, column = 3)



    

    root.mainloop()




