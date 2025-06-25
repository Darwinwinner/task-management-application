# Task Management CLI Application

A command-line interface (CLI) task manager built in Python that allows users to add, view, update, mark, and delete tasks using MongoDB as the primary database with JSON file backup.

---

## Features

* Add a new task with validation for due date and priority
* List all tasks in a formatted table view (Notion-style)
* Update specific fields of a task
* Mark a task as completed (only displays pending ones)
* Delete a task by ID
* Data is stored in MongoDB and backed up in a local JSON file

---

## Setup Instructions

### 1. Clone the Repository

```bash
$ git clone <your-repo-url>
$ cd <repo-folder>
```

### 2. Install Python Dependencies

Make sure you are using Python 3. Then install required libraries:

```bash
pip install pymongo
```

### 3. Set Up MongoDB

Make sure MongoDB is installed and running on your machine. You can download it from: [https://www.mongodb.com/try/download/community](https://www.mongodb.com/try/download/community)

### 4. Create Configuration File

Create a `config.ini` file in the root directory:

```ini
[mongodb]
uri = mongodb://localhost:27017
database = task_manager_db
collection = tasks
```

You can modify the URI, database name, and collection name as needed.

### 5. Run the Application

```bash
python main.py
```

Use the numbered menu to navigate through available actions.

---

## Sample Usage

```
=== Task Management ===
[1] Add a new task
[2] List all tasks
[3] Update a task's details
[4] Mark a task as completed
[5] Delete a task
[0] Exit
```

---

## License

This project is for technical assessment and educational purposes.
