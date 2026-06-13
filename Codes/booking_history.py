import book_ticket, after_login

def process(username) :
    logged_user = username
    
    with open("users_cred.txt", "r") as f_cred :
        for line in f_cred :
            user, pswd = line.strip().split(",")
            
            if logged_user == user :
                print("\033[1m==== ENTER THE PNR NUMBER ISSUED !! ====")
                print("NOTE : ALSO INCLUDE THE HYPHEN (-) AT CORRECT PLACE")
                
                while True :
                    pnr_number = input("ENTER HERE ➡️ : ")
                    pnr_found = False
                    
                    with open("ticket_per_account.txt", "r") as f_acct :
                        for line_acct in f_acct : 
                            if not line_acct.strip():
                                continue
                                
                            acct_user, pnr_list_str = line_acct.strip().split("=")
                            
                            if acct_user == logged_user:
                                
                                cleaned_pnr = pnr_list_str.replace("[", "").replace("]", "").replace("'", "")
                                pnr_list = [pnr.strip() for pnr in cleaned_pnr.split(",")]
                                
                                if pnr_number in pnr_list:
                                    pnr_found = True
                                    
                                    with open("tickets_issued.txt", "r") as f_ticket:
                                        for line_ticket in f_ticket :
                                            name, age, pnr_no, seat_no, coach = line_ticket.strip().split(",")
                                            
                                            if pnr_no == pnr_number:
                                                print("\nNAME :", name)
                                                print("AGE :", age)
                                                print("COACH :", coach)
                                                print("SEAT NUMBER :", seat_no, "\n")
                                                return 
                                    
                    if not pnr_found:
                        print("\033[1m==== NO PNR FOUND ====")
                        option = input("Do you want to re-enter the PNR ? (y / n) : ").lower()
                        if option == "y" :
                            continue
                        else :
                            break 
                        
    print("\033[1m===== NO TICKETS ISSUED BY YOUR USERNAME ==== ")
    
    def want() :
        choice = input("WANT TO BOOK TICKETS ? (y / n) : ").lower()
        if choice == "y" :
            book_ticket.book_ticket(True)
            return
            
        elif choice == 'n' :
            after_login.after_login(username)
            return
        else :
            print("\033[1m==== INVALID INPUT ====")
            want()        
    want()
    
