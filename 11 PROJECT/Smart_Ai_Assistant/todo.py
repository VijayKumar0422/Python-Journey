import json


def load_tasks():

    try:

        with open("data/tasks.json", "r") as file:

            return json.load(file)

    except:

        return []


def save_tasks(tasks):

    with open("data/tasks.json", "w") as file:

        json.dump(tasks, file, indent=4)


def add_task():

    tasks = load_tasks()

    task = input("Enter task : ")

    tasks.append(task)

    save_tasks(tasks)

    print("Task added successfully.")


def show_tasks():

    tasks = load_tasks()

    if len(tasks) == 0:

        print("No tasks found.")

    else:

        print("\nTasks")

        for index, task in enumerate(tasks, start=1):

            print(index, ".", task)


def delete_task():

    tasks = load_tasks()

    show_tasks()

    if len(tasks) == 0:

        return

    number = int(input("Enter task number to delete : "))

    tasks.pop(number - 1)

    save_tasks(tasks)

    print("Task deleted successfully.")