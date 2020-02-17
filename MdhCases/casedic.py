import os
import json

lila = '\033[95m'
gul = '\033[93m'
röd = '\033[91m'

options = ["list ", "add  ", "check", "del  ", "save ", "load " ]
todos = {}

if not os.path.exists("todo"): os.makedirs("todo")

def header(head):
    print(lila+head.center(21))

def line(typ):
    print(lila+typ*21)

while True:
    os.system("cls")
    line("*")
    header("Todo")
    line("-")
    for x in options: print(gul+ x + " | " + x.replace(" ", "") + " todo")
    line("-")
    selection = input(gul+"Selection > ").lower()
    for items in options:
        if items.replace(" ", "") == selection and selection != "add" and selection != "load":
            for todo in todos:
                if todos[todo] == False: check = "[ ] "
                else: check = "[✓] "
                print(str(index) + " " + check + todo)
                index += 1
    index = 0
    if selection == "add": todos[input(gul+"Description > ")] = False
    if selection == "check" or selection == "del":
        indexx = input("Index > ")
        for todo in todos:
            if indexx == str(index):
                if selection == "del": del todos[todo]
                elif todos[todo] == False: todos[todo] = True
                else: todos[todo] = False
                break
            index += 1
        else: print(röd + "ERROR: Invalid index '" + str(index) + "' does not exist")
    if selection == 'save': json.dump(todos, open("todo/"+input(gul+'Name > ')+'.json', 'w'))
    elif selection == 'load':
        print([pos_json for pos_json in os.listdir("todo/") if pos_json.endswith('.json')])
        try: todos.update(json.load(open(input(gul+'Name > ')+'json.'))) 
        except: print(röd + "ERROR: Invalid filename")
    index = 0
    line("-")
    input(gul+"Continue?")