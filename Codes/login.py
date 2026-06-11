def create_acc():
    id = input("CREATE A USERNAME : ")
    password = input("CREATE A PASSWORD : ")
    while True :
        print("\033[1m\n==== ENTER YOUR CREDENTIALS NOW !! ====\033[0m")
        check_id = input("ENTER YOUR USERNAME : ")
        check_pass = input("ENTER YOUR PASSWORD : ")
        if check_id != id or check_pass != password :
            print("\033[1m==== ENTER VALID DETAILS !! ====\033[0m")
            
        else :
            break
