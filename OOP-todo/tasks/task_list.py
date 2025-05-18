import json
import os
from .task import Task

DATA_FILE = "data.json"

class TaskList:
    def __init__(self):
        self.tasks = self.load()

    def add(self, description, priority="mittel"):
        task = Task(description, priority=priority)
        self.tasks.append(task)
        self.save()
        print(f"✅ Task '{description}' added.")

    def list(self):
        if not self.tasks:
            print("📭 No tasks found.")
            return

        for i, task in enumerate(self.tasks, 1):
            print(f"{i}. {task}")

    def mark_done(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_done()
            self.save()
            print(f"✅ Task '{self.tasks[index].description}' marked as done.")
        else:
            print("❌ Invalid task index.")

    def delete(self, index):
        if 0 <= index < len(self.tasks):
            removed = self.tasks.pop(index)
            self.save()
            print(f"🗑️ Task '{removed.description}' deleted.")
        else:
            print("❌ Invalid task index.")

    def clear(self):
        self.tasks = []
        self.save()
        print("🧹 All tasks cleared.")

    def save(self):
        with open(DATA_FILE, "w") as f:
            json.dump([task.to_dict() for task in self.tasks], f)

    def load(self):
        if not os.path.exists(DATA_FILE):
            return []
        with open(DATA_FILE, "r") as f:
            return [Task.from_dict(item) for item in json.load(f)]
