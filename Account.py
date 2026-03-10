
import pickle 
from Nav import goto
import tkinter as tk
from tkinter import messagebox, ttk






class Account():
    def __init__(self,id,fName,sName,eMail,pWord,pNum,pCode,isAdmin):
        self.fName = fName
        self.sName = sName
        self.eMail = eMail
        self.pWord = pWord
        self.pNum = pNum
        self.pCode = pCode
        self.isAdmin = isAdmin

        if not id and self.isAdmin: #to generate ID's
            try:
                with open("staff.pkl","rb") as file:
                    my_objects = list(pickle.load(file))
                id = "s" + str(int(my_objects[-1].id[1:]) + 1).zfill(2) # looks at the last entry in the file and takes off the "s" bit and adds on its own "s" with the latest entry + 1

            except:
                id = "s" + str(1).zfill(2)
                


        if not id and not self.isAdmin:
            try:
                with open("customers.pkl","rb") as file:
                    my_objects = list(pickle.load(file))
                id = "c" + str(int(my_objects[-1].id[1:]) + 1).zfill(2) #zfill pads with zeroes, will not error if it goes over 100
            except:
                id = "c" + str(1).zfill(2)

        
        
        self.id = id

    def get_attributes(self):
        ob_att = [self.id, self.fName, self.sName, self.eMail, self.pWord, self.pNum, self.pCode]
        return ob_att


def SignUpScreen():

        SignedUp = False

        root = tk.Tk()
        root.title("Sign Up")
        root.configure(bg = "pink")

        

        style = ttk.Style()
        style.theme_use("clam")

        style.configure("Button.TButton",background = "white",foreground = "black",bordercolor = "#C2185B",
                        borderwidth = 2)

        style.configure("Label.TLabel",background = "pink", foreground = "White")


        frameRight = ttk.Label(root,style = "Label.TLabel")
        frameRight.grid(row = 0, column = 3)
        frameLeft = ttk.Label(root,style= "Label.TLabel")
        frameLeft.grid(row = 0, column = 0)


        Registration = ttk.Label(root, text = "Sign Up",style = "Label.TLabel", font =("Arial", 20,"bold"), anchor = "center")
        Registration.grid(row = 0, column = 1, columnspan = 2)


        #ENTRY WIDGETS
        eMailLabel = ttk.Label(root,style = "Label.TLabel", text = "E-Mail:",font = ("Arial",14,"bold"))
        eMailLabel.grid(row = 1, column = 1)
        eMail = tk.Entry(root)
        eMail.grid(row = 1, column = 2)

        pWordLabel = ttk.Label(root,style = "Label.TLabel", text = "Password:",font = ("Arial",14,"bold"))
        pWordLabel.grid(row = 2, column = 1)
        pWord = tk.Entry(root,show = "*")
        pWord.grid(row = 2, column = 2)

        fNameLabel = ttk.Label(root,style = "Label.TLabel",text = "First Name:",font = ("Arial",14,"bold"))
        fNameLabel.grid(row = 3, column = 1)
        fName = tk.Entry(root,)
        fName.grid(row = 3, column = 2)

        sNameLabel = ttk.Label(root,style = "Label.TLabel",text = "Last Name:",font = ("Arial",14,"bold"))
        sNameLabel.grid(row = 4, column = 1)
        sName = tk.Entry(root)
        sName.grid(row = 4, column = 2)

        pNumLabel = ttk.Label(root,style = "Label.TLabel",text = "Phone Number:",font = ("Arial",14,"bold"))
        pNumLabel.grid(row = 5, column = 1)
        pNum = tk.Entry(root)
        pNum.grid(row = 5, column = 2)

        pCodeLabel = ttk.Label(root,style = "Label.TLabel",text = "Post Code:",font = ("Arial",14,"bold"))
        pCodeLabel.grid(row = 6, column = 1)
        pCode = tk.Entry(root)
        pCode.grid(row = 6, column = 2)

        Filler = ttk.Label(root,style = "Label.TLabel")
        Filler.grid(row = 7, column = 1, columnspan = 2)

        def addCustomer(fNameVal,sNameVal,eMailVal,pWordVal,pNumVal,pCodeVal):
    
            
            #VALIDATION
            if len(fNameVal) > 10 or len(fNameVal) <= 0:
                tk.messagebox.showerror("Error","First Name too long or empty")
                return
            
            

            if len(sNameVal) > 15 or len(fNameVal) <= 0:
                tk.messagebox.showerror("Error","Surname too long or empty")
                return
            
            
            
            if len(eMailVal) == 0 or len(eMailVal) > 30:
                tk.messagebox.showerror("Error", "Nothing Entered or Too long")
                return

            if "@" not in eMailVal:
                tk.messagebox.showerror("Error", "Invalid Format")
                return
            
            

            if len(pWordVal) < 8 or len(pWordVal) > 20:
                tk.messagebox.showerror("Error","Password does not have at least 8 letters or is too long")
                return
            
            
            pNumVal = str(pNumVal)

            if len(pNumVal) != 11:
                tk.messagebox.showerror("Error","Invalid Phone Number")
                return
            
        

            if len(pCodeVal) != 6 and len(pCodeVal) != 7:
                tk.messagebox.showerror("Error", "Invalid Postcode")
                return

            temp = Account(None, fNameVal, sNameVal,eMailVal,pWordVal,pNumVal,pCodeVal, False)#creates the object
            try:
                          
                    with open("customers.pkl", "rb")as file:
                        my_objects = list(pickle.load(file))
                    my_objects.append(temp)

                    with open("customers.pkl", "wb+") as file:
                        pickle.dump(my_objects, file)

                    tk.messagebox.showinfo("Success","Successfully Signed Up")



            except (FileNotFoundError,EOFError):
                    my_objects = []
                    my_objects.append(temp)
                    with open("customers.pkl", "wb+") as file:
                        pickle.dump(my_objects, file)
                    tk.messagebox.showinfo("Success","Successfully Signed Up") #if file doesn't exist, makes one
                    
            root.destroy()
            from Project import MainScreen
            MainScreen()


        SaveButton = ttk.Button(root,style = "Button.TButton", text = "Confirm", command = lambda: addCustomer(fName.get(),sName.get(),eMail.get(),pWord.get(),pNum.get(),pCode.get()))
        SaveButton.grid(row = 8, column = 1, columnspan = 2)


def EditAccount():
    root = tk.Tk()

    root.title("Daydreams and Party Things")
    root.configure(bg = "pink")

    

    style = ttk.Style(root)
    style.theme_use("clam")

    style.configure("Button.TButton",background = "white",foreground = "black",bordercolor = "#C2185B",
                    borderwidth = 2)

    style.configure("Label.TLabel",background = "pink", foreground = "White")
    style.configure("SPink.TLabel",background = "pink",foreground = "white",font = ("Arial",14,"bold"))

    with open("current_user.pkl","rb") as file:
        user = pickle.load(file)


    fNameLabel = ttk.Label(root,style = "SPink.TLabel", text = "First Name: ")
    fNameLabel.grid(row = 0, column = 0)
    fNameEntry = tk.Entry(root)
    fNameEntry.insert(0,user.fName)
    fNameEntry.grid(row = 0, column = 1)

    sNameLabel = ttk.Label(root,style = "SPink.TLabel", text = "Last Name: ")
    sNameLabel.grid(row = 1, column = 0)
    sNameEntry = tk.Entry(root)
    sNameEntry.insert(0,user.sName)
    sNameEntry.grid(row = 1, column = 1)

    eMailLabel = ttk.Label(root,style = "SPink.TLabel", text = "E-Mail: ")
    eMailLabel.grid(row = 2, column = 0)
    eMailEntry = tk.Entry(root)
    eMailEntry.insert(0,user.eMail)
    eMailEntry.grid(row = 2, column = 1)

    pWordLabel = ttk.Label(root,style = "SPink.TLabel", text = "Password: ")
    pWordLabel.grid(row = 3, column = 0)
    pWordEntry = tk.Entry(root)
    pWordEntry.insert(0,user.pWord)
    pWordEntry.grid(row = 3, column = 1)

    pNumLabel = ttk.Label(root,style = "SPink.TLabel", text = "Phone Number: ")
    pNumLabel.grid(row = 4, column = 0)
    pNumEntry = tk.Entry(root)
    pNumEntry.insert(0,user.pNum)
    pNumEntry.grid(row = 4, column = 1)

    pCodeLabel = ttk.Label(root,style = "SPink.TLabel", text = "Postcode: ",)
    pCodeLabel.grid(row = 5, column = 0)
    pCodeEntry = tk.Entry(root)
    pCodeEntry.insert(0,user.pCode)
    pCodeEntry.grid(row = 5, column = 1)

    def change():

        fName = fNameEntry.get()
        sName = sNameEntry.get()
        eMail = eMailEntry.get()
        pWord = pWordEntry.get()
        pNum = str(pNumEntry.get())
        pCode = pCodeEntry.get()
        id = user.id
        isAdmin = user.isAdmin

        temp = Account(id,fName,sName,eMail,pWord,pNum,pCode,isAdmin)


        if user.isAdmin == True: #if an admin then save to admin file else save to customer
            with open("staff.pkl","rb") as file:
                my_objects = list(pickle.load(file))

        else:
            
            with open("customers.pkl","rb") as file:
                my_objects = list(pickle.load(file))

        for obj in my_objects:
            if obj.eMail == user.eMail:
                my_objects.remove(obj)
                break

        my_objects.append(temp)

        if temp.isAdmin == True:
            with open("staff.pkl","wb") as file:
                pickle.dump(my_objects,file)

        else:
            with open("customers.pkl","wb") as file:
                pickle.dump(my_objects,file)

        


    ttk.Button(root,style = "Button.TButton",text = "Change Details",command = lambda: change()).grid(row = 6, column = 1)
    

    
                    
def regStaff():
            


        SignedUp = False

        root = tk.Tk()
        root.title("Register Staff")
        root.configure(bg = "black")



        #STYLING

        style = ttk.Style(root)
        style.theme_use("clam")


        style.configure("White.TLabel",background = "black", foreground = "White",font = ("Arial",20,"bold"))
        style.configure("Small.TLabel",background = "black", foreground = "White",font = ("Arial",14,"bold"))
        style.configure("Button.TButton", background = "white",foreground = "black")
        


        frameRight = ttk.Label(root,style = "White.TLabel")
        frameRight.grid(row = 0, column = 3)
        frameLeft = ttk.Label(root,style = "White.TLabel")
        frameLeft.grid(row = 0, column = 0)


        Registration = ttk.Label(root, style = "White.TLabel",text = "Register Staff", anchor = "center")
        Registration.grid(row = 0, column = 1, columnspan = 2)

        #ENTRY WIDGETS
        eMailLabel = ttk.Label(root,  style = "Small.TLabel",text = "E-Mail:")
        eMailLabel.grid(row = 1, column = 1)
        eMail = ttk.Entry(root)
        eMail.grid(row = 1, column = 2)

        pWordLabel = ttk.Label(root, style = "Small.TLabel", text = "Password:")
        pWordLabel.grid(row = 2, column = 1)
        pWord = ttk.Entry(root,show = "*")
        pWord.grid(row = 2, column = 2)

        fNameLabel = ttk.Label(root, style = "Small.TLabel",text = "First Name:")
        fNameLabel.grid(row = 3, column = 1)
        fName = ttk.Entry(root,)
        fName.grid(row = 3, column = 2)

        sNameLabel = ttk.Label(root, style = "Small.TLabel",text = "Surname:")
        sNameLabel.grid(row = 4, column = 1)
        sName = ttk.Entry(root)
        sName.grid(row = 4, column = 2)

        pNumLabel = ttk.Label(root, style = "Small.TLabel",text = "Phone Number:")
        pNumLabel.grid(row = 5, column = 1)
        pNum = ttk.Entry(root)
        pNum.grid(row = 5, column = 2)

        pCodeLabel = ttk.Label(root, style = "Small.TLabel",text = "Post Code:")
        pCodeLabel.grid(row = 6, column = 1)
        pCode = ttk.Entry(root)
        pCode.grid(row = 6, column = 2)

        Filler = ttk.Label(root,style = "Small.TLabel")
        Filler.grid(row = 7, column = 1, columnspan = 2)

        def addStaff(fNameVal,sNameVal,eMailVal,pWordVal,pNumVal,pCodeVal):

            
            #VALIDATION
            if len(fNameVal) > 10 or len(fNameVal) <= 0:
                tk.messagebox.showerror("Error","First Name too long or empty")
                return
            
            

            if len(sNameVal) > 15 or len(fNameVal) <= 0:
                tk.messagebox.showerror("Error","Surname too long or empty")
                return
            
            
            
            if len(eMailVal) == 0 or len(eMailVal) > 30:
                tk.messagebox.showerror("Error", "Nothing Entered or Too long")
                return

            if "@" not in eMailVal:
                tk.messagebox.showerror("Error", "Invalid Format")
                return
            
            

            if len(pWordVal) < 8 or len(pWordVal) > 20:
                tk.messagebox.showerror("Error","Password does not have at least 8 letters or is too long")
                return
            
            
            pNumVal = str(pNumVal)

            if len(pNumVal) != 11:
                tk.messagebox.showerror("Error","Invalid Phone Number")
                return
            
        

            if len(pCodeVal) != 6 and len(pCodeVal) != 7:
                tk.messagebox.showerror("Error", "Invalid Postcode")
                return

            temp = Account(None, fNameVal, sNameVal,eMailVal,pWordVal,pNumVal,pCodeVal, True)
            try: #if file exists then append to it but if it doesnt then make a new file
                          
                    with open("staff.pkl", "rb")as file:
                        my_objects = list(pickle.load(file))
                    my_objects.append(temp)

                    with open("staff.pkl", "wb+") as file:
                        pickle.dump(my_objects, file)

                    tk.messagebox.showinfo("Success","Successfully Signed Up")



            except:
                    my_objects = []
                    my_objects.append(temp)
                    with open("staff.pkl", "wb+") as file:
                        pickle.dump(my_objects, file)
                    tk.messagebox.showinfo("Success","Successfully Signed Up")
                    
            root.destroy()


        SaveButton = ttk.Button(root,style = "Button.TButton", text = "Confirm", command = lambda: addStaff(fName.get(),sName.get(),eMail.get(),pWord.get(),pNum.get(),pCode.get()))
        SaveButton.grid(row = 8, column = 1, columnspan = 2)




def LogInScreen():

    root = tk.Tk()

    LogIn = tk.Label(root, text = "Log In", font =("Arial",20))
    LogIn.grid(row = 0, column = 0, columnspan = 2)

    eMailLabel = tk.Label(root, text = "E-Mail:")
    eMailLabel.grid(row = 1, column = 1)
    eMail = tk.Entry(root)
    eMail.grid(row = 1, column = 2)

    pWordLabel = tk.Label(root, text = "Password:")
    pWordLabel.grid(row = 2, column = 1)
    pWord = tk.Entry(root, show = "*")
    pWord.grid(row = 2, column = 2)


    Filler = tk.Label(root)
    Filler.grid(row = 7, column = 1, columnspan = 2)


    def LogIn():
        eMailentry = eMail.get()
        pWordentry = pWord.get()

        with open ("customers.pkl","rb") as file:
            my_objects = list(pickle.load(file))

        with open("staff.pkl","rb") as staff:
            my_staff = list(pickle.load(staff))



        found = False

        for customer in my_objects: #checks through customer file first
            if customer.eMail == eMailentry and customer.pWord == pWordentry and found == False:
                found = True
                tk.messagebox.showinfo("Success","Logged In")
                with open("current_user.pkl","wb") as file:
                    pickle.dump(customer,file)
                root.destroy()


                MenuScreen()

                return

                
        for staff in my_staff:#then checks through staff file
            if staff.eMail == eMailentry and staff.pWord == pWordentry and found == False:
                found = True
                tk.messagebox.showinfo("success","Logged in")
                with open("current_user.pkl","wb") as file:
                    pickle.dump(staff,file)
                root.destroy()
                AdminScreen()
                return
                
                

        if found == False:
            tk.messagebox.showerror("Incoorect,""Username or Password incorrect")


def deleteAccount(menu):


    with open("customers.pkl","rb") as file:
        my_objects = list(pickle.load(file))

    with open("current_user.pkl","rb") as file2:
        user = pickle.load(file2)

    for obj in my_objects:# looks for correct account to delete and also gives confirmation
        if obj.id == user.id:
            opt = tk.messagebox.askquestion("Are you Sure?","Are you sure you want to delete your account?", parent = menu)

            if opt == "yes":
                my_objects.remove(obj)
                

                with open("customers.pkl","wb+") as file:
                    pickle.dump(my_objects,file)

                    menu.destroy()
                    LogInScreen()
                break
            
            else:
                return


