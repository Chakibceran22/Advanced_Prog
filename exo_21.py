def check_if_list_contains_only_int(list):
    for item in list:
        if not isinstance(item, int):
            return False
    return True
def length(list):
    if list == []:# the edge cases where the list is empty
        return 0
    length_of_list = 0
    for i in list:#iterating over the list to get the length and its gonna be always O(n)
        length_of_list += 1
    return length_of_list

def mean(list):
    if length(list) == 0:# the edge cases where the list is empty
        return 0
    
    if check_if_list_contains_only_int(list) == False:#to chekck if the list contains anything other than an int in it
        print("error there was something other than an int")
        return 0
    
    sum_of_list = 0
    for i in list:#Calculating the sum of the list it has same complexity as length
        sum_of_list += i
    return sum_of_list / length(list)

def range_of_list(list):
    if length(list) == 0:# the edge cases where the list is empty
        return 0
    if check_if_list_contains_only_int(list) == False:#to chekck if the list contains anything other than an int in it
        print("error there was something other than an int")
        return 0
    
    max = list[0]
    min = list[0]
    for i in list:#this calculates the max and min 
        if i > max:
            max = i
        if i < min:
            min = i
    return max - min
def median(list):
    if length(list) == 0:# the edge cases where the list is empty
        return 0
    if check_if_list_contains_only_int(list) == False:#to chekck if the list contains anything other than an int in it
        print("error there was something other than an int")
        return 0
    list.sort()
    if length(list) % 2 == 0:
        return (list[length(list) // 2] + list[length(list) // 2 - 1]) / 2
    else:
        return list[length(list) // 2]
list = [] #you can add a string here to test the error handling

while True:
    try:
        user_inputed_number = int(input("Enter a number or stop with 0: "))
        if user_inputed_number == 0:
            break
        list.append(user_inputed_number)
    except ValueError:
        print("Please enter a valid number")

print("the list is: ",list)
print("the length of the list is: ",length(list))
print("the mean of the list is: ",mean(list))
print("the range of list of the list is: ",range_of_list(list))
print("the median of the list is: ",median(list))
    

