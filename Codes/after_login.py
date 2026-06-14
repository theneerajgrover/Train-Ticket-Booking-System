import login, route_selection, date, trains_list, select_train, coaches_list, select_coach, seat_availability, seats_input, payment_calculation, passenger_details, booking_successful

first_thing_done = True


def book_ticket(user_logged_in):
    
    global first_thing_done, username
    username = login.logged_in
    
    while True :
        
        if first_thing_done :
            route_selection.select_start_end()

            tareek, month = date.select_date()
            trains = trains_list.trains_available()

            trains_list.print_list(trains)

            select_train.train(trains)

            my_choice = select_train.selected()

            print("\033[1m"+ my_choice + "\033[0m")
            seats = seat_availability.seat_availability(my_choice, trains)

            coaches_available = coaches_list.coaches()

            coach_for_selected_train = coaches_list.print_coaches(coaches_available, my_choice)
            coach_list_with_seats = select_coach.generate_coach_seats(coach_for_selected_train, seats)
            print()
            print(coach_list_with_seats)
            
            first_thing_done = False
            
        if not user_logged_in :
            
            print("\033[1m" + "==== LOGIN IS REQUIRED TO BOOK TICKETS ====\033[0m")
            username = login.process()
            user_logged_in = True
        
        if user_logged_in :
            if not first_thing_done :
                
                print("\033[1m" + "==== Hey",username, "====\033[0m")
                user_seats = seats_input.seat_confirm(seats)

                chosen_coach = select_coach.user_selects_coach(coach_list_with_seats, user_seats)
                # print(chosen_coach)

                passengers = passenger_details.details(tareek, month, user_seats, chosen_coach, username)

                # seat_number = passenger_details.generate_seat_number(chosen_coach, user_seats)
                # payment = payment_calculation.payment(my_choice, seats)

                # print("AMOUNT TO BE PAID :", payment)
                print("\033[1m\n==== DETAILS OF PASSENGERS ====\n\033[0m")

                for pas, details in passengers.items() :
                    print(pas, details)
                    
                booking_successful.booking()
                return username
