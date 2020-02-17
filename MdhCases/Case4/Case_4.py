import os
import requests
import random

options=["List available seasons", "View table for season", "Exit Football frenzy"]
rainbowColors=['\033[31m','\033[38;2;243;134;48m','\033[33m','\033[32m','\033[34m','\033[35m']
Messages = ["hotel?", "trivago"]
url = "http://football-frenzy.s3-website.eu-north-1.amazonaws.com/api"
Gray = "\033[0m"

def rainbow(string):
    for Amount, Char in enumerate(string):
        if Char == "|" or Char == "+" or Char == "─" or Char == "#":
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

def request(API):
    try:
        return requests.get(API).json() 
    except requests.exceptions.ConnectionError:
        rainbow("| API connection error")
        return None

def listera():
    SeasonYears = request(url)
    if SeasonYears:
        for Year in range(0, len(SeasonYears["seasons"]), 5):
            print(rainbowColors[0] + "| " + Gray, end="")
            print(*SeasonYears["seasons"][Year:Year+5], sep = ", ")
        line("─",30)

def scoreadder(YearDict, GameHome, GameAway):
    YearDict[GameHome["team"]]["GF"]+=GameHome["goals"]
    YearDict[GameAway["team"]]["GF"]+=GameAway["goals"]
    YearDict[GameHome["team"]]["GA"]+=GameAway["goals"]
    YearDict[GameAway["team"]]["GA"]+=GameHome["goals"]
    if GameHome["goals"] == GameAway["goals"]:
        YearDict[GameHome["team"]]["D"]+=1
        YearDict[GameAway["team"]]["D"]+=1
    elif GameHome["goals"] > GameAway["goals"]:
        YearDict[GameHome["team"]]["W"]+=1
        YearDict[GameAway["team"]]["L"]+=1
    else: 
        YearDict[GameHome["team"]]["L"]+=1
        YearDict[GameAway["team"]]["W"]+=1

def gettable():
    ViewYear = inputs("Year > ")
    SeasonYears = request(url)
    if SeasonYears != None:
        for Year in SeasonYears["seasons"]:
            if Year == ViewYear:
                SeasonYear = request(url+"/"+ViewYear)
                if SeasonYear != None:
                    YearDict = {team : {"GP":0,"W":0,"D":0,"L":0,"GF":0,"GA":0,"GD":0,"P":0} for team in SeasonYear["teams"]}
                    LoadAmount = len(SeasonYear["gamedays"])
                    Message = Messages[random.randint(0, len(Messages)-1)]
                    for amount, GameDays in enumerate(SeasonYear["gamedays"]):
                        GameDay = request(url+"/"+ViewYear+"/"+GameDays)
                        if GameDay != None:
                            for Games in GameDay["games"]:
                                scoreadder(YearDict, Games["score"]["home"], Games["score"]["away"])
                            os.system("cls")
                            print(Message.center(LoadAmount+8))
                            rainbow("["+"#"*amount+" "*(LoadAmount-amount)+"] "+str(int(amount/LoadAmount*100))+" %")
                        else:
                            break
                    if GameDay != None:
                        for teams in YearDict:
                            YearDict[teams]["GP"] = (YearDict[teams]["W"] + YearDict[teams]["D"] + YearDict[teams]["L"])
                            YearDict[teams]["GD"] = (YearDict[teams]["GF"] - YearDict[teams]["GA"])
                            YearDict[teams]["P"] = (YearDict[teams]["W"]*3 + YearDict[teams]["D"])
                        printtable(YearDict)
                    break
        else:
            rainbow("| There is no data for that year")

def printtable(table):
    while True:
        IndenteringTeam = max(map(len, table)) + 2
        os.system("cls")
        header = "| "+"Teams".center(IndenteringTeam)+"|"
        for Teams in table:
            for Headers in table[Teams]:
                header += Headers.center(4)+"|"
            break
        line("─",len(header)-2)
        rainbow(header)
        line("─",len(header)-2)
        for Team, Summary in table.items():
            head = "| " + Team + " " * (IndenteringTeam-len(Team)) +"|"
            for SpecificSummary in Summary:
                head += str(Summary[SpecificSummary]).center(4)+"|"
            rainbow(head)
        line("─",len(header)-2)
        try:
            Sortby = inputs("Sort by/exit: ")
            table = dict(sorted(table.items(), key = lambda x: x[1][Sortby.upper()],reverse=True))
        except:
            if Sortby == "exit":
                break
            inputs("Invalid argument")

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