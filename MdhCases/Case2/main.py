#Kursnamn: dva128 programmeringsteknik med python
#Gruppnamn: Enemy Dough
#Gruppmedlemmar: Nils Borg, Simon Ögaard Jozic, Brian Nguyen

import time
import os
import json

rainbowColors=['\033[31m','\033[38;2;243;134;48m','\033[33m','\033[32m','\033[34m','\033[35m']
todos={
    "todo":[],
    "check": []
}

options = ["list  | list Todos", "add   | add a Todo ", "check | check/uncheck a Todo", "del   | delete a Todo  ", "save  | save Todos to file ", "load  | load Todos from file" ]

length = 30

if not os.path.exists("todo"): os.makedirs("todo")
def rainbow(string):
    printint =i
    for char in string:
        if printint >= 6: printint = 0
        print(rainbowColors[printint]+char, end="")
        printint += 1
    print("")

def writerow(icon):
    rainbow(icon*length)

def centertext(text):
    rainbow(text.center(length))

def menu():
    writerow("*")
    centertext("Todoify")
    writerow("-")
    for x in options: rainbow(x)
    writerow("-")

def printTodo():
    loop=0
    while loop<len(todos["todo"]):
        if todos["check"][loop]==True:
            print("[✓] | ["+ str(loop) + "] " + todos["todo"][loop])
        else:
            print("[ ] | ["+ str(loop) + "] " + todos["todo"][loop])
        loop+=1

while True:
    for x in range(5):
        for i in range(6):
            printint=i
            os.system('cls')
            menu()
            time.sleep(1/60)



    select=input("What do you want to do?: ").lower()

    if select=="list":
        printTodo()
    elif select=="add":
        todos["todo"].append(input("What do you want to add?: "))
        todos["check"].append(False)
        printTodo()
    elif select=="check":
        printTodo()
        indx=input("Which Todo (index) do you want to check/uncheck?: ")
        try:
            intindx=int(indx)
            todos["check"][intindx]=not todos["check"][intindx]
            printTodo()
        except:
            print("Invalid index " + indx)
    elif select=="del":
        printTodo()
        indx=input("Which Todo (index) do you want to delete: ")
        try:
            intindx=int(indx)
            todos["todo"].pop(intindx)
            todos["check"].pop(intindx)
            printTodo()
        except:
            print("Invalid index "+ indx)
    elif select == "load":
        print("Available files:")
        for x in os.listdir("todo/"):
            if x.endswith(".json"):
                print(x[:-5])
        name = input("What file do you want to open?:")
        try:
            todos.update(json.load(open("todo/"+name+'.json')))
            printTodo()
        except:
            print("Invalid file name "+ name)
    elif select=="save":
        printTodo()
        name=input("What do you want the file to be named?: ")
        json.dump(todos, open("todo/"+name+'.json', 'w'))
    else:
        print(select+" is not an option")
    input("Press enter to continue...")