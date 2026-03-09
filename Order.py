import random
from Product import Product
from Classes.Stock import Stock
import pickle
import tkinter as tk
from tkinter import messagebox, StringVar, OptionMenu, ttk
from datetime import date,timedelta

class Order:

    def __init__(self,id, cusID, contents, date, delivDate, ordStat, cost, supply, canCreate):
        self.cusID = cusID
        self.contents = contents
        self.date = date
        self.delivDate = delivDate
        self.ordStat = ordStat
        self.cost = cost
        self.supply = supply
        self.canCreate = canCreate

        if not id:
            try:
                with open("orders.pkl","rb") as file:
                    my_objects = list(pickle.load(file))
                id = "o" + str(int(my_objects[-1].id[1:]) + 1).zfill(2) #zfill pads with zeroes, will not error if it goes over 100
            except:
                id = "o" + str(1).zfill(2)


        self.id = id

    def get_attributes(self):
        ob_att = [self.id, self.cusID, self.contents, self.date, self.delivDate, self.ordStat, self.cost, self.supply, self.canCreate]
        return ob_att


def placeOrder():

    root = tk.Toplevel()

    root.title("Place Order")
    root.configure(bg = "pink")
    style = ttk.Style()
    style.theme_use("clam")

    style.configure("Button.TButton",background = "white",foreground = "black",bordercolor = "#C2185B",
                    borderwidth = 2)

    style.configure("Label.TLabel",background = "pink", foreground = "White")

    style.configure(
    "Custom.TMenubutton",   
    background="pink",         
    foreground="white",
    bordercolor="#C2185B",
    borderwidth=2,
    padding=5)
                

    Products = [] # for Dropdown
    ProductPrices = {}
    ProdSelect = []
    Supplies = []
    


    with open("products.pkl","rb") as file:
        my_products = list(pickle.load(file))

    for item in my_products:
        print(item)
        safename = item.name.strip("{}")
        display = f"{item.name} (£{item.Price})"
        Products.append(display)
        ProductPrices[item.name] = item.Price
        Supplies.append(item.suppliesNeeded)

    ttk.Label(root,text = "Place Your Order",style = "Label.TLabel",font = ("Arial",20,'bold')).grid(row = 0, column = 0)

    opt = StringVar()
    opt.set(Products[0])

    ProductMenuLabel = ttk.Label(root,style = "Label.TLabel", text = "Select Products:")
    ProductMenuLabel.grid(row =  1, column = 0)

    ProductMenu = ttk.OptionMenu(root, opt,Products[0], *Products,style = "Custom.TMenubutton")
    ProductMenu.grid(row = 1, column = 1)

    QuantityLabel = ttk.Label(root,style = "Label.TLabel", text = "Quantity",font = ("Arial",14,"bold"))
    QuantityLabel.grid(row = 2, column= 0)
    quantity = tk.Entry(root)
    quantity.grid(row = 2, column = 1)

    costLabel = ttk.Label(root,style = "Label.TLabel", text = "Costs:",font = ("Arial",14,"bold"))
    costLabel.grid(row = 3, column = 0)

    cost = ttk.Label(root,style = "Label.TLabel",text = "£0",font = ("Arial",14,"bold"))
    cost.grid(row = 3, column = 1)
        

    def addProduct():
        prodOpt = opt.get()

        prodName = prodOpt.split(" (£")[0]
        prodPrice = ProductPrices[prodName]
        ProdSelect.append([prodName,prodPrice,quantity.get()])
        print(ProdSelect)
        TotalPrice = 0
        for i in ProdSelect:
            x = i[1] * int(i[2])
            TotalPrice = TotalPrice + x
        cost.config(text = "£" + str(TotalPrice))


    def confirmOrder():

        if not quantity.get():
            tk.messagebox.showerror("Failure, no quantity selected")
            return

        

        


        
        EndCost = cost.cget("text")
        ProdList = []
        for i in ProdSelect:
            ProdList.append([i[0],i[2]])

        with open ("current_user.pkl","rb") as file:
            my_objects = pickle.load(file)


    




        cusID = my_objects.id

        today = date.today()
        print(today)

        display_date = today.strftime("%d/%m/%Y")
        print(display_date)

        delivery_date = today + timedelta(weeks=2)

        display_date2 = delivery_date.strftime("%d/%m/%Y")
        print(display_date2)

        with open("inventory.pkl","rb") as file:
            my_stock = list(pickle.load(file))

        for obj in my_stock:
            print(obj.name,obj.quantity)

        total_supply_needed = {}

        for prod_name, quantity_ordered in ProdList:
            quantity_ordered = int(quantity_ordered)
            
            # Find the matching product object to get its recipe
            for product in my_products:
                if product.name == prod_name:
                    # product.suppliesNeeded is a list of [supply_name, amount]
                    for s_name, s_qty in product.suppliesNeeded:
                        needed = int(s_qty) * quantity_ordered
                        
                        # Add to our running dictionary of totals
                        if s_name in total_supply_needed:
                            total_supply_needed[s_name] += needed
                        else:
                            total_supply_needed[s_name] = needed
                    break # Found the product, move to next item in ProdList

        # 2. Check if we have enough in stock (canCreate)
        canCreate = True
        for supply_name, total_needed in total_supply_needed.items():
            found_in_stock = False
            for obj in my_stock:
                if obj.name == supply_name:
                    found_in_stock = True
                    if obj.quantity < total_needed:
                        canCreate = False
                    break
            
            # If a required supply isn't even in the inventory file
            if not found_in_stock:
                canCreate = False
                    
        with open("inventory.pkl","wb+") as file:
            pickle.dump(my_stock,file)
            
            
            

    
            

        temp = Order(None,cusID,ProdList,display_date,display_date2,"Making",EndCost,None,canCreate)

        try:
                    print(ProdList)
                    print(temp.get_attributes())
                          
                    with open("orders.pkl", "rb")as file:
                        my_objects = list(pickle.load(file))
                    my_objects.append(temp)

                    with open("orders.pkl", "wb+") as file:
                        pickle.dump(my_objects, file)

                    tk.messagebox.showinfo("Success","Successfully Placed Order")



        except:
                    my_objects = []
                    my_objects.append(temp)
                    with open("orders.pkl", "wb+") as file:
                        pickle.dump(my_objects, file)
                    tk.messagebox.showinfo("Success","Successfully Placed Order")
                    
        root.destroy()
        


            
        
            
        


        


    ttk.Button(root, text = "Add Product",style = "Button.TButton", command = lambda: addProduct()).grid(row = 2, column = 3, rowspan = 2)
    ttk.Button(root, text = "Confirm Order",style = "Button.TButton", command = lambda: confirmOrder()).grid(row = 3, column = 4, rowspan = 2)



    

    



    root.mainloop()

def viewOrders():
    root = tk.Tk()
    root.title("All Orders")
    root.configure(bg = "black")

    with open("orders.pkl","rb") as file:
        my_objects = list(pickle.load(file))

    print(my_objects)

    readord = []
    frames = []

    tk.Label(root,bg = "black",fg = "white", font = ("Arial",20,"bold"),text = "All Orders:").pack()

    for obj in my_objects:
        temp = vars(obj)
        readord.append(temp)

    def saveOrdersToFile():
        new_orders = []
        for o in readord:
            new_order = Order(
                o.get('id'),
                o.get('cusID'),
                o.get('contents'),
                o.get('date'),
                o.get('delivDate'),
                o.get('ordStat'),
                o.get('cost'),
                o.get('supply'),
                o.get('canCreate'),
            )
            new_orders.append(new_order)

        with open("orders.pkl", "wb") as file:
            pickle.dump(new_orders, file)


    def updateOrd(o, frames):
        window = tk.Tk()

        StatusLabel = tk.Label(window, text = "Status:")
        StatusLabel.grid(row = 0, column = 0)
        Status = tk.Entry(window)
        Status.insert(0,o['ordStat'])
        Status.grid(row = 0, column = 1)


        def saveStatus(frames):
            newStatus = Status.get()
            o['ordStat'] = newStatus
            saveOrdersToFile()
            showOrders(frames)




        tk.Button(window, text = "Confirm New Status", command = lambda: saveStatus(frames)).grid(row=1,column=0,columnspan=2)
        


        window.mainloop()


    def showOrders(frames):
        for frame in frames:
            frame.pack_forget()
        frames = []

        for order in readord:
            frame = tk.Frame(root,bg = "white",highlightbackground="#FFFFFF",highlightthickness=2,bd=0 , relief="solid", padx=5, pady=5)
            frame.pack(fill="x", pady=2)
            frames.append(frame)

            text = (
                f"Order #{order['id']} | "
                f"Customer: {order['cusID']} | "
                f"Products: {order['contents']} | "
                f"Status: {order['ordStat']} | "
                f"Cost: £{order['cost']} | "
                f"Delivery Date: {order['delivDate']}"
            )
            tk.Label(frame, text=text, anchor="w",bg = "white", fg = "black").pack(side="left", fill="x", expand=True)

            
            tk.Button(frame, text="Update Status", command=lambda o=order: updateOrd(o, frames)).pack(side="right")
        
    showOrders(frames)



    root.mainloop()


def cancelOrder():

    window = tk.Tk()
    style = ttk.Style()
    window.title("Cancel Orders")
    window.configure(bg = "pink")

    
    with open("orders.pkl","rb") as file:
        my_objects = list(pickle.load(file))

    with open("current_user.pkl","rb") as cus:
        customer = pickle.load(cus)


    cusOrds = []

    frames = []

    for obj in my_objects:
        if customer.id == obj.cusID and obj.ordStat == "Making":
            cusOrds.append(obj)


    def cancelOrd(o,frames):
        if o in my_objects:
            my_objects.remove(o)

        try:
            with open("orders.pkl","wb+") as file:
                pickle.dump(my_objects,file)

            window.destroy()

        except:
            tk.messagebox.showerror("Error","Order was not found")

    tk.Label(window,bg = "pink",fg = "white", font = ("Arial",20,"bold"),text = "Cancel Orders:").pack()

    for order in cusOrds:
        frame = tk.Frame(window,bg = "white",highlightbackground="#C2185B",highlightthickness=2,bd=0 , relief="solid")
        frame.pack(fill="x", pady=2)
        frames.append(frame)

        text = (
            f"Order #{order.id} | "
            f"Products: {order.contents} | "
            f"Status: {order.ordStat} | "
            f"Cost: £{order.cost} | "
            f"Delivery Date: {order.delivDate}"
        )
        tk.Label(frame, text=text, anchor="w",bg = "white", fg = "black").pack(side="left", fill="x", expand=True)

        
        ttk.Button(frame, text="Cancel Order", command=lambda o=order: cancelOrd(o, frames)).pack(side="right")

            

    
    
