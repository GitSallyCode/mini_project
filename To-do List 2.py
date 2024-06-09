
def menu_list():
    print("1. Add Task\n2. Remove Task\n3. View Tasks\n4. Suggest Tasks\n5. Exit")

def add_task(tasks):
    task = input("Enter the task: ")
    tasks.append(task)
    print(f"Task '{task}' added.")

def menu():
    tasks = []
    while True:
        menu_list()
        choice = input("Enter your choice: ")
        if choice == "1":
            add_task(tasks)
            break

menu()