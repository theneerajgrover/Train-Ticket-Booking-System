import login, route_selection, date, trains_list, select_train, seat_availability, payment_calculation, passenger_details, booking_successful

print("WELCOME TO THE RAILWAY SEAT BOOKING APPLICATION !!")

login.create_acc()
route_selection.select_start_end()
date.select_date()
trains_list.trains_available()
trains_list.print_list()
select_train.train()
seat_availability.seat_availability()
seat_availability.seat_confirm()
passengers = passenger_details.details()
payment = payment_calculation.payment()
print("AMOUNT TO BE PAID :", payment)
booking_successful.booking()