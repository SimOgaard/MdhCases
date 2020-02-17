#att göra lista
import pickle
import os
import json
längd = 60
linje = ("_"*längd)
thisdict = {}
menu = ["List   | List todo","Add    | Add todo","Check  | check todo","Delete | delete todo",linje,"Save   | Save todo to files", "Load   | Load todo from files", linje]
metod = ["list", "add", "check", "delete", "save", "load"]
def meny():
    print(linje)
    titel= "Todify"
    print(titel.center(längd))
    print(linje)
    for i in menu:
        print(i)

def funktioner(ska):
    if ska == "add": #Lägger till objekt
        try:
            key=input("Todo description: ")
            thisdict[str(key)] = "[ ]"
        except:
            print("Something went wrong")
    elif ska == "list": # Skriver ut alla objekt och deras värden
        for x, i in thisdict.items():
            print(i,x)
    elif ska == "check":  #Markerar i listan 
            for x, i in thisdict.items():
                print(i,x)
            check = input("What do you want to check or uncheck? ")
            for x in thisdict:
                if x == str(check):
                    if thisdict[str(x)] == "[ ]":
                        thisdict[str(x)] = "[✓]"
                        break
                    elif thisdict[str(x)] == "[✓]":
                        thisdict[str(x)] = "[ ]"
                        break
            else:
                print("Error", check,"was not in the list")
    elif ska =="delete": # Tar bort objekt i listan
        for x, i in thisdict.items():
                print(i,x)
        delete = input("What do you want to delete? ")
        if str(delete) in thisdict:
            del thisdict[str(delete)]
    elif ska == "save": #Sparar filen som binär i datorn
        try:
            save = input("Name the file ")
            with open(save+".txt", 'w') as outfile:
                json.dump(thisdict, outfile)
            
            # save2 = save+".dat"
            # print(save,"was saved on you computer")
            # pickle.dump(thisdict, open(save2, "wb"))
        except: print("404 error with")
    elif ska == "load": #Ladar in data från datorn
        try:
            load = input("Name the file ")
            load2 = load+".dat"
            test = open(str(load2),"rb")
            ut = pickle.load(test)     
            thisdict.update(ut)
        except: 
            FileNotFoundError
            print("error")
    input("Press enter to continue")

while True:
    meny()
    y = input("Choose method ")
    if y.lower() in metod:
        funktioner(y)
    os.system("cls")
