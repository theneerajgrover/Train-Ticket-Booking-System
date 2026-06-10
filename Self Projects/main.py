import login, route_selection, date, trains_list, select_train, seat_availability, payment_calculation, passenger_details, booking_successful

print("\033[1m" + "==== WELCOME TO THE RAILWAY SEAT BOOKING APPLICATION !! ====" + "\033[0m")

login.create_acc()
route_selection.select_start_end()

tareek, month = date.select_date()
trains = trains_list.trains_available()

trains_list.print_list(trains)

select_train.train(trains)

my_choice = select_train.selected()

print("\033[1m"+ my_choice + "\033[0m")
seats = seat_availability.seat_availability(my_choice, trains)

user_seats = seat_availability.seat_confirm(seats)
passengers = passenger_details.details(user_seats)

# payment = payment_calculation.payment(my_choice, seats)

# print("AMOUNT TO BE PAID :", payment)
print("\033[1m\n==== DETAILS OF PASSENGERS ====\n\033[0m")

for pas, details in passengers.items() :
    print(pas, details)
booking_successful.booking()
