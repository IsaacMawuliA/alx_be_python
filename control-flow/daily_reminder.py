# Prompt the user for task details
task = input("What is your task for the day? ")
priority = input("What is the priority of this task (high, medium, low)? ")
time_bound = input("Is this task time-bound (yes or no)? ")

# Process the Task Based on Priority and Time Sensitivity
print("Reminder:")
match priority:
    case "high":
        print(f"Priority task: {task}")
    case "medium":
        print(f"Task: {task}")
    case "low":
        print(f"Low priority task: {task}")

if time_bound == "yes":
    print("This task is time-bound and requires immediate attention today!")
