import json
import os

DATA_FILE = "data.json"

def load_tasks():
    """Load tasks from the JSON file."""
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    return []

def save_tasks(tasks):
    """Save tasks to the JSON file."""
    with open(DATA_FILE, "w") as file:
        json.dump(tasks, file)

def clear_tasks():
    """Clear all tasks."""
    if os.path.exists(DATA_FILE):
        os.remove(DATA_FILE)
        print("✅ All tasks cleared.")
    else:
        print("❌ No tasks to clear.")