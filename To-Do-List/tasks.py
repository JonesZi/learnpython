from storage import load_tasks, save_tasks

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

