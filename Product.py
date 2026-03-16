import random
import tkinter as tk
from tkinter import messagebox, StringVar, OptionMenu, ttk
import pickle



class Product:
    def __init__(self, id, name, suppliesNeeded,Desc,Price,Reviews):
        self.name = name
        self.Desc = Desc
        self.Price = Price
        self.suppliesNeeded = suppliesNeeded
        self.Reviews = Reviews

        if not id:
            try:
                with open("products.pkl","rb") as file:
                    my_objects = list(pickle.load(file))
                id = "p" + str(int(my_objects[-1].id[1:]) + 1).zfill(2) #zfill pads with zeroes, will not error if it goes over 100
            except:
                id = "p" + str(1).zfill(2)

        self.id = id
            

        def get_attributes(self):
            ob_att = [self.id, self.name, self.suppliesNeeded, self.Desc, self.Price, self.Reviews]
            return ob_att

def addProd():
    root = tk.Toplevel()
    root.title("Add Product")
    root.configure(bg = "black")


    #STYLING

    style = ttk.Style(root)
    style.theme_use("clam")

    style.configure("Main.TLabel",background = "black", foreground = "white", font = ("Arial",30,"bold"))
    style.configure("Entry.TLabel",background = "black", foreground = "white", font = ("Arial",16,"bold"))

    style.configure(
    "Black.TMenubutton",   
    background="black",         
    foreground="white",
    bordercolor="#FFFFFF",
    borderwidth=2,
    padding=5)

    style.configure("Conf.TButton", background = "white",foreground = "black")

    Supply = []
    supply = []

    with open("inventory.pkl","rb") as file:
        my_objects = list(pickle.load(file))

    for item in my_objects:
        
        Supply.append(item.name)

    

    ttk.Label(root,style = "Main.TLabel", text = "Add New Product").grid(row = 0, column = 0)
    

    #WIDGETS


    Name = tk.Entry(root)
    Name.grid(row = 1, column = 1)
    NameLabel = ttk.Label(root,style = "Entry.TLabel",text = "Name:")
    NameLabel.grid(row = 1, column = 0)

    DescLabel = ttk.Label(root,style = "Entry.TLabel", text = "Description")
    DescLabel.grid(row = 2, column = 0)
    desc = tk.Entry(root)
    desc.grid(row = 2, column = 1)

    PriceLabel = ttk.Label(root, style = "Entry.TLabel",text = "Price: ")
    PriceLabel.grid(row = 3, column = 0)
    price = tk.Entry(root)
    price.grid(row = 3, column = 1)

    SuppliesNeededLabel = ttk.Label(root,style = "Entry.TLabel", text = "Supplies Needed:")
    SuppliesNeededLabel.grid(row = 4, column = 0)

    opt = StringVar()
    opt.set(Supply[0])

    SupplyMenu = ttk.OptionMenu(root, opt,Supply[0], *Supply,style = "Black.TMenubutton")
    SupplyMenu.grid(row = 4, column = 1)

    QuantityLabel = ttk.Label(root,style = "Entry.TLabel", text = "Quantity:")
    QuantityLabel.grid(row = 5, column = 0)
    Quantity = tk.Entry(root)
    Quantity.grid(row = 5, column = 1)

    def addSupply():

        #FOR ADDING NEW SUPPLY TO THE RECIPE

        try:
            SupQuant = int(Quantity.get())
            new_item = [opt.get(), SupQuant]
            supply.append(new_item)
        except ValueError:
            tk.messagebox.showerror("Error","Quantity is not a number")
            return


            
        

    ttk.Button(root,style = "Conf.TButton", text = "Add Supply", command= lambda: addSupply()).grid(row = 5, column = 2,padx = 5,pady = 5)

    def confirmProd():
        name = Name.get()

        if not name:
            tk.messagebox.showerror("Error","Name not entered")
            return
        
        suppliesNeeded = supply

        if not supply:
            tk.messagebox.showerror("Error","No Supplies Selected")
            return
        Desc = desc.get()

        if not Desc:
            tk.messagebox.showerror("Error","No Description Entered")
            return
            
        try:
            Price = float(price.get())
        except ValueError:
            tk.messagebox.showerror("Error","Price must be number")
            return

        if not Price:
            tk.messagebox.showerror("Error","Price must be entered")
            return
        
            

        temp = Product(None, name, suppliesNeeded, Desc, Price,None)

        try:
                  
            with open("products.pkl", "rb")as file:
                my_objects = list(pickle.load(file))
            my_objects.append(temp)

            with open("products.pkl", "wb+") as file:
                pickle.dump(my_objects, file)

            tk.messagebox.showinfo("Success","Successfully Added Product")

            root.destroy()



        except Exception as e:
    
            my_objects = []
            my_objects.append(temp)
            with open("products.pkl", "wb+") as file:
                pickle.dump(my_objects, file)
            tk.messagebox.showinfo("Success","Successfully Added Product")
            root.destroy()




        


    ttk.Button(root,style = "Conf.TButton",text= "Confirm",command = lambda: confirmProd()).grid(row = 6, column = 1, columnspan = 2 ,padx = 20 ,pady = 20)


def editProd():
    root = tk.Toplevel()

    Products = [] # for Dropdown

    root.title("Edit Product")
    root.configure(bg = "black")
    

    style = ttk.Style(root)
    style.theme_use("clam")

    style.configure("1Main.TLabel",background = "black", foreground = "white", font = ("Arial",30,"bold"))
    style.configure("1Entry.TLabel",background = "black", foreground = "white", font = ("Arial",16,"bold"))

    style.configure(
    "1Black.TMenubutton",   
    background="black",         
    foreground="white",
    bordercolor="#FFFFFF",
    borderwidth=2,
    padding=5)

    style.configure("1Conf.TButton", background = "white",foreground = "black")

    


    with open("products.pkl","rb") as file:
        my_products = list(pickle.load(file))

    ProductLookup = {}

    for item in my_products:
        display = f"{item.name}"
        Products.append(display)
        ProductLookup[display] = item

    opt = StringVar()
    opt.set(Products[0])

    ProductMenu = ttk.OptionMenu(root, opt,Products[0], *Products,style = "1Black.TMenubutton")
    ProductMenu.grid(row = 0, column = 1,padx = 20,pady = 20)

    def changeProd():
        ProductMenu.destroy()
        nonlocal opt #makes the opt variable able to be used outside of its normal place
        selected = opt.get()
        selected_product = ProductLookup[selected]
        Supply = []

        DefaultSupply = selected_product.suppliesNeeded

        for product in my_products:
            if product.name == opt.get():
                my_products.remove(product)
                break


        for supply in selected_product.suppliesNeeded:
            entry = supply[0]
            Supply.append(entry)
            

        #ENTRY WIDGETS
        Name = tk.Entry(root)
        Name.insert(0,selected_product.name)
        Name.grid(row = 1, column = 1)
        NameLabel = ttk.Label(root,style = "1Entry.TLabel",text = "Name:")
        NameLabel.grid(row = 1, column = 0)

        DescLabel = ttk.Label(root,style = "1Entry.TLabel", text = "Description")
        DescLabel.grid(row = 2, column = 0)
        desc = tk.Entry(root)
        desc.insert(0,selected_product.Desc)
        desc.grid(row = 2, column = 1)
        

        PriceLabel = ttk.Label(root,style = "1Entry.TLabel", text = "Price: ")
        PriceLabel.grid(row = 3, column = 0)
        price = tk.Entry(root)
        price.insert(0,selected_product.Price)
        price.grid(row = 3, column = 1)

        SuppliesNeededLabel = ttk.Label(root,style = "1Entry.TLabel", text = "Supplies Needed:")
        SuppliesNeededLabel.grid(row = 4, column = 0)

        opt = StringVar()
        opt.set(Supply[0])

        SupplyMenu = ttk.OptionMenu(root, opt,Supply[0], *Supply,style="1Black.TMenubutton")
        SupplyMenu.grid(row = 4, column = 1)

        QuantityLabel = ttk.Label(root,style = "1Entry.TLabel", text = "Quantity:")
        QuantityLabel.grid(row = 5, column = 0)
        Quantity = tk.Entry(root)
        Quantity.grid(row = 5, column = 1)

        supply = []

        

        def addSupply():
            try:
                QuanSup = int(Quantity.get())

                new_item = [opt.get(),QuanSup]
                supply.append(new_item)

            except ValueError:
                tk.messagebox.showerror("Error","Quantity is not a number")
                return
            

                          

        ttk.Button(root,style = "1Conf.TButton",  text = "Add Supply", command= lambda: addSupply()).grid(row = 5, column = 2)

        def confirmProd():
            name = Name.get()

            if not name:
                tk.messagebox.showerror("Error","Name not entered")
                return
            
            suppliesNeeded = supply

            if not supply:
                suppliesNeeded = DefaultSupply
                
                
            Desc = desc.get()
            Price = float(price.get())

            temp = Product(selected_product.id, name, suppliesNeeded, Desc, Price)

            try:

                my_products.append(temp)



                
                    

                with open("products.pkl", "wb+") as file:
                    pickle.dump(my_products, file)

                tk.messagebox.showinfo("Success","Successfully Edited Product")

                root.destroy()



            except Exception as e:
                my_objects = []
                my_objects.append(temp)
                with open("products.pkl", "wb+") as file:
                    pickle.dump(my_products, file)
                tk.messagebox.showinfo("Success","Successfully Added Product")
                root.destroy()

        ttk.Button(root,style = "1Conf.TButton", text = "Confirm Edits",command = lambda:confirmProd()).grid(row = 6, column = 1)


            

    ttk.Button(root,style = "1Conf.TButton", text = "Confirm", command = lambda: changeProd()).grid(row = 6, column = 1,padx = 20,pady = 10)


def deleteProd():
    root = tk.Toplevel()

    Products = [] # for Dropdown

    root.title("Delete Product")
    root.configure(bg = "black")
    root.rowconfigure(0,weight = 1)
    root.geometry("150x200")

    style = ttk.Style(root)
    style.theme_use("clam")

    style.configure("1Main.TLabel",background = "black", foreground = "white", font = ("Arial",30,"bold"))
    style.configure("1Entry.TLabel",background = "black", foreground = "white", font = ("Arial",16,"bold"))

    style.configure(
    "1Black.TMenubutton",   
    background="black",         
    foreground="white",
    bordercolor="#FFFFFF",
    borderwidth=2,
    padding=5)

    style.configure("1Conf.TButton", background = "white",foreground = "black")

    


    with open("products.pkl","rb") as file:
        my_products = list(pickle.load(file))


    for item in my_products:
        display = f"{item.name}"
        Products.append(display)

    opt = StringVar()
    opt.set(Products[0])

    ProductMenu = ttk.OptionMenu(root, opt,Products[0], *Products,style = "1Black.TMenubutton")
    ProductMenu.grid(row = 0, column = 1,pady = 20,padx = 20)

    def delProd():
        nonlocal opt
        Product = opt.get()

        for obj in my_products:
            if obj.name == Product:
                opt2 = tk.messagebox.askyesno("Are you Sure?","Are you sure this is the product you want to delete?")

                if opt2:
                    my_products.remove(obj)
                    tk.messagebox.showinfo("Success","Product Deleted")
                    break
                else:
                    tk.messagebox.showinfo("Aborted","Product Not Deleted")
                    

        with open("products.pkl","wb+") as file:
            pickle.dump(my_products,file)
                
                

    ConfButton = ttk.Button(root, text = "Confirm Product", style= "1Conf.TButton", command = lambda: delProd())
    ConfButton.grid(row = 1, column = 1,pady = 10)







    



        


 

        
    

        
