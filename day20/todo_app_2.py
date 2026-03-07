import json
# cli_todo v2 with little improvements

# Create a todo class
class Todo:
  def __init__(self,task,due_date_time,priority,category):
    self.task=task
    self.due_date_time=due_date_time
    self.priority=priority
    self.category = category
  def todict(self):
    return{
      'task': self.task,
      'due_date_time': self.due_date_time,
      'priority': self.priority,
      'category': self.category,
    }
# todo list that contains file contents later
todos = []

try: #try opening a file notify the user if the file doesn't exist or not found
  with open("new_todo_file.json","r") as f:
    try:
      todos = json.load(f) # takes what ever is in new_todo_file.json and dumps in todos list
    except:
      print("there is an error")
except FileNotFoundError:
  print("File not found!")

# The main user interaction center
while True:
  cmd = input("What do you want to do? \n\t c - create a new todo\n\t l - list your todos\n\t d - delete your todo \n\t e - exit the loop\n")

  if cmd=="c":
    task = input("Task: ")
    due_date_time = input("Due date and time: ")
    priority = input("How urgent: ")
    category = input("Category: ")
    with open("new_todo_file.json","w") as f:
      todo = Todo(task,due_date_time,priority,category).todict()
      todos.append(todo)
      json.dump(todos,f,indent=2,sort_keys=True) # converting todos to a json file

  elif cmd == "l":
    try:
      with open("new_todo_file.json","r") as f:
        task_numb = 1
        if not todos: #check if the todos list is empty
          print("No todos yet")
        else:
          print("*******************************************************")
          for task in todos:
            print(f"{task_numb}. {task['task']}\n\t Due date/time: {task['due_date_time']}\n\t Priority: {task['priority']}\n\t Category: {task['category']}")
            task_numb+=1
          print("*******************************************************")
    except FileNotFoundError:
      print("File not found!")

  elif cmd=="d":
    task_del = input("Enter EXACT name of task name: ")
    new_todo = []
    found = False
    for t in todos:
      if t['task']!=task_del:
        new_todo.append(t)
      else:
        found = True
    if found:
      todos = new_todo
      with open("new_todo_file.json","w") as f:
        json.dump(todos, f, indent=4)
      print("Task deleted!")
    else:
      print("Task not found!")
  elif cmd=="e":
    print("exiting...")
    break
  else:
    print("use only c, d, l or e")

