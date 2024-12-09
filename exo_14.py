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
