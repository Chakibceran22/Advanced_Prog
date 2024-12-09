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