import random
def trains_available() :
    # trains_list = {"Orient Express" : random.randint(1, 30) , "Maharajas' Express" : random.randint(1, 30) , "Glacier Express" : random.randint(1, 30) , "Vande Bharat Express" : random.randint(1, 30) , "Shatabdi Express" : random.randint(1, 30) }
    trains_list = {'Orient Express': 7, "Maharajas' Express": 27, 'Glacier Express': 2, 'Vande Bharat Express': 2, 'Shatabdi Express': 6}
    return trains_list

trains = trains_available()

def print_list():
    list = []
    trains_list = trains
    print("\nTHE AVAILABLE TRAINS ARE FOLLOWING !!\n")
    for train in trains_list.items():
        list.append(train)
        print(train)
