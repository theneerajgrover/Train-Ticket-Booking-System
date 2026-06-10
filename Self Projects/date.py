def select_date():
    while True :
        date = (input("ENTER DATE : "))
        month = (input("ENTER MONTH IN DIGITS : "))
        if date.isdigit() and month.isdigit() :
            if int(date) < 0 and int(month) < 0:
                print("ENTER VALID DETAILS !!\n")
            else :
                break
            
        else :
            print("ENTER IN NUMERIC FORMAT !!")
