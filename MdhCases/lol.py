#lol = {"S":"{'RPM':0.000000','Integration':'0.00','Proportionell':'10.00','Easing':'0.00','Derivering':'0.00','DistanceDriven':'0.00','Pw':'100.00'}}"}
lol = '{"O":["119.863014","0.41","0.00","0.36","0.00","874.34","305.00"]}'
import json
i = json.loads(lol)
print(i["O"])