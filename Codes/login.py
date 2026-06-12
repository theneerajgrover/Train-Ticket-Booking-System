import create_account

def process() :
    while True :
        username = input("\nENTER YOUR USERNAME : ")
        
        user_found = False  
        with open("users_cred.txt", "r") as file :
            for user in file :
                user,pswd = user.strip().split(",")
                if username == user :
                    user_found = True
                    break
        
        if not user_found:
            print("\033[1m" + "\n==== ACCOUNT DOESN'T EXIST ====" + "\033[0m")
            choice = input("DO YOU WANT TO CREATE A NEW ACCOUNT ? (y / n) : ").lower()
            if choice == 'y' :
                create_account.process()
                return 
            else:
                continue
                    
        password = input("ENTER YOUR PASSWORD : ")
        
        with open("users_cred.txt", "r") as file :
            for line in file :
                user, pswd = line.strip().split(",")
                
                if username == user:
                    if password == pswd :
                        print("\033[1m" + "\n==== LOGIN SUCCESSFUL ====" + "\033[0m")
                        return username
                    
                    else :
                        print("\033[1m\n==== INCORRECT PASSWORD !! ====\n\033[1m")
                        break
