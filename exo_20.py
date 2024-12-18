user_list = []


def calculate_Median(user_list):
    list_length = len(user_list)
    if list_length % 2 == 0:
        median = (user_list[list_length//2] + user_list[list_length//2 - 1]) / 2
    else:
        median = user_list[list_length//2]
    return median   

def calculate_mean(user_list):
    sum_list = sum(user_list)
    
    mean = sum_list / len(user_list)
    return mean

while True:
    try:
        user_inputed_number = int(input("Enter a number or 0 to break:  "))
        if user_inputed_number == 0:
            break
        user_list.append(user_inputed_number)
        print("Updated List",user_list)
        user_list.sort()
        print("Sorted List ",user_list )
        print("Median Value:" , calculate_Median(user_list))
        print("Mean Value:" , calculate_mean(user_list))
        user_list.reverse()
        print("Reversed List ", user_list)
    except ValueError:
        print("Please enter a valid number")
        continue

while True:
    try:
        user_save_choice = int(input("Do you want to save the list? 1 for Yes, 2 for No: "))
        if user_save_choice == 1:
            with open("user_list.txt", "w") as file:
                for number in user_list:
                    file.write(str(number) + "\n")
            print("List saved successfully")        
            break
        elif user_save_choice == 2:
            break
        else:
            print("Please enter a valid choice between 1 or 2")
            continue
    except ValueError:
        print("Please enter a valid choice")
        continue