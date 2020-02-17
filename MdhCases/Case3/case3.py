import os
import requests

length = 30
url = "https://5hyqtreww2.execute-api.eu-north-1.amazonaws.com/artists/"
response_dictionary = requests.get(url).json()

def header(head):
    print("|"+head.center(length-2)+"|")

def line(typ):
    print(typ*length)

while True:
    os.system("cls")
    line("*")
    header("artists")
    line("-")
    for x in ["view artist profile", "exit application"]:
        print("| "+x[:1] + " | " + x)
    line("-")
    selection = input("| Selection > ").lower()
    line("-")
    if selection == "v":
        for artist in response_dictionary["artists"]:
            print("| "+artist["name"])
        line("-")
        artisten = input("| Artist name > ")
        line("-")
        for artister in response_dictionary["artists"]:
            if artister["name"] == artisten.lower().title():
                response_dictionary2 = requests.get(url+artister["id"]).json()
                for heads in response_dictionary2["artist"]:
                    if heads == "name":
                        break
                    infoline = ""
                    for info in response_dictionary2["artist"][heads]:
                        infoline += (info+", ")
                    print(("| "+heads+": "+infoline)[:-2])
                break
        else:
            print("| ERROR: Invalid expression '" + artisten + "' does not exist")
    elif selection == "e":
        break
    else:
        print("| ERROR: Invalid expression '" + selection + "' is not an option")
    line("-")
    input("| Continue?")