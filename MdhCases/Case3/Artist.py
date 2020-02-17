import os
import requests 
import json
lenght = 30
menu = ["| L | List DataBase", "| V | View Artist Profile", "| E | Exit The Script"]
url = "https://5hyqtreww2.execute-api.eu-north-1.amazonaws.com/artists/"
Show = True

def data(info):
    res = requests.get(url+info)
    resp = res.json()
    return resp

def line(tecken):
    print(tecken *lenght)
def header(string):
    center = string.center(lenght)
    print(center)

def ui():
    line("─")
    header("Artist DataBase")
    line("─")
    for x in menu:
        print(x)
    line("─")
def form(string):
    new = string.strip()
    new.lower()
    new2 =new.replace(" ", "")
    return new2

def methods(method):
    os.system('cls')
    if method == "l":
        info = data("")   
        num = 0
        line("─")
        for x in info["artists"]:      
            header(info["artists"][num]["name"])
            num+=1
        line("─")
        input("Continue?")
    elif method == "v":
        artist = input("Välj artist profil: ")
        info = data("") 
        num = 0
        for x in info["artists"]:
            Information= info["artists"][num]["name"].replace(" ", "")
            artistNew=form(artist)
            
            if  Information.lower() == artistNew:
                profile = info["artists"][num]["id"]
                info1 = data(profile)
               
            num +=1

        try:
            isss = info1["artist"]["name"]
            iss = info1["artist"]["genres"]
            iss2 = info1["artist"]["years_active"]
            iss3 = info1["artist"]["members"]
            line("─")
            header(str(isss))
            print("Genres: ",str(iss).replace("'", " "))
            print("Years of activity: ", str(iss2).replace("'", " "))
            print("Members: ",str(iss3).replace("'", " ") )
            line("─")
            input()
        except: 
            
            print("Error, the input given does not match any from out database")
            input()
    elif method == "e":
        exit()
        os.system('cls')

while Show == True:
    os.system('cls')
    ui()
    i = input("")
    l = form(i)
    methods(str(l))