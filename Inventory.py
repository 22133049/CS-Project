import tkinter as tk
from tkinter import messagebox, ttk, END,StringVar
import pickle

class Stock:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity


    def get_attributes(self):
        ob_att = [self.name,self.quantity]
        return ob_att


    def __str__(self):
        return f"{self.name}: {self.quantity}"


def openInv():
    root = tk.Tk()
    root.title("Inventory")
    root.configure(bg = "black")
    style = ttk.Style(root)
    style.theme_use("clam")
    style.configure("Text.TLabel",background = "black",foreground = "white", font = ("Arial",20,"bold"))
    style.configure("BButton.TButton",background = "white",foreground = "black", bordercolor = "#000000")

    ttk.Label(root,style = "Text.TLabel", text = "Inventory",anchor = "center").grid(row = 0, column = 0)

                    

    Stocklist = tk.Listbox(root,height = 10, width = 15)

    try:

        with open("inventory.pkl","rb") as inv:
            stock = list(pickle.load(inv))

    except:
        stock = []

    if not stock:
        Stocklist.insert(0,"No Stock, please click Add Stock")

    else:
        
        CurrentStock = {}
        for obj in stock:
            CurrentStock[obj.name] = obj.quantity# appending "name: quantity" to dictionary
    
        for name,qty in CurrentStock.items():
            
            Stocklist.insert(END,f"{name} ({qty})")#END puts each new entry at the bottom

    Stocklist.grid(row = 1, column = 0)



    
    
        

    
    




    def addStock():

        addmenu = tk.Toplevel(root)
        style = ttk.Style(addmenu)
        addmenu.title("Add Stock")
        addmenu.configure(background = "black")
        style.theme_use("clam")
        style.configure("AText.TLabel",background = "black",foreground = "white", font = ("Arial",14,"bold"))
        style.configure("AButton.TButton",background = "white",foreground = "black", bordercolor = "#000000")

        NameLabel = ttk.Label(addmenu,style = "AText.TLabel", text = "Name:")
        NameLabel.grid(row = 0, column = 0)
        Name = tk.Entry(addmenu)
        Name.grid(row = 0, column = 1)

        QuantityLabel = ttk.Label(addmenu, style = "AText.TLabel",text = "Quantity:")
        QuantityLabel.grid(row = 1, column = 0)
        Quantity = tk.Entry(addmenu)
        Quantity.grid(row = 1, column = 1)

        confirmButton = ttk.Button(addmenu,style = "AButton.TButton", text = "Confirm", command = lambda: confirm())
        confirmButton.grid(row = 2, column = 1, columnspan= 2)

        

        

        def confirm():

            name = Name.get()

            if not name:
                tk.messagebox.showerror("Error","Name not entered")
                return
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
    addButton.grid(row = 2, column = 0)


    def removeStock():

        addmenu = tk.Toplevel(root)
        style = ttk.Style(addmenu)
        addmenu.title("Remove Stock")
        addmenu.configure(background = "black")
        style.theme_use("clam")
        style.configure("AText.TLabel",background = "black",foreground = "white", font = ("Arial",14,"bold"))
        style.configure("AButton.TButton",background = "white",foreground = "black", bordercolor = "#000000")
        style.configure(
        "1Black.TMenubutton",   
        background="black",         
        foreground="white",
        bordercolor="#FFFFFF",
        borderwidth=2,
        padding=5)

        Stock = []

        with open("inventory.pkl","rb") as file:
            my_objects = list(pickle.load(file))

        StockLookup = {}

        for item in my_objects:
            display = f"{item.name}"
            Stock.append(display)
            StockLookup[display] = item

        if Stock:

            opt = StringVar(master = addmenu)
            opt.set(Stock[0])

            StockMenu = ttk.OptionMenu(addmenu, opt,Stock[0], *Stock,style = "1Black.TMenubutton")
            StockMenu.grid(row = 0, column = 1,padx = 20,pady = 20)

        else:
            tk.messagebox.showerror("Empty","Stock List is Empty")

        def confirm():
            nonlocal opt
            for obj in my_objects:
                if obj.name == opt.get():
                    StockO = obj
                    my_objects.remove(obj)

                    
                    break

            StockMenu.destroy()
            conf.destroy()

            ttk.Label(addmenu,text = "Quantity: ", style = "AText.TLabel").grid(row = 1,column = 0)
            QuantityE = ttk.Entry(addmenu)
            QuantityE.grid(row = 1, column = 1)


            def remove():
                nonlocal StockO
                if QuantityE.get().isdigit() == False:
                    tk.messagebox.showerror("Invalid","Invalid Number")
                    return
                    
                Amount = "Remove" + " " +  str(QuantityE.get()) + " " + opt.get() + "?"
                opt2 = tk.messagebox.askyesno("Are you Sure?",Amount)
                if opt2:
                    StockO.quantity = StockO.quantity - int(QuantityE.get())

                my_objects.append(StockO)
                with open("inventory.pkl","wb+") as file:
                    pickle.dump(my_objects,file)
                        
                    

            ttk.Button(addmenu,text = "Confirm", style = "BButton.TButton", command= lambda: remove()).grid(row = 2, column = 0,padx = 20,pady = 10)

        
            
            


        conf =ttk.Button(addmenu, text = "Confirm", style = "BButton.TButton",command= lambda: confirm())
        conf.grid(row = 1,column = 1,padx = 20,pady = 10)
        


    RemoveButton = ttk.Button(root,style = "BButton.TButton", text = "Remove Stock", command = lambda: removeStock())
    RemoveButton.grid(row = 2, column = 1)





    

    root.mainloop()







