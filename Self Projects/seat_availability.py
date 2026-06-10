import trains_list, select_train
list1 = trains_list.trains
seats = 0
def seat_availability() :
    global seats
    my_train = select_train.selected()
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
            
