# daily reminder

#define variable that prompts the user for input

task = input("Enter your task: ").capitalize()
task_priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

while True:
    match task_priority:
        case "high":
            if time_bound == "no":
                print(f"'{task}' is a low priority task. Consider completing it when you have free time.")
            else:
                print(f"'{task}' is a {task_priority} priority task that requires immediate attention today!")
            break
        case "medium":
            if time_bound == "no":
                print(f"'{task}' is a low priority task. Consider completing it when you have free time.")
            else:
                print(f"'{task}' is a {task_priority} priority task that should be completed soon.")
            break
        case "low":
            if time_bound == "no":
                print(f"'{task}' is a low priority task. Consider completing it when you have free time.")
            else:
                print(f"'{task}' is a {task_priority} priority task that can be completed later.")
            break
        case _:
            print("Invalid priority. Please enter high, medium, or low.")
            task_priority = input("Priority (high/medium/low): ").lower()
            time_bound = input("Is it time-bound? (yes/no): ").lower()
            continue