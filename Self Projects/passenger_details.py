import seat_availability
def details() :
    seats = seat_availability.seat_availability()
    passengers_list = {}
    for i in range(seats):
        name = input(f"ENTER NAME OF PASSENGER {i+1}: ")
        age = int(input(f'ENTER AGE OF PASSENGER {i + 1}: '))
        passengers_list[name] = age
    return passengers_list