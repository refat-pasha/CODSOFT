import json

# File to store tasks
FILE_NAME = "tasks.json"


# Load tasks from file
def load_tasks():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


# Save tasks to file
def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file)


# Display tasks
def display_tasks(tasks):
    print("\nTo-Do List:")
    for idx, task in enumerate(tasks, start=1):
        status = "✓" if task["completed"] else "✗"
        print(f"{idx}. {task['task']} [{status}]")
    print()


# Add a new task
def add_task(tasks):
    task = input("Enter the new task: ")
    tasks.append({"task": task, "completed": False})


# Mark a task as completed
def complete_task(tasks):
    task_number = int(input("Enter the task number to mark as completed: "))
    if 1 <= task_number <= len(tasks):
        tasks[task_number - 1]["completed"] = True
    else:
        print("Invalid task number!")


# Delete a task
def delete_task(tasks):
    task_number = int(input("Enter the task number to delete: "))
    if 1 <= task_number <= len(tasks):
        tasks.pop(task_number - 1)
    else:
        print("Invalid task number!")


# Main application
def main():
    tasks = load_tasks()
    while True:
        print("\n1. View Tasks\n2. Add Task\n3. Mark Task as Completed\n4. Delete Task\n5. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            display_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            save_tasks(tasks)
            print("Tasks saved. Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()
