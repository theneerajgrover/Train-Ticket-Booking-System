import trains_list
chosen_train = ""

def train():
    global chosen_train
    dict_of_trains = trains_list.trains
    list_of_trains = list(dict_of_trains.keys())
    while True :
        selection = int(input("\nSELECT THE TRAIN YOU WANT TO TRAVEL IN : (1, 2, 3, 4, 5) : "))
        for train in dict_of_trains :
            if selection == (list_of_trains.index(train) + 1) :
                chosen_train = train
                return train
        
        else :
            print("INVALID INPUT !!\n")
            
def selected() :
    return chosen_train
    
