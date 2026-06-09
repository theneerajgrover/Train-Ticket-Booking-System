import trains_list
def train():
    selected = ""
    dict_of_trains = trains_list.trains_available()
    list_of_trains = list(dict_of_trains.keys())
    while True :
        selection = int(input("\nSELECT THE TRAIN YOU WANT TO TRAVEL IN : (1, 2, 3, 4, 5) : "))
        for train in dict_of_trains :
            if selection == (list_of_trains.index(train) + 1) :
                print(train)
                selected = train
                return train
        
        else :
            print("INVALID INPUT !!\n")