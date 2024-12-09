while(True):
    try:
        input_year = int(input("Please enter a year: "))
        if( input_year % 4 == 0 and input_year % 100 != 0 or input_year % 400 == 0):
            print(f"{input_year} is a leap year.\n")
        else:
            print(f"{input_year} is not a leap year.\n")
        break;

    except Exception as e:#this blcok is for handleing errors if the string inputed is not a number 
        print("Please enter a valid year.\n")
        continue;

    
    