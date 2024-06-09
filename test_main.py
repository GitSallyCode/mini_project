tasks = []

# def add_task():
#     task = input("Please enter a task: ")
#     tasks.append(task)
#     print(f"{task} has been added to the list.")
def view_task():
    if tasks:
        print("To-do list: ")
def remove_task():
    removed_task = int(input("Enter the number to delete: "))
    if removed_task in range(len(tasks)):
        tasks.pop(removed_task)
        print(f"{removed_task} has been removed.")































