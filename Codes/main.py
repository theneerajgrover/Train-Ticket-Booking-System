import cancel_ticket, booking_history, create_account, login, after_login, exit, book_ticket

user_logged_in = False

print("\033[1m" + "==== WELCOME TO THE RAILWAY SEAT BOOKING APPLICATION !! ====\n" + "\033[0m")

while True :
    print("\033[1m" + "==== WHAT DO YOU WANT TO DO TODAY !! ====" + "\033[0m")
    print("1. Book Train Ticket")
    print("2. Cancel Train Ticket")
    print("3. Booking History")
    print("4. Open Dashboard")
    print("5. Create Account")
    print("6. Exit")
    
    user = input("\033[1mENTER YOUR CHOICE : (1,2,3,4,5,6) : \033[0m")
    if user == "1" :
        username = book_ticket.book_ticket(user_logged_in)
        after_login.after_login(username)
        
    elif user == "2":
        username = login.process()
        cancel_ticket.process()
        after_login.after_login(username)
        
    elif user == "3" :
        print("\033[1m" + "==== LOGIN IS REQUIRED TO SEE BOOKED TICKETS ====\033[0m")
        username = login.process()
        booking_history.process(username)
        after_login.after_login(username)
        
    elif user == "4":
        username = login.process()
        after_login.after_login(username)
        
    elif user == "5":
        username = create_account.process()
        after_login.after_login(username)
        
    elif user == "6":
        exit.exit_program()

    else :
        print("\033[1m==== INVALID INPUT !! ====\n\033[1m")
