tasks = []
task_id = 1


def add_task():
    global task_id
    name = input("Enter task name: ")
    task = (task_id, name, "Pending")
    tasks.append(task)
    print("Task added successfully.")
    task_id += 1


def view_tasks():
    if not tasks:
        print("No tasks available.")
        return

    print("\nTodo List")
    print("-" * 30)
    for t in tasks:
        print(f"ID: {t[0]} | Task: {t[1]} | Status: {t[2]}")


def mark_completed():
    task_num = int(input("Enter task ID to mark as completed: "))

    for i, t in enumerate(tasks):
        if t[0] == task_num:
            tasks[i] = (t[0], t[1], "Completed")
            print("Task marked as completed.")
            return

    print("Task not found.")


def delete_task():
    task_num = int(input("Enter task ID to delete: "))

    for t in tasks:
        if t[0] == task_num:
            tasks.remove(t)
            print("Task deleted.")
            return

    print("Task not found.")


def todo_manager():
    while True:
        print("\n--- Todo List Manager ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            mark_completed()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            print("Exiting Todo Manager.")
            break
        else:
            print("Invalid option. Try again.")


if __name__ == "__main__":
    todo_manager()