unique_words = set()
list_of_duplicates = []

while True:
    inputed_word = input("Enter a word to stop input #: ") #this is the exo mixed with the bonus
    if inputed_word == "#":
        print(f"you entered {len(unique_words)} unique words and {len(list_of_duplicates)} not unqiue")
        break
    if inputed_word in unique_words:
        list_of_duplicates.append(inputed_word)
    else:
        unique_words.add(inputed_word.replace(" ","").lower())#the lower ethode make the program case insensitive
        print(sorted(unique_words))#printed as a lst because sets have no order

while True:
    try:
        user_choice = int(input("Do you wanna save it to a file? 1. Yes 2. No "))
        if user_choice == 1:
            with open("unique_words.txt", "w") as file:
                for word in unique_words:
                    file.write(word + "\n")
            print("File saved successfully")
            break
        elif user_choice == 2:
            break
        else:
            print("Invalid input. Please enter a number between 1 and 2.")
            continue
    except ValueError:
        print("Invalid input. Please enter a number for the input.")
        continue   