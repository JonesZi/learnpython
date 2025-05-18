import argparse
from tasks.task_list import TaskList

def main():
    parser = argparse.ArgumentParser(description="📝 To-Do CLI")
    parser.add_argument("command", choices=["list", "add", "done", "delete", "clear"])
    parser.add_argument("value", nargs="?", help="Task description or index")
    parser.add_argument("--priority", choices=["hoch", "mittel", "niedrig"], default="mittel")

    args = parser.parse_args()
    task_list = TaskList()

    if args.command == "list":
        task_list.list()

    elif args.command == "add":
        if args.value:
            task_list.add(args.value, args.priority)
        else:
            print("❌ Please provide a task description.")

    elif args.command == "done":
        if args.value and args.value.isdigit():
            task_list.mark_done(int(args.value) - 1)
        else:
            print("❌ Please provide a valid task index.")

    elif args.command == "delete":
        if args.value and args.value.isdigit():
            task_list.delete(int(args.value) - 1)
        else:
            print("❌ Please provide a valid task index.")

    elif args.command == "clear":
        task_list.clear()

if __name__ == "__main__":
    main()
