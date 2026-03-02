
import pickle 
from Nav import goto
import tkinter as tk
from tkinter import messagebox






class Account():
    def __init__(self,id,fName,sName,eMail,pWord,pNum,pCode,isAdmin):
        self.fName = fName
        self.sName = sName
        self.eMail = eMail
        self.pWord = pWord
        self.pNum = pNum
        self.pCode = pCode
        self.isAdmin = isAdmin

        if not id and self.isAdmin:
            try:
                with open("staff.pkl","rb") as file:
                    my_objects = list(pickle.load(file))
                id = "s" + str(int(my_objects[-1].id[1:]) + 1).zfill(2)

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


        frameRight = tk.Label(root)
        frameRight.grid(row = 0, column = 3)
        frameLeft = tk.Label(root)
        frameLeft.grid(row = 0, column = 0)


        Registration = tk.Label(root, text = "Sign Up", font =("Arial", 20), anchor = "center")
        Registration.grid(row = 0, column = 1, columnspan = 2)

        eMailLabel = tk.Label(root, text = "E-Mail:")
        eMailLabel.grid(row = 1, column = 1)
        eMail = tk.Entry(root)
        eMail.grid(row = 1, column = 2)

        pWordLabel = tk.Label(root, text = "Password:")
        pWordLabel.grid(row = 2, column = 1)
        pWord = tk.Entry(root,show = "*")
        pWord.grid(row = 2, column = 2)

        fNameLabel = tk.Label(root,text = "First Name:")
        fNameLabel.grid(row = 3, column = 1)
        fName = tk.Entry(root,)
        fName.grid(row = 3, column = 2)

        sNameLabel = tk.Label(root,text = "Last Name:")
        sNameLabel.grid(row = 4, column = 1)
        sName = tk.Entry(root)
        sName.grid(row = 4, column = 2)

        pNumLabel = tk.Label(root,text = "Phone Number:")
        pNumLabel.grid(row = 5, column = 1)
        pNum = tk.Entry(root)
        pNum.grid(row = 5, column = 2)

        pCodeLabel = tk.Label(root,text = "Post Code:")
        pCodeLabel.grid(row = 6, column = 1)
        pCode = tk.Entry(root)
        pCode.grid(row = 6, column = 2)

        Filler = tk.Label(root)
        Filler.grid(row = 7, column = 1, columnspan = 2)

        def addCustomer(fNameVal,sNameVal,eMailVal,pWordVal,pNumVal,pCodeVal):
    
            

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

            temp = Account(None, fNameVal, sNameVal,eMailVal,pWordVal,pNumVal,pCodeVal, False)
            try:
                    print(temp.get_attributes())
                          
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
                    tk.messagebox.showinfo("Success","Successfully Signed Up")
                    
            root.destroy()
            from Project import MainScreen
            MainScreen()


        SaveButton = tk.Button(root, text = "Confirm", command = lambda: addCustomer(fName.get(),sName.get(),eMail.get(),pWord.get(),pNum.get(),pCode.get()))
        SaveButton.grid(row = 8, column = 1, columnspan = 2)


def EditAccount():
    root = tk.Tk()

    with open("current_user.pkl","rb") as file:
        user = pickle.load(file)


    fNameLabel = tk.Label(root, text = "First Name: ")
    fNameLabel.grid(row = 0, column = 0)
    fNameEntry = tk.Entry(root)
    fNameEntry.insert(0,user.fName)
    fNameEntry.grid(row = 0, column = 1)

    sNameLabel = tk.Label(root, text = "Last Name: ")
    sNameLabel.grid(row = 1, column = 0)
    sNameEntry = tk.Entry(root)
    sNameEntry.insert(0,user.sName)
    sNameEntry.grid(row = 1, column = 1)

    eMailLabel = tk.Label(root, text = "E-Mail: ")
    eMailLabel.grid(row = 2, column = 0)
    eMailEntry = tk.Entry(root)
    eMailEntry.insert(0,user.eMail)
    eMailEntry.grid(row = 2, column = 1)

    pWordLabel = tk.Label(root, text = "Password: ")
    pWordLabel.grid(row = 3, column = 0)
    pWordEntry = tk.Entry(root)
    pWordEntry.insert(0,user.pWord)
    pWordEntry.grid(row = 3, column = 1)

    pNumLabel = tk.Label(root, text = "Phone Number: ")
    pNumLabel.grid(row = 4, column = 0)
    pNumEntry = tk.Entry(root)
    pNumEntry.insert(0,user.pNum)
    pNumEntry.grid(row = 4, column = 1)

    pCodeLabel = tk.Label(root, text = "Postcode: ")
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


        if user.isAdmin == True:
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

        
        print(temp.get_attributes())
        print(my_objects)

    tk.Button(root,text = "Change Details",command = lambda: change()).grid(row = 6, column = 1)
    

    
                    
def regStaff():

        SignedUp = False

        root = tk.Tk()


        frameRight = tk.Label(root)
        frameRight.grid(row = 0, column = 3)
        frameLeft = tk.Label(root)
        frameLeft.grid(row = 0, column = 0)


        Registration = tk.Label(root, text = "Register Staff", font =("Arial", 20), anchor = "center")
        Registration.grid(row = 0, column = 1, columnspan = 2)

        eMailLabel = tk.Label(root, text = "E-Mail:")
        eMailLabel.grid(row = 1, column = 1)
        eMail = tk.Entry(root)
        eMail.grid(row = 1, column = 2)

        pWordLabel = tk.Label(root, text = "Password:")
        pWordLabel.grid(row = 2, column = 1)
        pWord = tk.Entry(root,show = "*")
        pWord.grid(row = 2, column = 2)

        fNameLabel = tk.Label(root,text = "First Name:")
        fNameLabel.grid(row = 3, column = 1)
        fName = tk.Entry(root,)
        fName.grid(row = 3, column = 2)

        sNameLabel = tk.Label(root,text = "Surname:")
        sNameLabel.grid(row = 4, column = 1)
        sName = tk.Entry(root)
        sName.grid(row = 4, column = 2)

        pNumLabel = tk.Label(root,text = "Phone Number:")
        pNumLabel.grid(row = 5, column = 1)
        pNum = tk.Entry(root)
        pNum.grid(row = 5, column = 2)

        pCodeLabel = tk.Label(root,text = "Post Code:")
        pCodeLabel.grid(row = 6, column = 1)
        pCode = tk.Entry(root)
        pCode.grid(row = 6, column = 2)

        Filler = tk.Label(root)
        Filler.grid(row = 7, column = 1, columnspan = 2)

        def addStaff(fNameVal,sNameVal,eMailVal,pWordVal,pNumVal,pCodeVal):

            

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
            try:
                    print(temp.get_attributes())
                          
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


        SaveButton = tk.Button(root, text = "Confirm", command = lambda: addStaff(fName.get(),sName.get(),eMail.get(),pWord.get(),pNum.get(),pCode.get()))
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

        for customer in my_objects:
            if customer.eMail == eMailentry and customer.pWord == pWordentry and found == False:
                found = True
                tk.messagebox.showinfo("Success","Logged In")
                with open("current_user.pkl","wb") as file:
                    pickle.dump(customer,file)
                root.destroy()


                MenuScreen()

                return

                
        for staff in my_staff:
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

    for obj in my_objects:
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

