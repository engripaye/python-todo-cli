import sys
import json
import os

# File to store tasks
TASKS_FILE = "tasks.json"


def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as f:
            return json.load(f)
    return []


def save_tasks(tasks):
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f, indent=2)


def add_task(task):
    tasks = load_tasks()
    tasks.append({"task": task, "done": False})
    save_tasks(tasks)
    print(f"✅ Added task: {task}")


def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print("📭 No tasks yet!")
        return
    print("\n📋 Your To-Do List:")
    for i, t in enumerate(tasks, 1):
        status = "✔️" if t["done"] else "❌"
        print(f"{i}. {t['task']} [{status}]")


def complete_task(index):
    tasks = load_tasks()
    if 0 < index <= len(tasks):
        tasks[index - 1]["done"] = True
        save_tasks(tasks)
        print(f"🎉 Task {index} marked as completed!")
    else:
        print("⚠️ Invalid task number.")


def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py [add|list|done] [task]")
        return

    command = sys.argv[1]

    if command == "add":
        if len(sys.argv) < 3:
            print("⚠️ Please provide a task.")
        else:
            task = " ".join(sys.argv[2:])
            add_task(task)

    elif command == "list":
        list_tasks()

    elif command == "done":
        if len(sys.argv) < 3:
            print("⚠️ Please provide a task number to mark as done.")
        else:
            try:
                index = int(sys.argv[2])
                complete_task(index)
            except ValueError:
                print("⚠️ Task number must be an integer.")

    else:
        print("⚠️ Unknown command. Use: add, list, done")


if __name__ == "__main__":
    main()
