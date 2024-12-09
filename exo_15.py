try:
        input_string = input("please enter a string to check if it contains vowels: ")
        
        if input_string.lower().__contains__('a'):
            print("a found")
        else:
            print("a not found")
        if input_string.lower().__contains__('e'):
            print("e found")
        else:
            print("e not found")
        if input_string.lower().__contains__('o'):
            print("o found")
        else:
            print("o not found")

except ValueError as e:
    print("You must enter a number")