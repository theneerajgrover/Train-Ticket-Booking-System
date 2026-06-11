import random

def generate_coach_seats(coaches, total_seats):
    selected_coaches = random.sample( coaches, min(total_seats, len(coaches)))

    coach_seats = {coach: 1 for coach in selected_coaches}

    remaining_seats = total_seats - len(selected_coaches)

    while remaining_seats > 0:
        coach = random.choice(selected_coaches)
        coach_seats[coach] += 1
        remaining_seats -= 1

    return coach_seats