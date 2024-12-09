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
    if number_items > 5:                    #this of the added discount after buyying 5 itmes
        total_amount -= total_amount * 0.15
    else:
        total_amount -= total_amount * 0.1
else:
    if number_items > 5:                    #this of the added discount after buyying 5 itmes
        total_amount -= total_amount * 0.25
    else:
        total_amount -= total_amount * 0.2 

print(f"Your total amount is {total_amount}.\n")                           

        