from task_manager import TaskManager
import datetime

# Task Manager CLI Application
def print_menu():
    print("\nTask Manager Menu:")
    print("[1] Add Task")
    print("[2] List Tasks")
    print("[3] Update Task")
    print("[4] Mark Task as Completed")
    print("[5] Delete Task")
    print("[0] Exit")

# Function to print tasks in a table format
def print_task_table(tasks):
    headers = ["ID", "Title", "Priority", "Status", "Due Date"]
    print("\n" + "=" * 80)
    print("| {:<5} | {:<20} | {:<8} | {:<10} | {:<12} |".format(*headers))
    print("|" + "-" * 77 + "|")
    for t in tasks:
        print("| {:<5} | {:<20} | {:<8} | {:<10} | {:<12} |".format(
            t['_id'], t['title'][:20], t['priority'], t['status'], t['due_date']))
    print("=" * 80)

# Function to input task details from the user
def input_task_details():
    title = input("Enter task title: ")
    description = input("Enter description: ")

    while True:
        due_date = input("Enter due date (YYYY-MM-DD): ")
        try:
            due_date_obj = datetime.datetime.strptime(due_date, "%Y-%m-%d")
            if due_date_obj.date() < datetime.date.today():
                print("Due date must be today or in the future.")
            else:
                break
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")

    valid_priorities = ["low", "medium", "high"]
    while True:
        priority = input("Enter priority (Low/Medium/High): ").strip().lower()
        if priority not in valid_priorities:
            print("Invalid priority. Choose from Low, Medium, or High.")
        else:
            priority = priority.capitalize()
            break

    return title, description, due_date, priority

# Main function to run the Task Manager CLI application
def main():
    task_manager = TaskManager()

    while True:
        print_menu()
        choice = input("Choose an option: ")

        if choice == '1':
            print("\n--- Add Task ---")
            title, description, due_date, priority = input_task_details()
            task_manager.add_task(title, description, due_date, priority)
            print("Task added successfully.")
        
        elif choice == '2':
            print("\n--- All Tasks ---")
            tasks = task_manager.list_tasks()
            if tasks:
                headers = ["ID", "Title", "Description", "Priority", "Status", "Due Date", "Created At"]
                print("\n" + "=" * 120)
                print("| {:<5} | {:<15} | {:<25} | {:<8} | {:<10} | {:<12} | {:<18} |".format(*headers))
                print("|" + "-" * 117 + "|")
                for t in tasks:
                    created_at_str = datetime.datetime.fromisoformat(t['created_at']).strftime("%b %d, %Y %I:%M %p")
                    print("| {:<5} | {:<15} | {:<25} | {:<8} | {:<10} | {:<12} | {:<18} |".format(
                        t['_id'], t['title'][:15], t['description'][:25], t['priority'], t['status'], t['due_date'], created_at_str))
                print("=" * 120)
            else:
                print("No tasks found.")

        elif choice == '3':
            print("\n--- Update Task ---")
            tasks = task_manager.list_tasks()
            if tasks:
                print_task_table(tasks)
            task_id = input("Enter task ID to update: ")
            field = input("Enter field to update (title/description/due_date/priority): ")
            new_value = input(f"Enter new value for {field}: ")
            task_manager.update_task(task_id, field, new_value)
            print("Task updated successfully.")

        elif choice == '4':
            print("\n--- Mark Task as Completed ---")
            tasks = task_manager.list_pending_tasks()

            if tasks:
                print_task_table(tasks)
                task_id = input("Enter Task ID: ")
                task_manager.mark_completed(task_id)
                print("Task marked as completed.")
            else:
                print("No pending tasks found.")
        
        elif choice == '5':
            print("\n--- Delete Task ---")
            tasks = task_manager.list_tasks()
            if tasks:
                print_task_table(tasks)
            task_id = input("Enter Task ID to delete: ")
            task_manager.delete_task(task_id)
            print("Task deleted successfully.")
        
        elif choice == '0':
            print("Exiting Task Manager. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
