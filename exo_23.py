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