def process(username):
    logged_user = username
    
    user_exists = False
    with open("users_cred.txt", "r") as f_cred:
        for line in f_cred:
            if not line.strip():
                continue
            user, pswd = line.strip().split(",")
            if logged_user == user:
                user_exists = True
                break
                
    if not user_exists:
        print("\033[1m===== INVALID USERNAME OR ACCOUNT NOT FOUND ==== ")
        return

    while True:
        print("\033[1m\n==== ENTER THE PNR NUMBER ISSUED !! ====")
        print("NOTE : ALSO INCLUDE THE HYPHEN (-) AT CORRECT PLACE\033[0m")
        pnr_number = input("ENTER HERE ➡️ : ").strip()
        pnr_found = False
        
        with open("ticket_per_account.txt", "r") as f_acct:
            for line_acct in f_acct: 
                if not line_acct.strip():
                    continue
                acct_user, pnr_list_str = line_acct.strip().split("=")
                
                if acct_user == logged_user:
                    cleaned_pnr = pnr_list_str.replace("[", "").replace("]", "").replace("'", "")
                    pnr_list = [pnr.strip() for pnr in cleaned_pnr.split(",")]
                    
                    if pnr_number in pnr_list:
                        pnr_found = True
                        break 
                        
        if pnr_found:
            
            ticket_details = None
            with open("tickets_issued.txt", "r") as f_ticket:
                for line_ticket in f_ticket:
                    if not line_ticket.strip():
                        continue
                    parts = line_ticket.strip().split(",")
                    
                    
                    if len(parts) == 7:
                        name, age, pnr_no, seat_no, coach, tareek, month = parts
                    elif len(parts) == 5:
                        name, age, pnr_no, seat_no, coach = parts
                        tareek, month = "Unknown", "Unknown"
                    else:
                        continue
                        
                    if pnr_no == pnr_number:
                        ticket_details = (name, age, seat_no, coach, tareek, month)
                        break

            if ticket_details:
                name, age, seat_no, coach, tareek, month = ticket_details
                print("\n\033[1m📋 TICKET FOUND DETAILS:\033[0m")
                print("NAME        :", name)
                print("AGE         :", age)
                print("COACH       :", coach)
                print("SEAT NUMBER :", seat_no)
                print(f"DATE        : {tareek} {month}\n")
                
                cancel_option = input("Do you really want to cancel ticket? (y / n) : ").lower()
                
                if cancel_option == "y":
                    
                    with open("tickets_issued.txt", "r") as f:
                        lines = f.readlines()
                    with open("tickets_issued.txt", "w") as f:
                        for line in lines:
                            
                            if pnr_number not in line:
                                f.write(line)
                                
                    
                    with open("ticket_per_account.txt", "r") as f:
                        acct_lines = f.readlines()
                    with open("ticket_per_account.txt", "w") as f:
                        for line in acct_lines:
                            if not line.strip():
                                continue
                            u, p_str = line.strip().split("=")
                            if u == logged_user:
                                
                                c_pnr = p_str.replace("[", "").replace("]", "").replace("'", "")
                                current_list = [p.strip() for p in c_pnr.split(",") if p.strip()]
                                if pnr_number in current_list:
                                    current_list.remove(pnr_number)
                                
                                if current_list:
                                    f.write(f"{u}={current_list}\n")
                            else:
                                f.write(line)
                                
                    print("\033[1;32m✅ Ticket cancelled successfully!\033[0m")
                    break
                else:
                    print("Cancellation aborted.")
                    break
            else:
                print("\033[1m==== ERROR: PNR in account registry but data missing in tickets file ====")
                break
        else:
            print("\033[1m==== NO PNR FOUND FOR THIS USER ====")
            option = input("Do you want to re-enter the PNR? (y / n) : ").lower()
            if option != "y":
                break
