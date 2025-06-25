import json
from task import Task

BACKUP_FILE = "tasks_backup.json"

# Function to save tasks to a JSON file (backup)
def save_tasks_to_file(tasks):
    with open(BACKUP_FILE, 'w') as file:
        json.dump([task.to_dict() for task in tasks], file, indent=4)

# Function to load tasks from a JSON file 
def load_tasks_from_file():
    try:
        with open(BACKUP_FILE, 'r') as file:
            data = json.load(file)
            return [Task.from_dict(task_data) for task_data in data]
    except FileNotFoundError:
        return []
