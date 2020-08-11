usernameInput = input("Username :")
passwordInput = input("Password :")
tuprice = 50
roprice = 30
caprice = 20
if usernameInput == "admin" and passwordInput == "1234":
    print("Wellcome !!")
    print("---Please Select A Product---")
    print("1 : Tulip       : 50 THB")
    print("2 : Rose        : 30 THB")
    print("3 : Carnation   : 20 THB")
    select = int(input("SELECT : "))
    total = int(input("How Many : "))
    if select == 1 or select == 2 or select == 3:
        if select == 1:
            select = tuprice
        if select == 2 :
            select = roprice
        if select == 3:
            select = caprice
    print("Total Price :",select * total,"THB")
    print("Thank You ")