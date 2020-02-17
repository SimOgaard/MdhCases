import os
import pandas as pd

lila = '\033[95m'
gul = '\033[93m'
röd = '\033[91m'

def header(head):
    print(lila+head.center(21))

def line(typ):
    print(lila+typ*21)

todos = pd.DataFrame(columns=["Check","Todo"])
if not os.path.exists("todos"): os.makedirs("todos")

while True:
    os.system("cls")
    line("*")
    header("Todo")
    line("-")
    for x in ["list ", "add  ", "check", "del  "]: print(gul+ x + " | " + x.replace(" ", "") + " todo")
    line("-")
    for x in ["save ", "load "]: print(gul+ x + " | " + x.replace(" ", "") + " todo")
    line("-")
    selection = input(gul+"Selection > ").lower()
    if selection == "list" and not todos.empty: print(todos)
    elif selection == "list": print(röd+"Error: Empty dataframe")
    elif selection == "add": todos = todos.append({"Check":"[ ]","Todo":input(gul+"Description > ")}, ignore_index=True)
    while not todos.empty:
        try:
            if selection == "check":
                index = input(gul+"Index > ")
                if todos.loc[int(index), "Check"] == "[ ]": todos.loc[int(index), "Check"] = "[X]"
                else: todos.loc[index, "Check"] = "[ ]"
            elif selection == "del": 
                index = input(gul+"Index > ")
                todos = todos.drop(index=[int(index)])
                todos = todos.reset_index(drop=True)
                print(gul+"Deleted todo at index: "+str(index))
            break
        except: print(röd + "ERROR: Invalid index '" + str(index) + "' does not exist")
    else:
        if selection == "check" or selection == "del": print(röd+"ERROR: Todos has no index")
    while 1+1==2:
        try:
            if selection == "save": todos.to_csv("todos/"+input("Todo name: ")+".csv")
            if selection == "load": todos = pd.read_csv(("todos/"+input(gul+"Todo name: ")+".csv"), parse_dates=True, index_col=0)
            break
        except: print(röd+"ERROR: Name insufficient")
    line("-")
    input(gul+"Continue?")