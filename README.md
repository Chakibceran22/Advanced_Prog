# Exercises Solutions

# Exercise 0: Calculating the Number of Rides Needed
Description: This program calculates the number of rides required to transport a group of people given the number of available seats per ride.
```python
while(True):
    nbr_people = int(input("How many people need a ride? "))
    if nbr_people > 0:
        while(True):
            nbr_seats = int(input("How many seats are available? "))
            if(nbr_seats > 0):
                break;
        nmb_rides = nbr_people // nbr_seats + (nbr_people % nbr_seats > 0)
        print(f"you will need {nmb_rides} rides to transport {nbr_people} people with {nbr_seats} seats available.\n")
        break;    
    else:
        print("Please enter a positive number of people.\n")
```

# Exercise 1: Ticket Purchase
Description: This program calculates the cost of tickets for a show. Special conditions apply for VIPs.
```python
username = input("Please enter your name: ")

if username == 'VIP':
    print("Enjoy your show for free!")
else:
    while(True):
        number_of_tickets = int(input("How many tickets do you want to buy? "))
        if number_of_tickets > 0:
            break;
        else:
            print("Please enter a positive number of tickets.\n")
    print(f"your total is gonna be {number_of_tickets * 15.5}.\n")
```

# Exercise 2: Temperature Feedback
Description: This program provides feedback based on the input temperature in Celsius.
```python
tempereture = int (input("Please enter the temperature in Celsius: "))
if tempereture < 20:
    print("It's cool !")
    if tempereture < 10:
        print("It's cold ")
        if tempereture < 0:
            print("It's freezing!! ")
print("stay safe outside")
```

# Exercise 3: Discount Calculation
Description: This program calculates the total cost of a purchase after applying discounts based on the number of items bought and the day of the week.
```python
while(True):
    total_amount = int(input("Please enter the total amount of your purchase: "))
    number_items = int(input("Please enter the number of items you bought: "))
    if total_amount > 0 and number_items > 0:
        break;
    else:
        print("Please enter  positive numbers.\n")

days_of_week = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday',]
weekend = ['saturday', 'sunday']
while(True):
    day = input("Please enter the day of the week: ")
    day = day.lower()
    if day in days_of_week or day in weekend:
        break;
    else:
        print("Please enter a valid day of the week.\n")
if day in days_of_week:
    if number_items > 5:
        total_amount -= total_amount * 0.15
    else:
        total_amount -= total_amount * 0.1
else:
    if number_items > 5:
        total_amount -= total_amount * 0.25
    else:
        total_amount -= total_amount * 0.2

print(f"Your total amount is {total_amount}.\n")
```

# Exercise 4: Determining the Older Age
Description: This program compares the ages of two individuals and determines which one is older or if they are the same age.
```python
while(True):
    first_age = int(input("Please enter the first person's age: "))
    second_age = int(input("Please enter the second person's age: "))
    if first_age > 0 and second_age > 0:
        break;
    else:
        print("enter positive ages.\n")
if first_age > second_age:
    print(f"The older age is {first_age}.")
elif first_age < second_age:
    print(f"The older age is {second_age}.")
else:
    print("Both ages are equal.")
```

# Exercise 5: Determining the Fastest Runner
Description: This program determines which of two runners completed a race in the shortest time, or if they both have the same time.
```python
while(True):
    first_runner_name = input("please enter the first runner's name: ")
    first_runner_time = float(input(f"please enter the time taken by {first_runner_name} to finish the race (in seconds): "))
    second_runner_name = input("please enter the second runner's name: ")
    second_runner_time = float(input(f"please enter the time taken by {second_runner_name} to finish the race (in seconds): "))
    if first_runner_time < 0 or second_runner_time < 0:
        print("Please enter positive times.\n")
    else:
        break;
if first_runner_time < second_runner_time:
    print(f"the fastetst runner {first_runner_name}")

elif first_runner_time > second_runner_time:
    print(f"the fastetst runner {second_runner_name}")
else:
    print("Both runners have the same time")
```

# Exercise 6: Splitting a Price into Whole and Fractional Parts
Description: This program takes a price as input and separates it into its whole and fractional parts.
```python
while(True):
    number = float(input("Please type in a price: "))
    if number > 0:
        break;
    else:
        print("Please enter a positive price.\n")

whole_part = int(number)
fractional_part = str(number).split(".")[1:] # Splitting the original number to extract the fractional part
fractional_part = int(fractional_part[0])

print(f"The whole part of the number is {whole_part} and the fractional part is {fractional_part}")
```

# Exercise 7: Leap Year Checker
Description: This program determines whether a given year is a leap year or not, with error handling for invalid inputs.
```python
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
        continue
```

# Exercise 8: FizzBuzz Implementation
Description: This program implements the classic FizzBuzz problem, printing "Fizz" for multiples of 3, "Buzz" for multiples of 5, and "FizzBuzz" for multiples of both.
```python
while True:
    try:
        input_number = int(input("please enter an integer: "))
        break
    except ValueError:
        print("Please enter a valid integer")
        continue

if input_number % 3 == 0 and input_number % 5 == 0:
    print("FizzBuzz")
elif input_number % 3 == 0:
    print("Fizz")
elif input_number % 5 == 0:
    print("Buzz")
```

# Exercise 9: City Population Calculator
Description: This program creates a dictionary of cities and their calculated populations based on the length of their names, sorting them by population.
```python
city_map = {}

while True:
        city = input("Please enter the name of the city: ")
        city = city.replace(" ","")
        number_of_citizens = len(city) * 1_000_000
        city_map[city] = number_of_citizens
        if(city == 'alger'):
            break;

#this creates a lambda function that gets me the values of the map and then it makes a list of tuples and sorts them by the values of the map
print(city_map.items())
city_map_sorted = dict(sorted(city_map.items(), key=lambda item: item[1] ,reverse=True))
print(city_map_sorted)
```


# Exercise 10: Palindrome Checker
Description: This program checks whether an input string is a palindrome by comparing characters from both ends, ignoring spaces.
```python
input_string = input("enter the string to verify: ")
input_string = input_string.replace(" ","")

left_pointer = 0
right_pointer = len(input_string) - 1
is_palindrome = True
while(left_pointer < right_pointer):
    if(input_string[left_pointer] != input_string[right_pointer]):
        is_palindrome = False
        break
    left_pointer += 1
    right_pointer -= 1
if(is_palindrome):
    print("The string is a palindrome")
else:
    print("The string is not a palindrome")    
```

# Exercise 11: Hash Line Generator
Description: This program generates a line of hash symbols (#) based on the user's input number.
```python
while True:
    try:
        number_of_hashes = int(input("Please enter the number of hashes: "))
        print("#" * number_of_hashes)
    except ValueError as e:
        print("You must enter a number")
```

# Exercise 12: Hash Rectangle Generator
Description: This program creates a rectangle pattern of hash symbols (#) based on user-specified width and height.
```python
while True:
    try:
        width = int(input("Please enter the width of hashes: "))
        height = int(input("Please enter the height of hashes: "))
        for i in range(height):
            print("#" * width)
    except ValueError as e:
        print("You must enter a number")
```

# Exercise 13: Text Underliner
Description: This program underlines input text using ANSI escape codes, continuing until the user enters '#'.
```python
while True:
    input_string = input("enter a string to see the underline to stop use #: ")
    if input_string == '#':
        break
    print(f"\033[4m{input_string}\033[0m")
# i found in my reasearch that this \033[4m enable underline mode and \033[0m disable it
```

# Exercise 14: Text Framer
Description: This program frames an input string with asterisks and spaces, limiting the input to 30 characters.
```python
while True:
    input_string = input("please enter the string to frame: ")
    if len(input_string) >30:
        print("The string is too long it has to be lower than 30 characters")
        continue
    else:
        break

while len(input_string) < 28:
    input_string = " " + input_string + " "
print("*" + input_string + "*")    
```

# Exercise 15: Vowel Checker
Description: This program checks for the presence of specific vowels (a, e, o) in an input string.
```python
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
```


# Exercise 16: Dynamic List Manipulation
Description: This program allows users to insert values at specific indices in a list, with handling for out-of-range indices.
```python
list = [1,2,3,4,5,6,7,8,9,10]
while True:
    try:
        index = int(input("Enter the index or enter -1 to stop: "))
        if(index == -1):
            break
        if(index < -1):
            print("Enter a valid positive index or -1 to stop")
            continue
        value = int(input("Enter the value for that index: "))
        if 0 <= index < len(list):
            list.insert(index, value)
            print("updated list: ", list)
        
        else:
            user_input = int(input("Index out of range do you still want to add it at the end of the list? enter 1 for yes and 0 for no: "))
            if user_input == 1:
                list.append(value)
                print("updated list: ", list)
            else:
                continue
            
    
    except ValueError:
        print("Enter a valid number")

print("final list: ", list)
```

# Exercise 17: List Operations and Combinations
Description: This program creates and manipulates two lists (numbers and shoe sizes), handles duplicates, and demonstrates list combination methods.
```python
numbers = []
shoe_sizes = []

for i in range(1,6):
    numbers.append(i)
    shoe_sizes.append(i+7) #this is to handle the second list without creating another loop

print("Numbers List:", numbers)
print("Shoe Sizes List: ",shoe_sizes)

#this is the bonus part
while True:
    try:
        user_input_number = int(input("Enter a number to stop enter -1: "))
        if user_input_number == -1:
            break
        if user_input_number in numbers:
            print("duplicates are not allowed")
            continue
        else:
            numbers.append(user_input_number)
            print("Updated Numbers List: ", numbers)
    except ValueError:
        print("Invalid input. Please enter a number.")

comines_lists = numbers.extend(shoe_sizes) # or we can use the + operator to combine the two lists
print("The Combined list of shoe_sized and numbers is:" ,comines_lists)
```

# Exercise 18: List Management Application
Description: A comprehensive list management application that provides various operations including append, insert, pop, remove, sort, reverse, and file operations.
```python
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

# Main program loop
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
                        numbers = [int(num) for line in lines for num in line.split()]
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
```


# Exercise 19: Unique Word Counter
Description: This program collects unique words from user input, handles duplicates, and offers the option to save the unique words to a file.
```python
unique_words = set()
list_of_duplicates = []

while True:
    inputed_word = input("Enter a word to stop input #: ") #this is the exo mixed with the bonus
    if inputed_word == "#":
        print(f"you entered {len(unique_words)} unique words and {len(list_of_duplicates)} not unqiue")
        break
    if inputed_word in unique_words:
        list_of_duplicates.append(inputed_word)
    else:
        unique_words.add(inputed_word.replace(" ","").lower())#the lower ethode make the program case insensitive
        print(sorted(unique_words))#printed as a lst because sets have no order

while True:
    try:
        user_choice = int(input("Do you wanna save it to a file? 1. Yes 2. No "))
        if user_choice == 1:
            with open("unique_words.txt", "w") as file:
                for word in unique_words:
                    file.write(word + "\n")
            print("File saved successfully")
            break
        elif user_choice == 2:
            break
        else:
            print("Invalid input. Please enter a number between 1 and 2.")
            continue
    except ValueError:
        print("Invalid input. Please enter a number for the input.")
        continue   
```

# Exercise 20: List Statistics Calculator
Description: This program maintains a list of numbers and calculates various statistics including median and mean, with an option to save results.
```python
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
```

# Exercise 21: Advanced List Statistics
Description: This program implements custom functions for calculating various list statistics including length, mean, range, and median, with type checking and error handling.
```python
def check_if_list_contains_only_int(list):
    for item in list:
        if not isinstance(item, int):
            return False
    return True

def length(list):
    if list == []:# the edge cases where the list is empty
        return 0
    length_of_list = 0
    for i in list:#iterating over the list to get the length and its gonna be always O(n)
        length_of_list += 1
    return length_of_list

def mean(list):
    if length(list) == 0:# the edge cases where the list is empty
        return 0
    
    if check_if_list_contains_only_int(list) == False:#to chekck if the list contains anything other than an int in it
        print("error there was something other than an int")
        return 0
    
    sum_of_list = 0
    for i in list:#Calculating the sum of the list it has same complexity as length
        sum_of_list += i
    return sum_of_list / length(list)

def range_of_list(list):
    if length(list) == 0:# the edge cases where the list is empty
        return 0
    if check_if_list_contains_only_int(list) == False:#to chekck if the list contains anything other than an int in it
        print("error there was something other than an int")
        return 0
    
    max = list[0]
    min = list[0]
    for i in list:#this calculates the max and min 
        if i > max:
            max = i
        if i < min:
            min = i
    return max - min

def median(list):
    if length(list) == 0:# the edge cases where the list is empty
        return 0
    if check_if_list_contains_only_int(list) == False:#to chekck if the list contains anything other than an int in it
        print("error there was something other than an int")
        return 0
    list.sort()
    if length(list) % 2 == 0:
        return (list[length(list) // 2] + list[length(list) // 2 - 1]) / 2
    else:
        return list[length(list) // 2]

list = [] #you can add a string here to test the error handling

while True:
    try:
        user_inputed_number = int(input("Enter a number or stop with 0: "))
        if user_inputed_number == 0:
            break
        list.append(user_inputed_number)
    except ValueError:
        print("Please enter a valid number")

list_statistics = {
    "length": length(list),
    "mean": mean(list),
    "range": range_of_list(list),
    "median": median(list)
}
print("the list is: ",list)
print("the statistics of the list are: ",list_statistics)
```

# Exercise 22: Character Printer
Description: This program takes a string input and prints each character followed by an asterisk.
```python
user_string = input("Enter a string: ")
for i in user_string:
    print(i)
    print('*')
```

# Exercise 23: Number Range Generator
Description: This program generates a range of numbers from negative to positive based on user input, excluding zero.
```python
while True :
    try:
        user_inputed_number = int(input("Enter a positive integer : "))
        if user_inputed_number <= 0:
            print("Please enter a positive integer")
            continue
        break
    except ValueError:
        print("Please enter a valid number")

for i in range(-user_inputed_number,user_inputed_number+1):
    if i == 0:
        continue
    print(i)
```


# Exercise 24: Anagram Checker
Description: This program implements a function to check if two strings are anagrams of each other by comparing their sorted characters.
```python
def anagram(str1,str2):
    if len(str1) != len(str2):
        return False
    
    string_list1 = list(str1)
    string_list2 = list(str2)
    string_list1.sort()
    string_list2.sort()
    if string_list1 == string_list2:
        return True
    else:
        return False

print(anagram("listen","silent"))
```


# How to Run
1. Clone the repository:
   ```bash
   git clone <repository-url>
   ```
2. Navigate to the project directory:
   ```bash
   cd <repository-directory>
   ```
3. Run the file:
   ```bash
   python <filename>.py
   ```

# How to Contribute
1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature-name
   ```
3. Make your changes and commit them:
   ```bash
   git commit -m "Description of changes"
   ```
4. Push your changes to your fork:
   ```bash
   git push origin feature-name
   ```
5. Open a pull request to the main repository.
