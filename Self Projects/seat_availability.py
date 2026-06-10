import trains_list, select_train
seats = 0
def seat_availability(my_train, trains) :
    global seats
    
    list1 = trains
    for i in list1 :
        if my_train == i:
            seats = int(list1[i])
            break
    return seats


def seat_confirm(seats) :
    while True :
        user_seats = int(input("ENTER NUMBER OF SEATS REQUIRED : "))
        if user_seats < 0 :
            print("ENTER VALID INPUT !!\n")
        elif user_seats <= seats :
            print("SEATS AVAILABLE !!")
            confirmation = input("DO YOU WANT TO CONFIRM THIS COUNT ? (y/n) : ").lower()
            if confirmation == 'y' :
                print(f"{user_seats} seats confirmed successfully")
                break
            else :
                print("ENTER AGAIN !!\n")
        else :
            print("THAT SEAT COUNT IS NOT AVAILABLE !!\n")
    return user_seats
