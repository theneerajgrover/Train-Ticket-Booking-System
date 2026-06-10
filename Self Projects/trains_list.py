import random
def trains_available() :
    trains_list = {"Dibrugarh - Kanyakumari Vivek Express" : random.randint(1, 30) , "Himsagar Express" : random.randint(1, 30) , "Aronai Superfast Express" : random.randint(1, 30) , "Navyug Express" : random.randint(1, 30) , "Avadh Assam Express" : random.randint(1, 30) }
    return trains_list

def print_list(trains):
    list = []
    trains_list = trains
    print("\033[1m\n==== THE AVAILABLE TRAINS ARE FOLLOWING !! ====\n\033[0m")
    
    for train in trains_list.items():
        list.append(train)
        print(train)
