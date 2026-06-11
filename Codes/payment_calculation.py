def payment(train, seats) :
    price = 0
    train_list = {"Orient Express" : 5100, "Maharajas' Express" : 3500, "Glacier Express" : 3100, "Vande Bharat Express" : 1800, "Shatabdi Express" : 1500}
    
    for i in train_list :
        if train == i :
            price = train_list[i]
    
    amount = seats * price
    return amount
