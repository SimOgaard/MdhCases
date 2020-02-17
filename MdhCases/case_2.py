import os
import json

rainbowcolours=['\033[31m','\033[38;2;243;134;48m','\033[33m','\033[32m','\033[34m','\033[35m']
todos={
    "todo": [],
    "check": []
}
options = ["list ", "add  ", "check", "del  ", "save ", "load " ]
length = 30

if not os.path.exists("todo"): os.makedirs("todo")

def rainbow(string):
    colourindex = 0
    for char in string:
        if colourindex == 6: colourindex = 0
        print(rainbowcolours[colourindex]+char, end="")
        colourindex += 1
    print("")

def writerow(icon):
    rainbow(icon*length)

def centertext(text):
    rainbow(text.center(length))

def menu():
    writerow("*")
    centertext("Todoify")
    writerow("-")
    for x in options: rainbow(x + " | " + x.replace(" ", "") + " todo")
    writerow("-")

def printTodo():
    x=0
    while x<len(todos["todo"]):
        if todos["check"][x]==True:
            print("[✓] | ["+ str(x) + "] " + todos["todo"][x])
        else:
            print("[ ] | ["+ str(x) + "] " + todos["todo"][x])
        x+=1

rainbow("██████      ██████")
rainbow("██████      ██████")
input("     continue")

while True:
    os.system('cls')
    menu()
    select=input("What to you want to do?: ").lower()

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