# task_manager.py
class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, description):
        task = {"id": len(self.tasks) + 1, "description": description, "completed": False}
        self.tasks.append(task)
        print(f"Task {task['id']} added: {description}")

    def list_tasks(self):
        if not self.tasks:
            print("No tasks available.")
            return
        for task in self.tasks:
            status = "Completed" if task["completed"] else "Pending"
            print(f"Task {task['id']}: {task['description']} [{status}]")

    def complete_task(self, task_id):
        for task in self.tasks:
            if task["id"] == task_id:
                task["completed"] = True
                print(f"Task {task_id} marked as completed.")
                return
        print(f"Task {task_id} not found.")

def main():
    manager = TaskManager()
    while True:
        print("\nTask Manager: 1. Add Task 2. List Tasks 3. Complete Task 4. Exit")
        choice = input("Enter choice: ")
        if choice == "1":
            description = input("Enter task description: ")
            manager.add_task(description)
        elif choice == "2":
            manager.list_tasks()
        elif choice == "3":
            task_id = int(input("Enter task ID to complete: "))
            manager.complete_task(task_id)
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()