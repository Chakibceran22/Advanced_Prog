while True:
    try:
        number_of_hashes = int(input("Please enter the number of hashes: "))
        print("#" * number_of_hashes)
    except ValueError as e:
        print("You must enter a number")
    