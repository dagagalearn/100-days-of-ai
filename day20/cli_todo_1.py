import json

class Todo:
    def __init__(self, task, due_time, priority):
        self.task = task
        self.due_time = due_time
        self.priority = priority

    def to_dict(self):
        return {
            "todo": self.task,
            "due_time": self.due_time,
            "priority": self.priority
        }

with open("todo.json", "r") as file:
    todos = json.load(file)

while True:
    cmd = input("\nChoose an action:\n\tc - create task\n\tl - list tasks\n\td - delete task\n\te - exit\n").lower()

    if cmd == "c":
        task = input("Task: ")
        due = input("Due time: ")
        priority = input("Priority: ")

        task_dict = Todo(task, due, priority).to_dict()
        todos.append(task_dict)

        with open("todo.json", "w") as file:
            json.dump(todos, file, indent=4)

        print("Task added!")

    elif cmd == "l":
        if not todos:
            print("No tasks yet!")
        else:
            task_number = 1
            for t in todos:
                print(str(task_number) + ". " + t["todo"] + " | Due: " + t["due_time"] + " | Priority: " + t["priority"])
                task_number += 1

    elif cmd == "d":
        del_task = input("Enter the exact name of the task to delete: ")

        new_todos = []
        found = False
        for t in todos:
            if t["todo"] != del_task:
                new_todos.append(t)
            else:
                found = True

        if found:
            todos = new_todos
            with open("todo.json", "w") as file:
                json.dump(todos, file, indent=4)
            print("Task deleted!")
        else:
            print("Task not found!")

    elif cmd == "e":
        print("Exiting program...")
        break

    else:
        print("Invalid command. Please choose c, l, d, or e.")
