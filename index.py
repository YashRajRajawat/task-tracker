from datetime import datetime
import re #built in module for regex
import time
import json

numPosPattern = "^[1-9]\\d*$"

def addTask():
    try:
        with open('tasks.json', 'r') as file:
            data_list = json.load(file)
    except FileNotFoundError:
        data_list = []

    max_id = 0
    id = 0

    if len(data_list) != 0:
        for tasks in data_list:
            id = tasks.get("id")
            max_id = max(id, max_id)

    id = max_id + 1

    while True:
        description = input("Enter task description: \n> ")
        if re.match("^.{0}$", description):
            print("empty input!!!")
            continue
        elif (not (re.match("^.{1,100}$", description))):
            print("exceeding 100 chars")
            continue
        else:
            break
    
    status = "To-do"
    createdAt = datetime.now()
    updatedAt = datetime.now()

    data = {
        "id": id,
        "description": description,
        "status": status,
        "Created At": createdAt.strftime("%d/%m/%Y, %H:%M:%S"),
        "Last Updated At": updatedAt.strftime("%d/%m/%Y, %H:%M:%S")
    }

    data_list.append(data)

    with open('tasks.json', 'w') as file:
        json.dump(data_list, file, indent=2)

    print("Task Added Successfully with ID", id)

def updateTask():
    try:
        with open('tasks.json', 'r') as file:
            data_list = json.load(file)
    except FileNotFoundError:
        return print("Add a task first.")
    
    if len(data_list) == 0:
        return print("No tasks found.")

    while True:
        id_input = input("Enter Task ID for Updatation: \n> ")
        if re.match("^.{0}$", id_input):
            print("empty input!!!")
            continue
        elif (not (re.match(numPosPattern, id_input))):
            print("Wrong input!!")
            continue
        else:
            break

    for tasks in data_list:
        if int(id_input) == tasks.get("id"):
            newDescription = input("New description for task " + tasks.get("description") + " and ID " + id_input + "\n> ")
            newUpdatedAt = datetime.now()
            tasks['description'] = newDescription
            tasks['Last Updated At'] = newUpdatedAt.strftime("%d/%m/%Y, %H:%M:%S")
            break
    else:
        return print("No Such ID Found.")
        
    with open('tasks.json', 'w') as file:
        json.dump(data_list, file, indent=2)

    print(id_input + " ID task updated succesfully.")

def deleteTask():
    try:
        with open('tasks.json', 'r') as file:
            data_list = json.load(file)
    except FileNotFoundError:
        return print("Add a task first.")
    
    if len(data_list) == 0:
        return print("No tasks found.")

    while True:
        id_input = input("Enter Task ID for Updatation: \n> ")
        if re.match("^.{0}$", id_input):
            print("empty input!!!")
            continue
        elif (not (re.match(numPosPattern, id_input))):
            print("Wrong input!!")
            continue
        else:
            break

    for tasks in data_list:
        if int(id_input) == tasks.get("id"):
            data_list.remove(tasks)
            break
    else:
        return print("No Such ID Found.")
    
    with open('tasks.json', 'w') as file:
        json.dump(data_list, file, indent=2)

    print(id_input + " ID task deleted successfully.")

def markInProgress():
    try:
        with open('tasks.json', 'r') as file:
            data_list = json.load(file)
    except FileNotFoundError:
        return print("Add a task first.")
    
    if len(data_list) == 0:
        return print("No tasks found.")
    
    while True:
        id_input = input("Enter Task ID to be marked in-progress: \n> ")
        if re.match("^.{0}$", id_input):
            print("empty input!!!")
            continue
        elif (not (re.match(numPosPattern, id_input))):
            print("Wrong input!!")
            continue
        else:
            break

    for tasks in data_list:
        if int(id_input) == tasks.get("id"):
            newUpdatedAt = datetime.now()
            tasks['status'] = "In-Progress" 
            tasks['Last Updated At'] = newUpdatedAt.strftime("%d/%m/%Y, %H:%M:%S")
            break
    else:
        return print("No Such ID Found.")
        
    with open('tasks.json', 'w') as file:
        json.dump(data_list, file, indent=2)

    print(id_input + " ID task marked as in-progress.")

def markDone():
    try:
        with open('tasks.json', 'r') as file:
            data_list = json.load(file)
    except FileNotFoundError:
        return print("Add a task first.")
    
    if len(data_list) == 0:
        return print("No tasks found.")

    while True:
        id_input = input("Enter Task ID to be marked done: \n> ")
        if re.match("^.{0}$", id_input):
            print("empty input!!!")
            continue
        elif (not (re.match(numPosPattern, id_input))):
            print("Wrong input!!")
            continue
        else:
            break

    for tasks in data_list:
        if int(id_input) == tasks.get("id"):
            newUpdatedAt = datetime.now()
            tasks['status'] = "Done" 
            tasks['Last Updated At'] = newUpdatedAt.strftime("%d/%m/%Y, %H:%M:%S")
            break
    else:
        return print("No Such ID Found.")
        
    with open('tasks.json', 'w') as file:
        json.dump(data_list, file, indent=2)

    print(id_input + " ID task marked as Done.")

def listAll():
    try:
        with open('tasks.json', 'r') as file:
            data_list = json.load(file)
    except FileNotFoundError:
        return print("Add a tasks first.")
    
    if len(data_list) == 0:
        return print("No tasks found.")
    
    for tasks in data_list:
        print(tasks)
    
def viewDoneTasks():
    try:
        with open('tasks.json', 'r') as file:
            data_list = json.load(file)
    except FileNotFoundError:
        return print("Add a task first.")
    
    if len(data_list) == 0:
        return print("No tasks found.")

    for tasks in data_list:
        if "Done" == tasks.get("status"):
            print(tasks)

def viewTodoTasks():
    try:
        with open('tasks.json', 'r') as file:
            data_list = json.load(file)
    except FileNotFoundError:
        return print("Add a task first.")
    
    if len(data_list) == 0:
        return print("No tasks found.")

    for tasks in data_list:
        if "To-do" == tasks.get("status"):
            print(tasks)

def viewInProgressTasks():
    try:
        with open('tasks.json', 'r') as file:
            data_list = json.load(file)
    except FileNotFoundError:
        return print("Add a task first.")
    
    if len(data_list) == 0:
        return print("No tasks found.")

    for tasks in data_list:
        if "In-Progress" == tasks.get("status"):
            print(tasks)

def viewStatus():
    print("1. View Done tasks")
    print("2. View todo tasks")
    print("3. View in-progress tasks")
    choice = input("Enter your choice: \n> ")
    match choice:
        case "1":
            viewDoneTasks()
        case "2":
            viewTodoTasks()
        case "3":
            viewInProgressTasks()
        case '':
            print("Invalid Input!!")
        case _:
            print("Invalid Input!!")


# print(f""" __    __     _                            _          _            _      _                  _             
# / / /\ \ \___| | ___ ___  _ __ ___   ___  | |_ ___   | |_ __ _ ___| | __ | |_ _ __ __ _  ___| | _____ _ __ 
# \ \/  \/ / _ \ |/ __/ _ \| '_ ` _ \ / _ \ | __/ _ \  | __/ _` / __| |/ / | __| '__/ _` |/ __| |/ / _ \ '__|
#  \  /\  /  __/ | (_| (_) | | | | | |  __/ | || (_) | | || (_| \__ \   <  | |_| | | (_| | (__|   <  __/ |   
#   \/  \/ \___|_|\___\___/|_| |_| |_|\___|  \__\___/   \__\__,_|___/_|\_\  \__|_|  \__,_|\___|_|\_\___|_| \n\n""")

while True:
    print("1. Add a Task")
    print("2. Update Task")
    print("3. Delete Task")
    print("4. Mark task in progress")
    print("5. Mark task as done")
    print("6. View All Tasks")
    print("7. View by Status")
    print("8. Exit")
    choice = input("Enter your choice: \n> ")
    match choice:
        case "1":
            addTask()
        case "2":
            updateTask()
        case "3":
            deleteTask()
        case "4":
            markInProgress()
        case "5":
            markDone()
        case "6":
            listAll()
        case "7":
            viewStatus()
        case "8":
            print("Exiting the program")
            time.sleep(2)
            break
        case '':
            print("Invalid Input!!")
        case _:
            print("Invalid Input!!")
