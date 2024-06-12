tasks = []
import datetime


def get_priority_value(priority):
    # Assign numerical values to priorities to facilitate sorting
    if priority.capitalize() == 'High':
        return 1
    elif priority.capitalize() == 'Medium':
        return 2
    elif priority.capitalize() == 'Low':
        return 3
    return 4  # Default value for unknown priorities


def add_task():
    while True:
        task_name = input("Please enter a task (q to quit): ")
        if task_name.lower() == 'q':
            break
        while True:
            priority = input("Enter priority (High, Medium, Low): ")
            if priority.capitalize() in ["High", "Medium", "Low"]:
                break
            else:
                print("Invalid priority. Please enter High, Medium, or Low.")
        while True:
            deadline = input("Enter deadline (YYYY-MM-DD): ")
            try:
                deadline_date = datetime.datetime.strptime(deadline, "%Y-%m-%d").date()
                break
            except:
                print("Invalid date format. Please enter the date in YYYY-MM-DD format.")

        task = {"name": task_name, "priority": priority, "deadline": deadline}
        tasks.append(task)
        task_details = ", ".join(f"{key.capitalize()}: {value}" for key, value in task.items())
        print(f"'{task_details}' has been added to the list.")


def remove_task():
    view_task()
    try:
        removed_task_index = int(input("Enter the number to delete: ")) - 1
        if removed_task_index in range(len(tasks)):
            removed_task = tasks.pop(removed_task_index)
            print(f"{removed_task} has been removed.")
        else:
            print("Invalid task number.")
    except:
        print("Invalid input. Please enter a valid number.")


def view_task():
    if len(tasks) == 0:
        print("There are no tasks.")
    else:
        sorted_tasks = sorted(tasks, key=lambda x: (get_priority_value(x['priority']), x['deadline']))
        print("List of tasks are below: ")
        print("-----------------------------------------------------------------------")
        for i, task in enumerate(sorted_tasks, start=1):
            task_details = ", ".join(f"{key.capitalize()}: {value}" for key, value in task.items())
            print(f"{i}. {task_details}")
            print("-----------------------------------------------------------------------")


def suggest_task():
    print("Good afternoon! Here are some tasks you might want to work on: ")


while True:
    print("[To-Do List Application]")
    print("1. Add Task")
    print("2. Remove Task")
    print("3. View Tasks")
    print("4. Suggest Tasks")
    print("5. Exit")
    number = input("Please select a number: ")

    if number == '1':
        add_task()
    elif number == '2':
        remove_task()
    elif number == '3':
        view_task()
    elif number == '4':
        suggest_task()
    elif number == '5':
        print("Goodbye")
        break
    else:
        print("Invalid input. Please enter a valid number.")

print("Thank you! :)")











