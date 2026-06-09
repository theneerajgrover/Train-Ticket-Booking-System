import select_train, seat_availability
def payment() :
    price = 0
    train_list = {"Orient Express" : 5100, "Maharajas' Express" : 3500, "Glacier Express" : 3100, "Vande Bharat Express" : 1800, "Shatabdi Express" : 1500}
    select = select_train.train()
    for i in train_list :
        if select == i :
            price = train_list[i]
    
    no_of_seats = seat_availability.seat_confirm()
    amount = no_of_seats * price
    return amount