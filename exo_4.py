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