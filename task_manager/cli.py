import argparse
from task_manager.tasks import add_task, view_tasks, complete_task, delete_task

def main():
    parser = argparse.ArgumentParser(description="CLI Task Manager")
    parser.add_argument("command", choices=["add", "view", "complete", "delete"], help="Command to execute")
    parser.add_argument("args", nargs="*", help="Arguments for the command")

    args = parser.parse_args()

    if args.command == "add":
        description = " ".join(args.args)
        add_task(description)
    elif args.command == "view":
        view_tasks()
    elif args.command == "complete":
        task_id = int(args.args[0])
        complete_task(task_id)
    elif args.command == "delete":
        task_id = int(args.args[0])
        delete_task(task_id)
    else:
        print("Invalid command. Use 'tasks.py -h' for help.")

if __name__ == "__main__":
    main()
    