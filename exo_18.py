
numbers = []
def print_menu() :
    print("Menu: \n 1.Append \n 2.Insert \n 3.Pop \n 4.Remove \n 5.Sort \n 6.Reverse \n 7.save it to a file  \n 8.Quit")

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
def sort_list():
    numbers.sort()
    print("Updated Numbers List: ", numbers)



def reverse_list():
    numbers.reverse()
    print("Updated Numbers List: ", numbers)

def save_list_to_file():
    with open("list.txt","w") as file:
        for number in numbers:
            file.write(str(number) + " ")
        print("List saved to file")


#this is for the bonus
while True:
    print("choose an option to load a list from a file or create a new list")
    try:
        user_list_choice = int(input("1. Load a list from a file 2. Create a new list: "))
        
        if user_list_choice == 2:
            while True:
                try:
                    user_input_number = int(input("Enter a number to the list if you wanna stop enter -1: "))
                    if user_input_number == -1:
                        break
                    numbers.append(user_input_number)
                    print("Updated Numbers List: ", numbers)
                    
                except ValueError:
                    print("Invalid input. Please enter a number for the input.")
                    continue
            break    
        elif user_list_choice == 1:
                
                try:
                    with open("list.txt","r") as file:
                        lines = file.read().splitlines()
                        numbers = [int(num) for line in lines for num in line.split()] #this takes the input from the list.txt file
                        break
                except Exception as e:
                    print(e)
                    continue
            
        else:
            print("enter a choice 1 or 2")

    except ValueError:
        print("Invalid input. Please enter a number for the choice.")
        continue


print("Numbers List:", numbers)

while True:
    try:
        print_menu()
        user_choice = int(input("choose an option:"))
        if user_choice == 8:
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
        elif user_choice == 5:
            sort_list()
        elif user_choice == 6:
            reverse_list()
        elif user_choice == 7:
            save_list_to_file()
        else:
            print("Invalid input. Please enter a number between 1 and 7.")
            continue
    except ValueError:
        print("Invalid input. Please enter a number for the choicce.")
        continue

