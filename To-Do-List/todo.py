import argparse
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

def list_tasks():
    """List all tasks."""
    tasks = load_tasks()
    if not tasks:
        print("No tasks found.")
    else:
        for i, task in enumerate(tasks, start=1):
            status = "[x]" if task["done"] else "[ ]"
            print(f"{status} {i}. {task['task']}")

def add_task(task_name):
    """Add a new task."""
    tasks = load_tasks()
    tasks.append({"task": task_name, "done": False})
    save_tasks(tasks)
    print(f"✅ Task '{task_name}' added.")


def mark_task_done(task_index):
    """Mark a task as done."""
    tasks = load_tasks()
    if 0 <= task_index < len(tasks):
        tasks[task_index]["done"] = True
        save_tasks(tasks)
        print(f"✅ Task '{tasks[task_index]['task']}' marked as done.")
    else:
        print("❌ Invalid task index.")

def delete_task(task_index):
    """Delete a task."""
    tasks = load_tasks()
    if 0 <= task_index < len(tasks):
        deleted_task = tasks.pop(task_index)
        save_tasks(tasks)
        print(f"✅ Task '{deleted_task['task']}' deleted.")
    else:
        print("❌ Invalid task index.")

def clear_tasks():
    """Clear all tasks."""
    if os.path.exists(DATA_FILE):
        os.remove(DATA_FILE)
        print("✅ All tasks cleared.")
    else:
        print("❌ No tasks to clear.")

def main():
    parser = argparse.ArgumentParser(description="Simple To-Do List CLI")
    parser.add_argument("command", choices=["list", "add", "done", "delete", "clear"], help="Command to execute")
    parser.add_argument("task", nargs="?", help="Task name or index")

    args = parser.parse_args()

    if args.command == "list":
        list_tasks()
    elif args.command == "add":
        if args.task:
            add_task(args.task)
        else:
            print("❌ Please provide a task name.")
    elif args.command == "done":
        if args.task and args.task.isdigit():
            mark_task_done(int(args.task) - 1)
        else:
            print("❌ Please provide a valid task index.")
    elif args.command == "delete":
        if args.task and args.task.isdigit():
            delete_task(int(args.task) - 1)
        else:
            print("❌ Please provide a valid task index.")
    elif args.command == "clear":
        clear_tasks()

if __name__ == "__main__":
    main()
    