import login

def process() :

    username = input("\nENTER YOUR USERNAME :")
    
    account_exists = False  # Track if account is found
    with open("users_cred.txt", "r") as file :
        for user in file :
            user,pswd = user.strip().split(",")
            if username == user :
                account_exists = True
                print("\033[1m" + "\n==== ACCOUNT ALREADY EXISTS ====" + "\033[0m")
                account_login = input("Do you want to login your account (y, n) ? : ").lower()
                if account_login == "y" :
                    login.process()
                    return  username# Stop execution here so it doesn't try to create a password below
                break
        
    if account_exists:  # Exit the function if the user decided not to log in
        return

    password = input("ENTER YOUR PASSWORD : ")
    
    with open("users_cred.txt", "a") as file :
        file.write(username + "," + password + "\n")
        
    print("\033[1m" + "\n==== ACCOUNT CREATED SUCCESSFULLY !! ====" + "\n\033[0m") 
    return username