def select_date():
    while True:
        date_input = input("ENTER DATE : ")
        month_input = input("ENTER MONTH IN DIGITS : ")
        
        if date_input.isdigit() and month_input.isdigit():
            day = int(date_input)
            month = int(month_input)
            
            if month >= 1 and month <= 12:
                
                max_days = 31
                if month == 4 or month == 6 or month == 9 or month == 11:
                    max_days = 30
                elif month == 2:
                    max_days = 29
                
                if day >= 1 and day <= max_days:
                    print("\033[1m==== DATE ACCEPTED ====\033[0m")
                    return day, month
                else:
                    print("\033[1m==== ENTER VALID DETAILS !! ====\n\033[0m")
            else:
                print("\033[1m==== ENTER VALID DETAILS !! ====\n\033[0m")
        else:
            print("\033[1m==== ENTER VALUES IN NUMERIC FORMAT !! ====\n\033[0m")
