import random
coaches_list = ["1A", "2A", "3A", "S1", "S2", "S3", "S4", "S5", "S6", "S7", "S8"]
length = len(coaches_list)

# unique_coaches = random.sample(coaches, k=3)
coaches_dict = {}

def coaches():
    coaches_dict = {
        "Dibrugarh - Kanyakumari Vivek Express" : random.sample(coaches_list, k = random.randint(1,length)),
        "Himsagar Express"                      : random.sample(coaches_list, k = random.randint(1,length)),
        "Aronai Superfast Express"              : random.sample(coaches_list, k = random.randint(1,length)),
        "Navyug Express"                        : random.sample(coaches_list, k = random.randint(1,length)),
        "Avadh Assam Express"                   : random.sample(coaches_list, k = random.randint(1,length)),
    }
    return coaches_dict


def print_coaches(coaches ,chosen_train):
    # print("\033[1m\n==== THE AVAILABLE COACHES ARE FOLLOWING !! ====\n\033[0m")
    
    if chosen_train in coaches.keys() :
        # print(coaches[chosen_train])
        return coaches[chosen_train]