import requests
import os
connection=False
baseUrl="http://football-frenzy.s3-website.eu-north-1.amazonaws.com/api"
length=70
teams={}
options=["| list | List available seasons", "| view | View table for season"]
def line(char):
    print(char*length)

def center(text):
    print(text.center(length))

def Get(url):
    try:
        r=requests.get(url)
        got_dict = r.json()
        connection=True
        return got_dict, connection
    except requests.exceptions.ConnectionError:
        connection=False
        print("Could not connect to api! Check your connection and try again")
        return {}, connection



def elongate(word, length):
    while len(word)<length:
        word+=" "
    return word


def menu():
    line("*")
    center("FOOTBALL FRENZY")
    center("STAT VIEWER")
    line("-")
    for option in options:
        print(option)
    line("-")

def showYears():
    api,connection=Get(baseUrl)
    if connection==True:
        loop=0
        print("| ", end="")
        for years in api["seasons"]:
            if loop<3:
                print(years+ " ", end="")
                loop+=1
            else:
                print(years+ " \n| ", end="")
                loop=0
        print("")
        line("-")
            

def showStats():
    api,connection=Get(baseUrl)
    if connection==True:
        year=input("| Select a year: ")
        line("*")
        if year in api["seasons"]:
            yearDict,connection=Get(baseUrl + "/" + year)
            if connection==True:
                for team in yearDict["teams"]:
                    if team not in teams:
                        teams[team]={

                            "W": 0,
                            "L": 0,
                            "D": 0,
                            "GF": 0,
                            "GA": 0

                        }
            for gameday in yearDict["gamedays"]:
                dateDict,connection=Get(baseUrl+"/"+year+ "/" + gameday)
                if connection==True:
                    for game in dateDict["games"]:
                        if game["score"]["home"]["goals"]>game["score"]["away"]["goals"]:
                            teams[game["score"]["home"]["team"]]["W"]+=1
                            teams[game["score"]["away"]["team"]]["L"]+=1
                        elif game["score"]["home"]["goals"]<game["score"]["away"]["goals"]:
                            teams[game["score"]["away"]["team"]]["W"]+=1
                            teams[game["score"]["home"]["team"]]["L"]+=1
                        else:
                            teams[game["score"]["away"]["team"]]["D"]+=1
                            teams[game["score"]["home"]["team"]]["D"]+=1
                        teams[game["score"]["away"]["team"]]["GF"]+=game["score"]["away"]["goals"]
                        teams[game["score"]["away"]["team"]]["GA"]+=game["score"]["home"]["goals"]
                        teams[game["score"]["home"]["team"]]["GF"]+=game["score"]["home"]["goals"]
                        teams[game["score"]["home"]["team"]]["GA"]+=game["score"]["away"]["goals"]
                    scorelen=6
            longestTeam=len(max(teams, key=len))+1
            results=["W", "D", "L", "GF", "GA","GD","P"]
            print("| "+elongate("Team", longestTeam)+":   ", end="")
            for result in results:
                print(elongate(result, scorelen), end="")
            print("")
            print("| "+"-"*longestTeam+":   "+ 7*(elongate("---", scorelen)))
            for team in teams:
                print("| "+elongate(team,longestTeam)+ ": ", end ="")
                print("  ", end="")
                for score in teams[team]:
                    print(elongate(str(teams[team][score]),scorelen), end="")
                print(elongate(str(teams[team]["GF"]-teams[team]["GA"]),scorelen)+str(teams[team]["W"]*3+teams[team]["D"]))
            
        else:
            print("There is not data for that year:")



while True:
    os.system("cls")
    menu()
    selection=input("| Selection: ")
    line("*")
    if selection=="list":
        showYears()
    elif selection=="view":
        showYears()
        showStats()
        line("*")
    else:
        print("Invalid choice!")
    input("Press enter to continue...")