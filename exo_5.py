

while(True):
    first_runner_name = input("please enter the first runner's name: ")
    first_runner_time = float(input(f"please enter the time taken by {first_runner_name} to finish the race (in seconds): "))
    second_runner_name = input("please enter the second runner's name: ")
    second_runner_time = float(input(f"please enter the time taken by {second_runner_name} to finish the race (in seconds): "))
    if first_runner_time < 0 or second_runner_time < 0:
        print("Please enter positive times.\n")
    else:
        break;
if first_runner_time < second_runner_time:
    print(f"the fastetst runner {first_runner_name}")

elif first_runner_time > second_runner_time:
    print(f"the fastetst runner {second_runner_name}")
else:
    print("Both runners have the same time") 