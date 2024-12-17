numbers = [1,2,3,4,5]
def print_menu() :
    print("Menu: \n 1.Append \n 2.Insert \n 3.Pop \n 4.Remove \n 5.Quit")

def append_element():
    while True:
        try:
            user_input_number = int(input("Enter a number to append: "))
            numbers.append(user_input_number)
            print("Updated Numbers List: ", numbers)
            break
            
        except ValueError:
            print("Invalid input. Please enter a number for the input.")
            continue

def insert_element():
    while True:
        try:
            user_input_number = int(input("Enter a number to insert: "))
            user_input_index = int(input("Enter the index to insert the number: "))
            if user_input_index > len(numbers):
                print("Invalid out of Bounds do you still wish to insert it at the end.")
                while True:
                    try:
                        user_choice_for_isertion = int(input("1. Yes 2. No  "))
                        if user_choice_for_isertion == 1:
                            numbers.append(user_input_number)
                            print("Updated Numbers List: ", numbers)
                            break
                        elif user_choice_for_isertion == 2:
                            break
                        else:
                            print("Invalid input. Please enter a number between 1 and 2.")
                            continue
                    except:
                        print("Invalid input. Please enter a number for the input.")
                        continue
                break
            numbers.insert(user_input_index,user_input_number)
            print("Updated Numbers List: ", numbers)
            break
            
        except ValueError:
            print("Invalid input. Please enter a number for the input.")
            continue

def pop_element():
    numbers.pop()
    print("Updated Numbers List: ", numbers)

def remove_element():
    while True:
        try:
            user_input_number = int(input("Enter a number to remove: "))
            if user_input_number not in numbers:
                print("Number not in list")
                continue
            numbers.remove(user_input_number)
            print("Updated Numbers List: ", numbers)
            break
            
        except ValueError:
            print("Invalid input. Please enter a number for the input.")
            continue

print("Numbers List:", numbers)
while True:
    try:
        print_menu()
        user_choice = int(input("choose an option:"))
        if user_choice == 5:
            print("thank you for using the app")
            break
        elif user_choice == 1:
            append_element()
        elif user_choice == 2:
            insert_element()
        elif user_choice == 3:
            pop_element()
        elif user_choice == 4:
            remove_element()
        else:
            print("Invalid input. Please enter a number between 1 and 5.")
            continue
    except ValueError:
        print("Invalid input. Please enter a number for the choicce.")
        continue

