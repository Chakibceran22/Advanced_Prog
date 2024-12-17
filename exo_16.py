list = [1,2,3,4,5,6,7,8,9,10]
while True:
    try:
        index = int(input("Enter the index or enter -1 to stop: "))
        if(index == -1):
            break
        if(index < -1):
            print("Enter a valid positive index or -1 to stop")
            continue
        value = int(input("Enter the value for that index: "))
        if 0 <= index < len(list):
            list.insert(index, value)
            print("updated list: ", list)
        
        else:
            user_input = int(input("Index out of range do you still want to add it at the end of the list? enter 1 for yes and 0 for no: "))
            if user_input == 1:
                list.append(value)
                print("updated list: ", list)
            else:
                continue
            
    
    except ValueError:
        print("Enter a valid number")

print("final list: ", list)