import tkinter as tk
from tkinter import messagebox, ttk
import pickle

def viewAccounts():
    root = tk.Tk()

    root.title("Search Accounts")
    root.configure(bg = "black")
    style = ttk.Style(root)
    style.theme_use("clam")

    style.configure("Main.TLabel",background="black",foreground="white",font=("Arial",30,"bold"))
    style.configure("Entry.TLabel",background="black",foreground="white",font=("Arial",16,"bold"))
    style.configure("Button.TButton", background = "white",foreground = "black")
    

    frameRight = ttk.Label(root,style="Entry.TLabel")
    frameRight.grid(row = 0, column = 3)
    frameLeft = ttk.Label(root,style="Entry.TLabel")
    frameLeft.grid(row = 0, column = 0)


    Registration = ttk.Label(root,style = "Main.TLabel", text = "Search Accounts", anchor = "center")
    Registration.grid(row = 0, column = 1, columnspan = 2)

    eMailLabel = ttk.Label(root,style = "Entry.TLabel", text = "E-Mail:")
    eMailLabel.grid(row = 1, column = 1)
    eMail = tk.Entry(root)
    eMail.grid(row = 1, column = 2)

    fNameLabel = ttk.Label(root,style = "Entry.TLabel",text = "First Name:")
    fNameLabel.grid(row = 3, column = 1)
    fName = tk.Entry(root,)
    fName.grid(row = 3, column = 2)

    sNameLabel = ttk.Label(root,style = "Entry.TLabel",text = "Surname:")
    sNameLabel.grid(row = 4, column = 1)
    sName = tk.Entry(root)
    sName.grid(row = 4, column = 2)

    pNumLabel = ttk.Label(root,style = "Entry.TLabel",text = "Phone Number:")
    pNumLabel.grid(row = 5, column = 1)
    pNum = tk.Entry(root)
    pNum.grid(row = 5, column = 2)

    pCodeLabel = ttk.Label(root,style = "Entry.TLabel",text = "Post Code:")
    pCodeLabel.grid(row = 6, column = 1)
    pCode = tk.Entry(root)
    pCode.grid(row = 6, column = 2)

    Filler = ttk.Label(root,style = "Entry.TLabel")
    Filler.grid(row = 7, column = 1, columnspan = 2)


    def SearchUsers():

        MatchTotal = 0

        fNameVar = fName.get()

        if len(fNameVar):
            MatchTotal += 1

        sNameVar = sName.get()

        if len(sNameVar):
            MatchTotal += 1


        pNumVar = pNum.get()

        if len(pNumVar):
            MatchTotal += 1

        pCodeVar = pCode.get()

        if len(pCodeVar):
            MatchTotal += 1


        eMailVar = eMail.get()

        if len(eMailVar):
            MatchTotal += 1

        with open("customers.pkl","rb") as file:
            my_objs = list(pickle.load(file))

        with open("staff.pkl","rb") as stf:
            my_staff = list(pickle.load(stf))

        my_objs.extend(my_staff)


        matches = []

        if MatchTotal == 0:
            tk.messagebox.showerror("Error","Cannot Search with Nothing Entered")
            return

        for obj in my_objs:
            UserTotal = 0

            

            if len(fNameVar) and obj.fName.lower().startswith(fNameVar.lower()):
                UserTotal += 1
            
            if len(sNameVar) and obj.sName.lower().startswith(sNameVar.lower()):
                UserTotal += 1
            
            if len(eMailVar) and obj.eMail.lower().startswith(eMailVar.lower()):
                UserTotal += 1
            
            if len(pNumVar) and obj.pNum.lower().startswith(pNumVar.lower()):
                UserTotal += 1
            
            if len(pCodeVar) and obj.pCode.lower().startswith(pCodeVar.lower()):
                UserTotal += 1


            if UserTotal >= MatchTotal:
                matches.append(obj)

        
        readmatch = []

        for obj in matches:
            readmatch.append([obj.fName,obj.sName,obj.eMail,obj.pCode,obj.pNum])

  



        
        tk.messagebox.showinfo("Matches Found", readmatch)
    
                

        

        

    SearchButton = ttk.Button(root,style = "Button.TButton", text= "Search for Users",command = lambda: SearchUsers())
    SearchButton.grid(row = 8,column = 2)

    root.mainloop()

    


    
