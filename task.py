import datetime

# Task Class
class Task:

    # Initializes a task with the given parameters
    def __init__(self, task_id, title, description, due_date, priority, status = "Pending"):
        self.task_id = task_id
        self.title = title
        self.description = description
        self.due_date = due_date
        self.priority = priority
        self.status = status
        self.created_at = datetime.datetime.now()

    # Converts the task to a dictionary format for storage
    def to_dict(self):
        return {
            "_id": self.task_id,
            "title": self.title,
            "description": self.description,
            "due_date": self.due_date,
            "priority": self.priority,
            "status": self.status,
            "created_at": self.created_at.isoformat()
        }
    
    # Creates a Task instance from a dictionary representation
    @staticmethod
    def from_dict(data):
        task = Task(
            task_id = data["_id"],
            title = data["title"],
            description = data["description"],
            due_date = data["due_date"],
            priority = data["priority"],
            status = data.get("status", "Pending")
        )
        task.created_at = datetime.datetime.fromisoformat(data["created_at"])
        return task