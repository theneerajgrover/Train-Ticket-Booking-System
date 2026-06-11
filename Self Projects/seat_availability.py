seats = 0
def seat_availability(my_train, trains) :
    global seats
    
    list1 = trains
    for i in list1 :
        if my_train == i:
            seats = int(list1[i])
            break
    return seats
