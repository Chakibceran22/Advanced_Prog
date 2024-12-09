input_string = input("enter the string to verify: ")
input_string = input_string.replace(" ","")

left_pointer = 0
right_pointer = len(input_string) - 1
is_palindrome = True
while(left_pointer < right_pointer):
    if(input_string[left_pointer] != input_string[right_pointer]):
        is_palindrome = False
        break
    left_pointer += 1
    right_pointer -= 1
if(is_palindrome):
    print("The string is a palindrome")
else:
    print("The string is not a palindrome")    