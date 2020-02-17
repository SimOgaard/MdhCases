import os
import requests
import itertools
import random

options=["List available seasons", "View table for season", "Exit Football frenzy"]
rainbowColors=['\033[31m','\033[38;2;243;134;48m','\033[33m','\033[32m','\033[34m','\033[35m']
Messages = ["hotel?", "trivago"]
url = "http://football-frenzy.s3-website.eu-north-1.amazonaws.com/api"
Gray = "\033[0m"

def rainbow(string):
    for Amount, Char in enumerate(string):
        if Char =="|" or Char == "+" or Char == "─" or Char == "#":
            print(rainbowColors[Amount % len(rainbowColors)]+Char, end="")
        else:
            print(Gray+Char, end="")
    print(Gray)

def inputs(string):
    return input(rainbowColors[0] + "| " + Gray + string).replace(" ", "").lower()

def line(char,length):
    rainbow("+" + char*length + "+")

def center(string,length):
    rainbow("|" + string.center(length) + "|")

def menu():
    os.system("cls")
    line("─",30)
    center("Football frenzy",30)
    center("Turbo stat viewer",30)
    line("─",30)
    for option in options:
        rainbow("| " + option[:4] + " | " + option)
    line("─",30)

def listera():
    SeasonYears = requests.get(url).json()["seasons"]
    for Year in range(0, len(SeasonYears), 5):
        print(rainbowColors[0] + "| " + Gray, end="")
        print(*SeasonYears[Year:Year+5], sep = ", ")
    line("─",30)

def gettable():
    ViewYear = inputs("Year > ")
    SeasonYears = requests.get(url).json()["seasons"]
    for Year in SeasonYears:
        if Year == ViewYear:
            SeasonYear = requests.get(url+"/"+ViewYear).json()
            YearDict = {i : {"W":0,"D":0,"L":0,"P":0} for i in SeasonYear["teams"]}
            SetProcent = LoadAmount = len(SeasonYear["gamedays"])
            LoadStart = 0
            Message = Messages[random.randint(0, len(Messages)-1)]
            for GameDays in SeasonYear["gamedays"]:
                GameDay = requests.get(url+"/"+ViewYear+"/"+GameDays).json()
                for Games in GameDay["games"]:
                    GameHome = Games["score"]["home"]
                    GameAway = Games["score"]["away"]
                    YearDict[GameHome["team"]]["P"]+=GameHome["goals"]
                    YearDict[GameAway["team"]]["P"]+=GameAway["goals"]
                    if GameHome["goals"] == GameAway["goals"]:
                        YearDict[GameHome["team"]]["D"]+=1
                        YearDict[GameAway["team"]]["D"]+=1
                    elif GameHome["goals"] > GameAway["goals"]:
                        YearDict[GameHome["team"]]["W"]+=1
                        YearDict[GameAway["team"]]["L"]+=1
                    else: 
                        YearDict[GameHome["team"]]["L"]+=1
                        YearDict[GameAway["team"]]["W"]+=1
                LoadAmount-=1
                LoadStart+=1
                os.system("cls")
                print(Message.center(len(SeasonYear["gamedays"])+8))
                rainbow("["+"#"*LoadStart+" "*LoadAmount+"] "+str(int(LoadStart/SetProcent*100))+" %")
            printtable(dict(sorted(YearDict.items(), key = lambda x: x[1]["P"],reverse=True)))
            break
    else:
        rainbow("| No such year exists")

def printtable(table):
    IndenteringTeam = max(map(len, table)) + 2
    os.system("cls")
    head = "| "+"Teams".center(IndenteringTeam)+"|"+"W".center(4)+"|"+"D".center(4)+"|"+"L".center(4)+"|"+"P".center(4)+"|"
    line("─",len(head)-2)
    rainbow(head)
    line("─",len(head)-2)
    for Team, Summary in table.items():
        rainbow("| " + Team + " " * (IndenteringTeam-len(Team)) +"|" + str(Summary["W"]).center(4) + "|" + str(Summary["D"]).center(4) + "|" + str(Summary["L"]).center(4) + "|" + str(Summary["P"]).center(4) + "|")
    line("─",len(head)-2)

while True:
    menu()
    Selection = inputs("Selection > ")
    line("─",30)
    if Selection == "list":
        listera()
    elif Selection == "view":
        gettable()
    elif Selection == "exit":
        break
    else:
        rainbow("| Invalid option")
        line("─",30)
    Selection = inputs("Press enter to continue...")