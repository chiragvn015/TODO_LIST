# To-Do List Application in Python

# Initialize an empty list to store tasks
tasks = []

def display_menu():
    """Display the menu options to the user."""
    print("\n--- To-Do List Menu ---")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Delete Task")
    print("4. Exit")

def view_tasks():
    """Display all tasks in the to-do list."""
    if not tasks:
        print("\nNo tasks available. Your to-do list is empty!")
    else:
        print("\n--- Your Tasks ---")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")

def add_task():
    """Add a new task to the to-do list."""
    task = input("\nEnter the task: ").strip()
    if task:
        tasks.append(task)
        print(f"Task '{task}' added successfully!")
    else:
        print("Task cannot be empty. Please try again.")

def delete_task():
    """Delete a task from the to-do list."""
    view_tasks()
    if tasks:
        try:
            task_number = int(input("\nEnter the task number to delete: "))
            if 1 <= task_number <= len(tasks):
                removed_task = tasks.pop(task_number - 1)
                print(f"Task '{removed_task}' deleted successfully!")
            else:
                print("Invalid task number. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a valid task number.")

def main():
    """Main function to run the To-Do List application."""
    print("Welcome to the To-Do List Application!")
    while True:
        display_menu()
        choice = input("\nEnter your choice (1-4): ").strip()

        if choice == "1":
            view_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            delete_task()
        elif choice == "4":
            print("\nThank you for using the To-Do List Application. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option (1-4).")

# Run the application
if __name__ == "__main__":
    main()