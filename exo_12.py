while True:
    try:
        width = int(input("Please enter the width of hashes: "))
        height = int(input("Please enter the height of hashes: "))
        for i in range(height):
            print("#" * width)
    except ValueError as e:
        print("You must enter a number")
    