class Task:
    def __init__(self, description, done=False, priority="mittel"):
        self.description = description
        self.done = done
        self.priority = priority

    def mark_done(self):
        self.done = True

    def to_dict(self):
        return {
            "task": self.description,
            "done": self.done,
            "priority": self.priority
        }

    @staticmethod
    def from_dict(data):
        return Task(
            data["task"],
            data.get("done", False),
            data.get("priority", "mittel")
        )

    def __str__(self):
        status = "☑️" if self.done else "[ ]"
        return f"{status} {self.description} (Priority: {self.priority})"
