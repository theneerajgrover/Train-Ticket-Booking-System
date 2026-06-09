def create_acc():
    id = input("CREATE A USERNAME : ")
    password = input("CREATE A PASSWORD : ")
    while True :
        print("\nENTER YOUR CREDENTIALS NOW !!")
        check_id = input("ENTER YOUR USERNAME : ")
        check_pass = input("ENTER YOUR PASSWORD : ")
        if check_id != id or check_pass != password :
            print("ENTER VALID DETAILS !!")
        else :
            break