---

# 📝 Python To-Do CLI

A simple **Command-Line To-Do List** built in Python.
You can add tasks, list them, and mark them as complete. Tasks are stored in a JSON file so they persist between runs.

---

## 📌 Features

* ✅ Add tasks
* 📃 List all tasks
* 🎉 Mark tasks as complete
* 💾 Persistent storage using `tasks.json`

---

## ⚡ Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/python-todo-cli.git
   cd python-todo-cli
   ```

2. Make sure you have **Python 3** installed:

   ```bash
   python --version
   ```

---

## ▶️ Usage

Run the script using Python:

```bash
# Add a new task
python todo.py add "Learn Python"

# List all tasks
python todo.py list

# Mark task 1 as done
python todo.py done 1
```

---

## 📂 Project Structure

```
python-todo-cli/
│── todo.py        # Main CLI program
│── tasks.json     # Task storage file (auto-created)
│── README.md      # Project documentation
```

---

## 🌟 Example

```bash
$ python todo.py add "Finish homework"
✅ Task added: Finish homework

$ python todo.py list
1. Finish homework [❌]

$ python todo.py done 1
🎉 Task 1 marked as complete!

$ python todo.py list
1. Finish homework [✔️]
```

---

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you’d like to improve.

---

Would you like me to also **generate the GitHub commands** (init, add, commit, push) so you can upload this Python project easily like you did with the Go one?
