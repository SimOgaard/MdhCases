# lol=0
# import json
# for x in json.loads(open('lol.json').read())["integers"]:
# 	lol+=x
# print(lol)

# message1 = "Please do not hack my computer.\n"
# message2 = "My antivirus is out of date."

# with open("MOTD.txt", "w") as f:
# 	f.write(message1)
# 	f.write(message2)

# print("SUCCESS: Important message written to file.")

floats = [
    68.32977367236687,
    33.209328618985,
    56.071557955086234,
    22.890202977397244,
    33.50205864899913,
    16.779236699227283,
    59.30313332594327,
    74.44025372037025,
    84.91449841004301,
    62.99338889003317,
    84.43965436408911,
    24.58263331420486,
    13.559620298939745,
    5.16956950629136,
    80.96885147250413,
    0.8268981866415781,
    12.060427756654068,
    2.2396726313399395,
    60.67206100488456,
    21.732106473742064
]
lol = float("inf")
for x in floats:
	if abs(x-50)<lol:
		
	print(abs(x-50))
