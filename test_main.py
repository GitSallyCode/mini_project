tasks = []
foods = []
prices = []
total = 0


def add_task():
    task = input("Please enter a task: ")
    tasks.append(task)
    print(f"{''.join(tasks)} has been added to the list.")
def remove_task():
    removed_task = int(input("Enter the number to delete: "))
    if removed_task in range(len(tasks)):
        tasks.pop(removed_task)
        print(f"{removed_task} has been removed.")
def view_task():
    if len(tasks) == 0:
        print("There are no tasks.")
    else:
        print("List of tasks: ")
        for i, task in enumerate(tasks):
            print(f"{i+1}, {task}")
def delete_task():
    while len(tasks) > 0:


while True:
    print("To-Do List Application")
    print("1. Add Task")
    print("2. Remove Task")
    print("3. View Tasks")
    print("4. Exit")
    number = int(input("Please select a number: "))

    if number == 1:
        add_task()
        # print(f"{tasks} has been added to the list.")
        if "groceries" in tasks or "GROCERIES" in tasks:
            while True:
                food = input("Enter a food to buy (otherwise, q to quit): ")
                if food.lower() == "q":
                    break
                else:
                    price = float(input(f"Enter the price of a {food}: $"))
                    foods.append(food)
                    prices.append(price)
            for price in prices:
                total += price
        print("Please see your shopping cart below:")
        print(f"Item(s) is(are) {', '.join(foods)}, and total price is ${total}")

    elif number == 2:
        remove_task()
        pass
    elif number == 3:
        print("Tasks:")
    elif number == 4:
        print("Goodbye")
        break
    else:
        print("It's invalid.")
print("Thank you!:)")

































