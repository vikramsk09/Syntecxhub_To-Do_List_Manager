tasks = []

def add_task():
    task = input("\nPlease enter a task to add: ")
    tasks.append(task)
    print(f"Your task - '{task}' has been added to the list.")

def view_task():
    if not tasks:
        print("There are no tasks currently.")
    else:
        print("Current Tasks are: ")
        for index, task in enumerate(tasks):
            print(f"Task #{index+1}. {task}")

def delete_task():
    if not tasks:
        print("There are no tasks to delete.")
        return

    view_task()
    try:
        task_to_delete = int(input("\nEnter the task number to delete: "))

        if 1 <= task_to_delete <= len(tasks):
            tasks.pop(task_to_delete - 1)   # Fixed Index
            print(f"\nTask #{task_to_delete} has been deleted.")
        else:
            print("\nInvalid task number.")

    except ValueError:
        print("Invalid input. Please enter a number.")


if __name__ == "__main__":
    # Create a loop to run the app
    print("Welcome to the To-Do List app :)")
    while True:
        print("\n")
        print("Please select one of the following options")
        print("-------------------------------------------")
        print("1. Add a new task")
        print("2. View all tasks")
        print("3. Delete a task")
        print("4. Quit")

        choice = input("Enter your choice: ")
        if choice == "1":
            add_task()

        elif choice == "2":
            view_task()

        elif choice == "3":
            delete_task()

        elif choice == "4":
            break

        else:
            print("Invalid input. Please try again.")

    print("Goodbye!")
