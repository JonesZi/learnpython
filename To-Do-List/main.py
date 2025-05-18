import argparse
from tasks import list_tasks, add_task, mark_task_done, delete_task
from storage import clear_tasks

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