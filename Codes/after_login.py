import cancel_ticket, booking_history, exit, book_ticket

user_logged_in = False

def after_login(username) :
    
    global qwuser_logged_in
    
    while True :
        print("\033[1m==== HEY", username + " ====\n\033[0m")
        print("1. Book Train Ticket")
        print("2. Cancel Train Ticket")
        print("3. Booking History")
        print("4. Exit")
        
        user = input("\033[1mENTER YOUR CHOICE : (1,2,3,4,5,6) : \033[0m")
        if user == "1" :
            user_logged_in = True
            book_ticket.book_ticket(user_logged_in)
            
        elif user == "2":
            cancel_ticket.process()
            
        elif user == "3" :
            booking_history.process()
            
        elif user == "4":
            exit.exit_program()

        else :
            print("\033[1m==== INVALID INPUT !! ====\n\033[1m")
    
