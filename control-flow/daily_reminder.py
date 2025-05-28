# daily reminder

#define variable that prompts the user for input

task = input("Enter your task: ").capitalize()
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

while True:
    match priority:
        case "high":
            if time_bound == "yes":
                print(f"'{task}' is a {priority} priority task that requires immediate attention today!")
            else:
                print(f"'{task}' is a low priority task. Consider completing it when you have free time.")
            break
        case "medium":
            if time_bound == "yes":
                print(f"'{task}' is a {priority} priority task that should be completed soon.")
            else:
                print(f"'{task}' is a low priority task. Consider completing it when you have free time.")
            break
        case "low":
            if time_bound == "yes":
                print(f"'{task}' is a {priority} priority task that can be completed later.")
            else:
                print(f"'{task}' is a low priority task. Consider completing it when you have free time.")
            break
        case _:
            print("Invalid priority. Please enter high, medium, or low.")
            priority = input("Priority (high/medium/low): ").lower()
            time_bound = input("Is it time-bound? (yes/no): ").lower()
            continue