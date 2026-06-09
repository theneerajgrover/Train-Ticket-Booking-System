import random
def trains_available() :
    trains_list = {"Orient Express" : random.randint(1, 30) , "Maharajas' Express" : random.randint(1, 30) , "Glacier Express" : random.randint(1, 30) , "Vande Bharat Express" : random.randint(1, 30) , "Shatabdi Express" : random.randint(1, 30) }
    return trains_list

def print_list():
    list = []
    trains_list = trains_available()
    print("\nTHE AVAILABLE TRAINS ARE FOLLOWING !!\n")
    for train in trains_list.items():
        list.append(train)
        print(train)