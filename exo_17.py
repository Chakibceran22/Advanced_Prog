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