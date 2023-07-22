import argparse
import json
import os
from colorama import init, Fore, Style
from prettytable import PrettyTable

TASKS_FILE = "data.json"

def load_tasks():
    tasks = []  # Initialize tasks to an empty list
    if os.path.exists(TASKS_FILE) and os.path.getsize(TASKS_FILE) > 0:
        with open(TASKS_FILE, "r") as f:
            tasks = json.load(f)
    return tasks

def save_tasks(tasks):
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f)

def add_task(description):
    tasks = load_tasks()
    tasks.append({"description": description, "completed": False})
    save_tasks(tasks)
    print(f"{Fore.GREEN}Task added.{Style.RESET_ALL}")

def view_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks found.")
    else:
        table = PrettyTable()
        table.field_names = ["ID", "Description", "Completed"]
        for i, task in enumerate(tasks, start=1):
            status = "X" if task["completed"] else ""
            table.add_row([i, task["description"], status])
        print(table)

def complete_task(task_id):
    tasks = load_tasks()
    if 1 <= task_id <= len(tasks):
        tasks[task_id - 1]["completed"] = True
        save_tasks(tasks)
        print(f"{Fore.GREEN}Task completed.{Style.RESET_ALL}")
    else:
        print(f"{Fore.YELLOW}Invalid task ID.{Style.RESET_ALL}")

def delete_task(task_id):
    tasks = load_tasks()
    if 1 <= task_id <= len(tasks):
        del tasks[task_id - 1]
        save_tasks(tasks)
        print(f"{Fore.GREEN}Task deleted.{Style.RESET_ALL}")
    else:
        print(f"{Fore.YELLOW}Invalid task ID.{Style.RESET_ALL}")

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
        print(f"{Fore.YELLOW}Invalid command. Use 'tasks.py -h' for help.{Style.RESET_ALL}")

if __name__ == "__main__":
    init(autoreset=True)
    main()