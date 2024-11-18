import json

file_name = 'to_do_list.json'

# load task from file

def load_task():
    try:
        with open(file_name, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def save_tasks(to_do_list):
    with open(file_name, "w") as file:
        json.dump(to_do_list, file)

def display_tasks(to_do_list):
    print("\nTo-Do List:")
    for idx, task in enumerate(to_do_list, start=1):
        status = "✓" if task["completed"] else "✗"
        print(f"{idx}. {task['task']} [{status}]")
    print()

def add_task(to_do_list):
    task = input("Enter Task: ")
    to_do_list.append({"task": task, "completed": False})


def complete_task(to_do_list):
    task_num = int(input("Enter the the task number to mark as complete: "))
    if 1<= task_num <= len(to_do_list):
        to_do_list[task_num - 1]["completed"] = True
    else:
        print(f"Invalid task Number! {task_num}")


def delete_task(to_do_list):
    task_num = int(input("Enter the task number to Delete: "))
    if 1 <= task_num <= len(to_do_list):
        to_do_list.pop(task_num - 1)
    else:
        print(f"Invalid Task Number! {task_num}")

def main():
    to_do_list = load_task()
    while True:
        print("\n1. View Tasks\n2. Add Task\n3. Mark Task as Completed\n4. Delete Task\n5. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            display_tasks(to_do_list)
        elif choice == "2":
            add_task(to_do_list)
        elif choice == "3":
            complete_task(to_do_list)
            display_tasks(to_do_list)
        elif choice == "4":
            delete_task(to_do_list)
            display_tasks(to_do_list)
        elif choice == "5":
            save_tasks(to_do_list)
            display_tasks(to_do_list)
            print("Tasks saved. Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()










