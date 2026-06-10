import seat_availability

def details(seats):
    passengers_list = {}
    
    for i in range(seats):
        print("\nENTER DETAILS CORRECTLY")
        print("AGE should be an integer")
        print("NAME must be a string")
        
        while True:
            name = input(f"ENTER NAME OF PASSENGER {i+1}: ").strip()
            age = input(f'ENTER AGE OF PASSENGER {i+1}: ').strip()
            
            if name.replace(" ", "").isalpha() and age.isdigit():
                break
            print("Invalid input! Please enter text for name and numbers for age.")
        
        passengers_list[f"Passenger_{i+1}"] = {"Name": name.upper(), "Age": int(age)}
        
    return passengers_list
