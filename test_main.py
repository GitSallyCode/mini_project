tasks = []

def add_task():
    while True:
        task = input("Please enter a task(q to quit): ")
        if task.lower() == 'q':
            break
        tasks.append(task)
        print(f"'{task}' has been added to the list.")
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
        print("--------------------------")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")
            print("--------------------------")

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