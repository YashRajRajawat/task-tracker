from datetime import datetime
import re #built in module for regex
import time

numPosPattern = "^[1-9]\\d*$"

def addTask():
    id = input("Enter Id of task: \n> ")
    if not (re.match(numPosPattern, id)):
        print("invalid input!!!")
        return

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

    print("Task Added Successfully")

print(f""" __    __     _                            _          _            _      _                  _             
/ / /\ \ \___| | ___ ___  _ __ ___   ___  | |_ ___   | |_ __ _ ___| | __ | |_ _ __ __ _  ___| | _____ _ __ 
\ \/  \/ / _ \ |/ __/ _ \| '_ ` _ \ / _ \ | __/ _ \  | __/ _` / __| |/ / | __| '__/ _` |/ __| |/ / _ \ '__|
 \  /\  /  __/ | (_| (_) | | | | | |  __/ | || (_) | | || (_| \__ \   <  | |_| | | (_| | (__|   <  __/ |   
  \/  \/ \___|_|\___\___/|_| |_| |_|\___|  \__\___/   \__\__,_|___/_|\_\  \__|_|  \__,_|\___|_|\_\___|_| \n\n""")

while True:
    print("1. Add a task")
    print("2. Exit")
    choice = input("Enter your choice: \n> ")
    match choice:
        case "1":
            addTask()
        case "2":
            print("Exiting the program")
            time.sleep(2)
            break
        case '':
            print("Invalid Input!!")
        case _:
            print("Invalid Input!!")
