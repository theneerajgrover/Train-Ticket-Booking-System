def select_start_end() :
    while True :
        start = input("\nENTER STARTING POINT : ")
        end = input("ENTER ENDING POINT : ")
        if not (start.isalpha()) or not (end.isalpha()):
            print("ENTER VALID DETAILS !!")
            
        else :
            break