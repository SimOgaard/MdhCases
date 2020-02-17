import os
import pandas as pd
import numpy as np

lila = '\033[95m'
gul = '\033[93m'
röd = '\033[91m'

def header(head):
    print(lila+head.center(60))

def line(typ):
    print(lila+typ*60)

import requests
url = "http://football-frenzy.s3-website.eu-north-1.amazonaws.com/api"
if not os.path.exists("csv"): os.makedirs("csv")
seasonyears = requests.get(url).json()["seasons"]
while True:
    df = pd.DataFrame(columns=["Team", "W", "D", "L", "P"])
    tal = 10
    years=""
    os.system("cls")
    line("*")
    header("Football")
    line("-")
    for x in ["list available seasons", "view table for season"]: print(gul+x[:4]+" | "+x)
    line("-")
    selection = input(gul+"Selection > ").lower()
    line("-")
    if selection == "list":
        for year in seasonyears:
            if tal > 0:
                years += year+", "
                tal -= 1
            else:
                print(gul+"| "+ years)
                years = ""
                years += year+", "
                tal = 9
        if not tal == 9: print(gul+"| "+ years)
        line("-")
    elif selection == "view":
        viewyear = input(gul+"Year > ")
        line("*")
        if os.path.exists("csv/"+viewyear+".csv"): print(pd.read_csv(("csv/"+viewyear+".csv"), parse_dates=True, index_col=0).to_string(index=False))
        else:
            for year in seasonyears:
                if year == viewyear:
                    response_dictionary = requests.get(url+"/"+viewyear).json()
                    df["Team"] = response_dictionary["teams"]
                    df = df.replace(np.nan, 0)
                    procents = loadamount = len(response_dictionary["gamedays"])
                    loadstart = 0
                    for gamedays in response_dictionary["gamedays"]:
                        gameday = requests.get(url+"/"+viewyear+"/"+gamedays).json()
                        os.system("cls")
                        loadamount-=1
                        procent = (loadstart+1)/procents
                        print("Progress: ["+"#"*loadstart+"-"*loadamount+"] "+str(int(procent*100))+" %")
                        loadstart+=1
                        for games in gameday["games"]:
                            turf = "home"
                            turfs = "away"
                            tal = 10
                            if games["score"]["home"]["goals"] == games["score"]["away"]["goals"]: df.loc[df["Team"].str.contains(games["score"]["home"]["team"]+"|"+games["score"]["away"]["team"]), 'D'] += 1
                            while tal > 8:
                                tal -= 1
                                df.loc[df["Team"].str.contains(games["score"][turf]["team"]), 'P'] += games["score"][turf]["goals"]
                                if games["score"][turf]["goals"] > games["score"][turfs]["goals"]: df.loc[df["Team"].str.contains(games["score"][turf]["team"]), 'W'] += 1
                                if games["score"][turf]["goals"] < games["score"][turfs]["goals"]: df.loc[df["Team"].str.contains(games["score"][turf]["team"]), 'L'] += 1
                                turf = "away"
                                turfs = "home"
                    df = df.iloc[df['P'].argsort()][::-1]
                    df.to_csv("csv/"+viewyear+".csv")
            if df.empty: print(röd + "ERROR: Invalid expression '" + viewyear + "' does not exist")
            else:
                print("")
                print(df.to_string(index=False))
    else: print(röd + "ERROR: Invalid expression '" + selection + "' is not an option")
    input(gul+"Continue?")