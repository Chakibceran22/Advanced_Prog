while(True):
    number = float(input("Please type in a price: "))
    if number > 0:
        break;
    else:
        print("Please enter a positive price.\n")

whole_part = int(number)
fractional_part = str(number).split(".")[1:]#this is to split my original number to its fracional and whole parts im juts getting the fractioanl part
fractional_part = int(fractional_part[0])



print(f"The whole part of the number is {whole_part} and the fractional part is {fractional_part})")