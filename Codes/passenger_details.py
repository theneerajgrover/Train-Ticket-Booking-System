import random

pnr_list = []
booking_confirmed = {}

def details(tareek, month, seats, coach_list, username):
    passengers_list = {}
    pnrs_list = []
    
    print("\033[1m\n==== ENTER DETAILS CORRECTLY ====\033[0m")
    print("\033[1m🌈 AGE should be an integer\033[0m")
    print("\033[1m🌈 NAME must be a string\033[0m")
    
    for i in range(seats):
        while True:
            name = input(f"\nENTER NAME OF PASSENGER {i+1}: ").strip()
            age = input('ENTER AGE : ').strip()
            
            if name.replace(" ", "").isalpha() and age.isdigit() and 0 < int(age) <= 100:
                pnr = generate_pnr()
                seat_number = generate_seat_number() # Fixed: Removed argument
                pnrs_list.append(pnr)
                break
            print("\033[1m\n==== Invalid input! Please enter text for name and numbers for age. ====\033[0m")
        
        passengers_list[f"Passenger_{i+1}"] = {
            "Name": name.upper(), 
            "Age": int(age), 
            "PNR NUMBER": pnr, 
            "Seat Number": seat_number, 
            "Coach": coach_list[i]
        }
        
        with open("tickets_issued.txt", "a") as file:
            file.write(f"{name} ,{age} ,{pnr} ,{seat_number} ,{coach_list[i]} ,{tareek} ,{month} \n")
        
    with open("ticket_per_account.txt", "a") as file:
        file.write(f"{username} = {pnrs_list}\n")
        
    return passengers_list

def generate_pnr():
    num1 = random.randint(100, 999)
    num2 = random.randint(1000000, 9999999)
    return f"{num1} - {num2} "

def generate_seat_number(): 
    
    return random.randint(1, 50)
