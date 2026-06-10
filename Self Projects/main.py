import login, route_selection, date, trains_list, select_train, seat_availability, payment_calculation, passenger_details, booking_successful

print("WELCOME TO THE RAILWAY SEAT BOOKING APPLICATION !!")

login.create_acc()
route_selection.select_start_end()
date.select_date()
trains_list.trains_available()
trains_list.print_list()
select_train.train()
my_choice = select_train.selected()

print(my_choice)
seats = seat_availability.seat_availability()

seat_availability.seat_confirm(seats)
passengers = passenger_details.details(seats)

# payment = payment_calculation.payment(my_choice, seats)

# print("AMOUNT TO BE PAID :", payment)
print(passengers)
booking_successful.booking()
