import requests as r
import os

length=40
options=["| L | List artists", "| V | View artist profile", "| E | Exit application"]
rainbowColors=['\033[31m','\033[38;2;243;134;48m','\033[33m','\033[32m','\033[34m','\033[35m', "\033[0m"]

def rainbow(string):
    printint=0
    for char in string:
        if printint >= 6:
            printint = 0
        if char =="|" or char == "+" or char == "─":
            print(rainbowColors[printint]+char, end="")
        else:
            print(rainbowColors[6]+char, end="")
        printint += 1
    print(rainbowColors[6])

def form(string):
    return input(rainbowColors[0]+"| "+rainbowColors[6]+string).replace(" ", "").lower()

def line(char):
    rainbow("+"+char*length+"+")

def center(text):
    rainbow("|"+text.center(length)+"|")

def menu():
    line("─")
    center("Artist Database")
    line("─")
    for option in options:
        rainbow(option)
    line("─")

def printArtists():
    line("─")
    for artist in artistsDict()["artists"]:
        center(artist["name"])
    line("─")

def artistsDict():
    json_dict=r.get("https://5hyqtreww2.execute-api.eu-north-1.amazonaws.com/artists/")
    artists_dict=json_dict.json()
    return artists_dict

def printDetails(name):
    for artist in artistsDict()["artists"]:
        if artist["name"].replace(" ", "").lower()==name:
            json_dict=r.get("https://5hyqtreww2.execute-api.eu-north-1.amazonaws.com/artists/"+ artist["id"])
            details_dict=json_dict.json()
            line("─")
            center(artist["name"])
            line("─")
            rainbow ("| Members: " + ', '.join(details_dict["artist"]["members"]))
            rainbow ("| Genres: " + ', '.join(details_dict["artist"]["genres"]))
            rainbow("| Years active: " + details_dict["artist"]["years_active"][0])
            line("─")
            break
    else:
        rainbow("| No such artist exists")

while True:
    os.system("cls")
    menu()
    selection = form("What do you want to do?: ")
    if selection== "l":
        printArtists()
    elif selection == "v":
        printArtists()
        printDetails(form("Which artist do you want to select?: "))
    elif selection=="e":
        break
    else:
        rainbow("| Invalid option")
    form("Press enter to continue...")