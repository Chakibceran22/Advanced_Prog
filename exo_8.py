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
