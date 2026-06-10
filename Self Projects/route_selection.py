def select_start_end() :
    while True :
        start = input("\nENTER STARTING POINT : ").lower()
        end = input("ENTER ENDING POINT : ").lower()
        if not (start.isalpha()) or not (end.isalpha()):
            print("\033[1m==== ENTER VALID DETAILS !! ====\n\033[0m")
            
        else :
            break
