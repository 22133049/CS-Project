import random
import tkinter as tk
from tkinter import messagebox, StringVar, OptionMenu
import pickle



class Product:
    def __init__(self, id, name, suppliesNeeded,Desc,Price):
        self.name = name
        self.Desc = Desc
        self.Price = Price
        self.suppliesNeeded = suppliesNeeded

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

    Supply = []
    supply = []

    with open("inventory.pkl","rb") as file:
        my_objects = list(pickle.load(file))

    for item in my_objects:
        
        Supply.append(item.name)

    

    tk.Label(root, text = "Add New Product",font =("Arial",30,'bold')).grid(row = 0, column = 0)
    


    Name = tk.Entry(root)
    Name.grid(row = 1, column = 1)
    NameLabel = tk.Label(root,text = "Name:")
    NameLabel.grid(row = 1, column = 0)

    DescLabel = tk.Label(root, text = "Description")
    DescLabel.grid(row = 2, column = 0)
    desc = tk.Entry(root)
    desc.grid(row = 2, column = 1)

    PriceLabel = tk.Label(root, text = "Price: ")
    PriceLabel.grid(row = 3, column = 0)
    price = tk.Entry(root)
    price.grid(row = 3, column = 1)

    SuppliesNeededLabel = tk.Label(root, text = "Supplies Needed:")
    SuppliesNeededLabel.grid(row = 4, column = 0)

    opt = StringVar()
    opt.set(Supply[0])

    SupplyMenu = OptionMenu(root, opt, *Supply)
    SupplyMenu.grid(row = 4, column = 1)

    QuantityLabel = tk.Label(root, text = "Quantity:")
    QuantityLabel.grid(row = 5, column = 0)
    Quantity = tk.Entry(root)
    Quantity.grid(row = 5, column = 1)

    def addSupply():

        new_item = [opt.get(), int(Quantity.get())]
        supply.append(new_item)
            
        

    tk.Button(root, text = "Add Supply", command= lambda: addSupply()).grid(row = 5, column = 2)

    def confirmProd():
        name = Name.get()
        suppliesNeeded = supply

        if not supply:
            tk.messagebox.showerror("Error","No Supplies Selected")
            return
        Desc = desc.get()
        Price = float(price.get())

        temp = Product(None, name, suppliesNeeded, Desc, Price)

        try:
                  
            with open("products.pkl", "rb")as file:
                my_objects = list(pickle.load(file))
            my_objects.append(temp)

            with open("products.pkl", "wb+") as file:
                pickle.dump(my_objects, file)

            tk.messagebox.showinfo("Success","Successfully Added Product")

            root.destroy()



        except Exception as e:
            print("Exception ocured:", e)
            my_objects = []
            my_objects.append(temp)
            with open("products.pkl", "wb+") as file:
                pickle.dump(my_objects, file)
            tk.messagebox.showinfo("Success","Successfully Added Product")
            root.destroy()




        


    tk.Button(root,text= "Confirm",command = lambda: confirmProd()).grid(row = 6, column = 1, columnspan = 2)


def editProd():
    root = tk.Toplevel()

    Products = [] # for Dropdown

    


    with open("products.pkl","rb") as file:
        my_products = list(pickle.load(file))

    ProductLookup = {}

    for item in my_products:
        display = f"{item.name} (£{item.Price})"
        Products.append(display)
        ProductLookup[display] = item

    opt = StringVar()
    opt.set(Products[0])

    ProductMenu = OptionMenu(root, opt, *Products)
    ProductMenu.grid(row = 1, column = 1)

    def changeProd():
        selected_product = ProductLookup[opt.get()]
        print(selected_product.name)
        print(selected_product.Price)
        print(selected_product.suppliesNeeded)

            
        Name = tk.Entry(root)
        Name.insert(0,selected_product.name)
        Name.grid(row = 1, column = 1)
        NameLabel = tk.Label(root,text = "Name:")
        NameLabel.grid(row = 1, column = 0)

        DescLabel = tk.Label(root, text = "Description")
        DescLabel.grid(row = 2, column = 0)
        desc = tk.Entry(root)
        desc.grid(row = 2, column = 1)

        PriceLabel = tk.Label(root, text = "Price: ")
        PriceLabel.grid(row = 3, column = 0)
        price = tk.Entry(root)
        price.insert(0,selected_product.Price)
        price.grid(row = 3, column = 1)

        SuppliesNeededLabel = tk.Label(root, text = "Supplies Needed:")
        SuppliesNeededLabel.grid(row = 4, column = 0)

        opt = StringVar()
        opt.set(Supply[0])

        SupplyMenu = OptionMenu(root, opt, *Supply)
        SupplyMenu.grid(row = 4, column = 1)

        QuantityLabel = tk.Label(root, text = "Quantity:")
        QuantityLabel.grid(row = 5, column = 0)
        Quantity = tk.Entry(root)
        Quantity.grid(row = 5, column = 1)

        def addSupply():
            
            supply.append(opt.get())
            supply.append(int(Quantity.get()))
                          

        tk.Button(root, text = "Add Supply", command= lambda: addSupply()).grid(row = 5, column = 2)

        def confirmProd():
            name = Name.get()
            suppliesNeeded = supply

            if not supply:
                tk.messagebox.showerror("Error","No Supplies Selected")
                return
            Desc = desc.get()
            Price = float(price.get())

            temp = Product(None, name, suppliesNeeded, Desc, Price, None)

            try:
                      
                with open("products.pkl", "rb")as file:
                    my_objects = list(pickle.load(file))
                my_objects.append(temp)

                with open("products.pkl", "wb+") as file:
                    pickle.dump(my_objects, file)

                tk.messagebox.showinfo("Success","Successfully Added Product")

                root.destroy()



            except Exception as e:
                print("Exception ocured:", e)
                my_objects = []
                my_objects.append(temp)
                with open("products.pkl", "wb+") as file:
                    pickle.dump(my_objects, file)
                tk.messagebox.showinfo("Success","Successfully Added Product")
                root.destroy()


            

    tk.Button(root,text = "Confirm", command = lambda: changeProd()).grid(row = 2, column = 1)

  

        


 

        
    

        
