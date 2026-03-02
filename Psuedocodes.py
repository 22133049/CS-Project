 function editAccount():
    using "customer" file:
        for ENTRY in "customer":
            APPEND ENTRY to customers
    
    using "staff" file:
        for ENTRY in "staff":
            APPEND ENTRY to staffs

ENTER fName,sName,eMail,pWord,pNum,pCode

users = ARRAY
APPEND customers to users
APPEND staffs to users

found = False
GET CurrentUser from file
for ENTRY in users:
   if ENTRY.eMail == CurrentUser.eMail AND ENTRY.pword == CurrentUser.pWord
        found = True
        REMOVE ENTRY FROM users
        break
   
if CurrentUser.isAdmin == True:
    open "staff" file:
    WRITE users to file