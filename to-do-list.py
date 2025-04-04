def display_tasks(tasks):
    if not tasks:
        print("\nNo tasks available!")
    else:
        print("\nTo-Do List:")
        for i, task in enumerate(tasks, 1):
            status = "✓" if task[1] else "✗"
            print(f"{i}. [{status}] {task[0]}")

def main():
    tasks = []
    
    while True:
        print("\nOptions: 1. Add Task  2. View Tasks  3. Mark Done  4. Delete Task  5. Exit")
        choice = input("Enter choice: ").strip()

        if choice == "1":
            task = input("Enter task: ").strip()
            tasks.append([task, False])
            print("Task added!")

        elif choice == "2":
            display_tasks(tasks)

        elif choice == "3":
            display_tasks(tasks)
            index = int(input("Enter task number to mark done: ")) - 1
            if 0 <= index < len(tasks):
                tasks[index][1] = True
                print("Task marked as done!")

        elif choice == "4":
            display_tasks(tasks)
            index = int(input("Enter task number to delete: ")) - 1
            if 0 <= index < len(tasks):
                tasks.pop(index)
                print("Task deleted!")

        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice! Try again.")

if __name__ == "__main__":
    main()
