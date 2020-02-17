# def increment(li):
#     return [x+1 for x in li]
# nums = [2,3,4,5,6]
# print(increment(nums))

# import random

# print('''
# ****************
# * HIGHER LOWER *
# ****************
# Guess a number
# between 0 and 99
# ----------------
# ''')

# choice = 100
# botnum = random.randint(0,99)
# amount = 0

# while choice != botnum:
#     choice = int(input("> "))
#     if choice < botnum:
#         print("HIGHER")
#     elif choice > botnum:
#         print("LOWER")
#     amount+=1
# print("congrats it took you", amount, "tries")

# val = 1
# störst = float("-inf")
# while True:
#     val = int(input("> "))
#     if val == 0:
#         break
#     elif val > störst:
#         störst = val    
# print(störst)

# medel = 0
# amount = 0
# while True:
#     val = int(input("> "))
#     if val != 0:
#         medel+=val
#         amount+=1
#     else:
#         break
# print(medel/amount)

# words = {
#     "att": "to",
#     "det": "it",
#     "gillar": "like",
#     "jag": "I",
#     "mat": "food",
#     "spela": "play",
#     "tv-spel": "videogames",
#     "roligt": "fun",
#     "är": "is"
# }

# def translate(scentence):
#     return " ".join([words[x] for x in scentence.lower().split(" ")])

# t = translate("Jag gillar mat")
# print(t)
# # I like food

# t = translate("Det är roligt att spela TV-spel")
# print(t)
# # it is fun to play videogames

# print('''.: SuperSum v2.1.0 :.
# ---------------------''')

# val = 1
# summa = 0
# while val != 0:
#     val = int(input("> "))
#     summa += val

# print('''---------------------
# Summan av de inmatade
# heltalen är '''+str(summa))


# countries = {
# 	"Sweden": ["Stockholm", "Göteborg", "Malmö"],
# 	"Norway": ["Oslo", "Bergen", "Trondheim"],
# 	"England": ["London", "Birmingham", "Manchester"],
# 	"Germany": ["Berlin", "Hamburg", "Munich"],
# 	"France": ["Paris", "Marseille", "Toulouse"]
# }

# def get_country(city):
#     for country, cities in countries.items():
#         if city in cities:
#             return country
#     else:
#         return False

# print(get_country("Paris"))

# message1 = "Please do not hack my computer.\n"
# message2 = "My antivirus is out of date."

# with open("MOTD.txt", "w") as f:
# 	f.write(message1)
# 	f.write(message2)

# print("SUCCESS: Important message written to file.")



# users = [
# 	{
# 		"name": "Amanda",
# 		"age": 49
# 	},
# 	{
# 		"name": "Gunnar",
# 		"age": 51
# 	},
# 	{
# 		"name": "Lena",
# 		"age": 50
# 	},
# 	{
# 		"name": "Frida",
# 		"age": 52
# 	},
# 	{
# 		"name": "Lotta",
# 		"age": 49
# 	},
# 	{
# 		"name": "Clas",
# 		"age": 51
# 	}
# ]

# for user in users:
#     if user["age"]>=50:
#         print(user["name"])

# users = [
# 	"Anna",
# 	"Lars",
# 	"Eva",
# 	"Mikael",
# 	"Maria",
# 	"Anders"
# ]

# index = 0

# while index < len(users):
# 	print(users[index], "-", users[index + 1])
# 	index += 2

# import random

# x = random.randint(0, 9)
# y = random.randint(0, 9)
# z = random.randint(0, 9)

# print("-------------")
# print("|", x, "|", y, "|",  z, "|")
# print("-------------")

# if 0==x==y==z:
#     print("JACKPOT")
# elif x==y==z:
#     print("THREE IN A ROW")
# elif x==y-1==z-2:
#     print("LADDER")
# elif x==y+1==z+2:
#     print("REVERSE LADDER")
# else:
#     print("Try again!")
