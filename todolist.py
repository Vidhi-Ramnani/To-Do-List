tasks = {}

def display_menu():
    print("\n--- To-Do List Application ---")
    print("1. Show all tasks")
    print("2. Add a new task")
    print("3. Update an existing task")
    print("4. Remove a task")
    print("5. Exit")

def show_tasks():
    if not tasks:
        print("Your to-do list is currently empty.")
    else:
        print("\nYour To-Do List:")
        for id, task in tasks.items():
            print(f"{id}: {task}")

def add_task():
    task_name = input("Enter a new task: ")
    task_id = len(tasks) + 1
    tasks[task_id] = task_name
    print(f"Task '{task_name}' added with ID {task_id}.")

def update_task():
    show_tasks()
    try:
        task_id = int(input("Enter the task ID to update: "))
        if task_id in tasks:
            new_task = input("Enter the updated task: ")
            tasks[task_id] = new_task
            print(f"Task {task_id} updated.")
        else:
            print("Task ID not found.")
    except ValueError:
        print("Please enter a valid number for the task ID.")

def delete_task():
    show_tasks()
    try:
        task_id = int(input("Enter the task ID to delete: "))
        if task_id in tasks:
            deleted_task = tasks.pop(task_id)
            print(f"Task '{deleted_task}' deleted.")
        else:
            print("Task ID not found.")
    except ValueError:
        print("Please enter a valid number for the task ID.")

while True:
    display_menu()
    choice = input("Choose an option (1-5): ")
    
    if choice == "1":
        show_tasks()
    elif choice == "2":
        add_task()
    elif choice == "3":
        update_task()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        print("Exiting the application. Goodbye!")
        break
    else:
        print("Invalid choice. Please select a valid option.")
