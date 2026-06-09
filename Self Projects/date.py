def select_date():
    while True :
        date = int(input("ENTER DATE : "))
        month = int(input("ENTER MONTH IN DIGITS : "))
        if date < 0 or month < 0:
            print("ENTER VALID DETAILS !!\n")

        else :
            break