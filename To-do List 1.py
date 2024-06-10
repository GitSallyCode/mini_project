def menu_list():
     print("To-Do List Application\n 1. Add task\n 2. Remove task\n 3. View task\n 4. Exit")

def add_task(tasks):
    task = input("Enter a new task: ")
    tasks.append(task)
    print(f"Task {task} was added to the list")

def menu():
    tasks = []
    while True:
        menu_list()
        choice = input("Enter your choice: ")
        if choice == "1":
            add_task(tasks)
            break
menu()

