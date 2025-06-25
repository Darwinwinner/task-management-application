from db import get_db_collection
from task import Task 
from file_storage import save_tasks_to_file, load_tasks_from_file

# TaskManager Class
class TaskManager:

    # Initializes the TaskManager with a database collection
    def __init__(self):
        self.collection = get_db_collection()
    
    # Generates a new task ID based on the last task in the collection
    def _generate_task_id(self):
        tasks = list(self.collection.find().sort("_id"))
        if not tasks:
            return "001"
        last_id = tasks[-1]["_id"]
        new_id = int(last_id) + 1
        return str(new_id).zfill(3)
    
    # Adds a new task to the collection and syncs to file
    def add_task(self, title, description, due_date, priority):
        task_id = self._generate_task_id()
        task = Task(task_id, title, description, due_date, priority)
        self.collection.insert_one(task.to_dict())
        self._sync_to_file()

    # Lists all tasks in the collection
    def list_tasks(self):
        tasks = list(self.collection.find())
        return tasks

    # Lists all pending tasks in the collection
    def list_pending_tasks(self):
        return list(self.collection.find({"status": "Pending"}))

    # Lists all completed tasks in the collection
    def mark_completed(self, task_id):
        self.collection.update_one({"_id": task_id}, {"$set": {"status": "Completed"}})

    # Deletes a task from the collection and syncs to file
    def delete_task(self, task_id):
        self.collection.delete_one({"_id": task_id})
        self._sync_to_file()

    # Updates a specific field of a task and syncs to file
    def update_task(self, task_id, field, new_value):
        self.collection.update_one({"_id": task_id}, {"$set": {field: new_value}})
        self._sync_to_file()

    # Synchronizes the current state of tasks to a file
    def _sync_to_file(self):
        tasks =  [Task.from_dict(t) for t in self.collection.find()]
        save_tasks_to_file(tasks)

    
