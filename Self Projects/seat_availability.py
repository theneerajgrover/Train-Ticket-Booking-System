import trains_list, select_train
def seat_availability() :
    seats = 0
    train = select_train.train()
    list1 = trains_list.trains_available()
    for i in list1 :
        if train == i:
            seats = list1[i]
    return seats

def seat_confirm() :
    while True :
        user_seats = int(input("ENTER NUMBER OF SEATS REQUIRED : "))
        if user_seats < 0 :
            print("ENTER VALID INPUT !!\n")
        elif user_seats <= seat_availability() :
            print("SEATS AVAILABLE !!")
            confirmation = input("DO YOU WANT TO CONFIRM THIS COUNT ? (y/n) : ").lower()
            if confirmation == 'y' :
                return user_seats
            else :
                print("ENTER AGAIN !!\n")
        else :
            print("THAT SEAT COUNT IS NOT AVAILABLE !!\n")