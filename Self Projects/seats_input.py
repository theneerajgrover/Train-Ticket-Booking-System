
def seat_confirm(seats) :
    while True :
        user_seats = int(input("ENTER NUMBER OF SEATS REQUIRED : "))
        if user_seats < 0 :
            print("\033[1m\n==== ENTER VALID INPUT !! ====\033[0m")
            
        elif user_seats <= seats :
            print("\033[1m\n==== SEATS AVAILABLE !! ====\033[0m")
            
            confirmation = input("DO YOU WANT TO CONFIRM THIS COUNT ? (y/n) : ").lower()
            if confirmation == 'y' :
                print("\033[1m" + f"==== {user_seats} seats confirmed successfully ====\033[0m")
                break
            else :
                print("\033[1mENTER AGAIN !!\n\033[0m")
        else :
            print("\033[1m\n==== THAT SEAT COUNT IS NOT AVAILABLE !! ====\033[0m")
    return user_seats
