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
    
