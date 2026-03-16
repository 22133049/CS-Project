import tkinter as tk
from tkinter import messagebox, ttk, StringVar
from Product import Product
import pickle




def leaveReview():

    root = tk.Toplevel()

    root.title("Place Order")
    root.configure(bg = "pink")

    #STYLING
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
    
    #GRAB PRODUCTS FROM FILE

    with open("products.pkl","rb") as file:
        my_products = list(pickle.load(file))

    for item in my_products:#takes product and display the name and price into dropdown menu
        safename = item.name.strip("{}")
        display = f"{item.name} (£{item.Price})"
        Products.append(display)
        ProductPrices[item.name] = item.Price
        Supplies.append(item.suppliesNeeded)

    ttk.Label(root,text = "Select Product",style = "Label.TLabel",font = ("Arial",20,'bold')).grid(row = 0, column = 0)

    opt = StringVar()
    opt.set(Products[0])



    
    ProductMenuLabel = ttk.Label(root,style = "Label.TLabel", text = "Select Product:")
    ProductMenuLabel.grid(row =  1, column = 0)

    ProductMenu = ttk.OptionMenu(root, opt,Products[0], *Products,style = "Custom.TMenubutton")
    ProductMenu.grid(row = 1, column = 1)

    def writeReview():

        revMenu = tk.Toplevel(root)


        ttk.Label(revMenu,text = "Write here: ",style = "Label.TLabel").grid(row = 1, column = 1)
        Review = ttk.Entry(revMenu)
        Review.grid(row = 1, column = 2,padx = 20,pady = 20)
        
        nonlocal opt
        for obj in my_products:
            if obj.name == opt.get():
                selected_product = obj
                break

        with open("current_user.pkl","rb") as file:
            my_user = pickle.load(file)

        def confirm():
            review = Review.get()
            if not review:
                tk.messagebox.showerror("Error","No Review Entered")

            cusID = my_user.id

            finalReview = [cusID,review]

            selected_product.Reviews.append(finalReview)

            with open("products.pkl","wb+") as file:
                pickle.dump(my_products,file)

            tk.messagebox.showinfo("Success", "Review added successfully!")
            revMenu.destroy()

        ttk.Button(revMenu,text = "Confirm",style = "Button.TButton",command = lambda: confirm()).grid(row = 2, column = 2)


        

        


    ttk.Button(root,text = "Confirm",style = "Button.TButton",command = lambda: writeReview()).grid(row = 2,column = 1)

def viewReviews():
    root = tk.Toplevel()

    root.title("Place Order")
    root.configure(bg = "black")

    #STYLING
    style = ttk.Style()
    style.theme_use("clam")

    style.configure("Button.TButton",background = "white",foreground = "black",bordercolor = "#FFFFFF",
                    borderwidth = 2)

    style.configure("Label.TLabel",background = "black", foreground = "White")

    style.configure(
    "Custom.TMenubutton",   
    background="black",         
    foreground="white",
    bordercolor="#FFFFFF",
    borderwidth=2,
    padding=5)
                

    Products = [] # for Dropdown
    ProductPrices = {}
    ProdSelect = []
    Supplies = []
    
    #GRAB PRODUCTS FROM FILE

    with open("products.pkl","rb") as file:
        my_products = list(pickle.load(file))

    for item in my_products:#takes product and display the name and price into dropdown menu
        safename = item.name.strip("{}")
        display = f"{item.name} (£{item.Price})"
        Products.append(display)
        ProductPrices[item.name] = item.Price
        Supplies.append(item.suppliesNeeded)

    ttk.Label(root,text = "Select Product",style = "Label.TLabel",font = ("Arial",20,'bold')).grid(row = 0, column = 0)

    opt = StringVar()
    opt.set(Products[0])



    
    ProductMenuLabel = ttk.Label(root,style = "Label.TLabel", text = "Select Products:")
    ProductMenuLabel.grid(row =  1, column = 0)

    ProductMenu = ttk.OptionMenu(root, opt,Products[0], *Products,style = "Custom.TMenubutton")
    ProductMenu.grid(row = 1, column = 1)

    def selectProd():
        nonlocal opt
        menu = tk.Toplevel()
        menu.title("Reviews")
        menu.configure(bg = "black")

        for obj in my_products:
            if obj.name == opt.get():
                selected_product = obj
                break


        for review in selected_product.Reviews:

                cust_id = review[0]
                review_text = review[1]
                frame = tk.Frame(menu,bg = "white",highlightbackground="#FFFFFF",highlightthickness=2,bd=0 , relief="solid", padx=5, pady=5)
                frame.pack(fill="x", pady=2)
                frames.append(frame)

                text = f"Customer {cust_id}: {review_text}"
                    
                tk.Label(frame, text=text, anchor="w",bg = "white", fg = "black").pack(side="left", fill="x", expand=True)

                




    ttk.Button(root,text = "Confirm",style = "Button.TButton", command = lambda: selectProd()).grid(row = 2, column = 1)

    
