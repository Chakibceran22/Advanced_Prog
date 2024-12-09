while True:
    input_string = input("enter a string to see the underline to stop use #: ")
    if input_string == '#':
        break
    print(f"\033[4m{input_string}\033[0m")
# i found in my reasearch that this \033[4m enable underline mode and \033[0m disable it