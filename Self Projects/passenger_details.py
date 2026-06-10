import random
pnr_list = []

def details(seats):
    passengers_list = {}
    print("\033[1m\n==== ENTER DETAILS CORRECTLY ====\033[0m")
    print("\033[1m👉🏻 AGE should be an integer\033[0m")
    print("\033[1m👉🏻 NAME must be a string\033[0m")
    
    for i in range(seats):
        
        while True:
            name = input(f"\nENTER NAME OF PASSENGER {i+1}: ").strip()
            age = input(f'ENTER AGE : ').strip()
            
            if name.replace(" ", "").isalpha() and age.isdigit() and 0 < int(age) <= 100:
                pnr = generate_pnr()
                break
            print("\033[1m\n==== Invalid input! Please enter text for name and numbers for age. ====\033[0m")
        
        passengers_list[f"Passenger_{i+1}"] = {"Name": name.upper(), "Age": int(age), "PNR NUMBER" : pnr}
        
    return passengers_list


def generate_pnr():
    num1 = random.randint(100,999)
    num2 = random.randint(1000000,9999999)
    generated_pnr = str(num1) + "-" + str(num2)
    
    return generated_pnr
