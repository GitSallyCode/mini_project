tasks = []


def add_task():
    while True:
        task_name = input("Please enter a task (q to quit): ")
        if task_name.lower() == 'q':
            break
        priority = input("Enter priority (High, Medium, Low): ")
        deadline = input("Enter deadline (YYYY-MM-DD): ")
        task = {"name": task_name, "priority": priority, "deadline": deadline}
        tasks.append(task)
        task_details = ", ".join(f"{key.capitalize()}: {value}" for key, value in task.items())
        print(f"[{task_details}] has been added to the list.")


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
        print("List of tasks are below: ")
        print("-----------------------------------------------------------------------")
        for i, task in enumerate(tasks, start=1):
            task_details = ", ".join(f"{key.capitalize()}: {value}" for key, value in task.items())
            print(f"{i}. {task_details}")
            print("-----------------------------------------------------------------------")

while True:
    print("[To-Do List Application]")
    print("1. Add Task")
    print("2. Remove Task")
    print("3. View Tasks")
    print("4. Exit")
    number = input("Please select a number: ")

    if number == '1':
        add_task()
    elif number == '2':
        remove_task()
    elif number == '3':
        view_task()
    elif number == '4':
        print("Goodbye")
        break
    else:
        print("Invalid input. Please enter a valid number.")

print("Thank you!:)")