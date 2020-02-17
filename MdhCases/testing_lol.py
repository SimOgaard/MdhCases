
# result = {
# 	"banana": {
# 		"confidence": 0.97
# 	},
# 	"cucumber": {
# 		"confidence": 0.36
# 	},
# 	"fruit": {
# 		"confidence": 0.99
# 	},
# 	"plantain": {
# 		"confidence": 0.72
# 	},
# 	"jackfruit": {
# 		"confidence": 0.31
# 	}
# }
# image="LOL"
# if result["banana"]["confidence"] >= 0.7:
#     print(image,"contains a banana ("+str(result["banana"]["confidence"]*100)+"% confidence)")


# countries = [
# 	"Russia",
# 	"Canada",
# 	"China",
# 	"United States",
# 	"Brazil"
# ]

# for amount, country in enumerate(countries,1):
#     print(amount,country)
# amount = 0
# while amount < len(countries):
#     amount+=1
#     print(amount,countries[amount-1])

# print("--- Karusellkollen 3.0 beta ---")

# höjd = int(input("Ange höjd > "))
# vuxens_sällskap = input("Vuxens sällskap? (J/N) > ")

# print("-------------------------------")

# if 130 <= höjd:
# 	print("Du får åka Lisebergbanan helt själv!")
# elif 110 <= höjd:
# 	if vuxens_sällskap == "J":
# 		print("Eftersom du har vuxens sällskap")
# 		print("får du åka Lisebergsbanan!")
# else:
# 	print("Du får inte åka Lisebergsbanan.")

# if höjd >= 130:
# 	print("Du får åka Lisebergbanan helt själv!")
# elif höjd >= 110 and vuxens_sällskap == "J":
# 	print("Eftersom du har vuxens sällskap")
# 	print("får du åka Lisebergsbanan!")
# else:
#     print("Du får inte åka Lisebergsbanan.")

# numbers = [
#     31,
#     5,
#     30,
#     16,
#     35,
#     42,
#     21,
#     2,
#     10,
#     40,
#     40,
#     27,
#     3,
#     11,
#     20,
#     8,
#     22,
#     33,
#     38,
#     1
# ]

# x=(float("inf")*-1)
# for number in numbers:
#     if number < max(numbers) and number > x:
#         x = number
# print(x)

# numbers.remove(max(numbers))
# print(max(numbers))



















# floats = [
#     68.32977367236687,
#     33.209328618985,
#     56.071557955086234,
#     22.890202977397244,
#     33.50205864899913,
#     16.779236699227283,
#     59.30313332594327,
#     74.44025372037025,
#     84.91449841004301,
#     62.99338889003317,
#     84.43965436408911,
#     24.58263331420486,
#     13.559620298939745,
#     5.16956950629136,
#     80.96885147250413,
#     0.8268981866415781,
#     12.060427756654068,
#     2.2396726313399395,
#     60.67206100488456,
#     21.732106473742064
# ]

# closest = float("inf")
# for num in floats:
#     if abs(50-num) < abs(50-closest):
#         closest = num
# print(closest)


# nums=[]
# while 0 not in nums:
#     nums.append(int(input("> ")))
# print(sum(nums)/(len(nums)-1))



# x=0
# while True:
#     y = int(input("> "))
#     x += y
#     if y == 0:
#         print(x)
#         break


# x=[]
# while 0 not in x:
#     x.append(int(input("> ")))
# print(max(x))    



# import random
# computernumber = random.randint(0, 99)
# guessamount = 0
# while True:
#     yournumber = int(input("> "))
#     guessamount += 1
#     if yournumber < computernumber:
#         print("Higher")
#     elif yournumber > computernumber:
#         print("Lower")
#     else:
#         print(str(yournumber)+" is correct")
#         print("it took you "+str(guessamount)+" guesses")
#         break

# mathkonstants = {
#     "e": 2.718,
#     "i": "sqrt(-1)",
#     "pi": 3.142
# }

# while True:
#     mathchoise = input("> ")
#     if mathchoise in mathkonstants:
#         print(mathkonstants[mathchoise])
#         continue
#     elif mathchoise == "exit":
#         break
#     print("choice none existant")

# def has_two_even_elements(numlist):
#     evenamount = 0
#     for nums in numlist:
#         if nums % 2 == 0:
#             evenamount += 1
#     if evenamount == 2:
#         return True
#     return False

# b = has_two_even_elements([2, 6, 5, 4, 3, 7, 9, 8])
# print(b)
# # False

# b = has_two_even_elements([5, 2, 3, 8, 7, 5])
# print(b)
# # True

# b = has_two_even_elements([1, 7, 4, 5, 3, 7, 9])
# print(b)
# # False

# def largest(*li):
#     return max(li)

# l = largest(5, 2, 8, 3, 9, 2, 6)
# print(l)
# # 9

# l = largest(5, 2, 7, 4)
# print(l)
# # 7

# l = largest(6, 4, 2, 3, 1)
# print(l)
# # 6
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
#     translated = []
#     scentence = scentence.lower().split(" ")
#     for word in scentence:
#         translated.append(words[word])
#     return " ".join(translated)
# t = translate("Jag gillar mat")
# print(t)
# # I like food

# t = translate("Det är roligt att spela TV-spel")
# print(t)
# # it is fun to play videogames

# import json
# print(sum(json.loads(open('todos.json').read())["integers"]))


# def increment(nums):
#     return [x+1 for x in nums]
# nums = [2, 3, 5, 7, 11]
# new_list = increment(nums)
# print(new_list)
# # [3, 4, 6, 8, 12]

# MyDog = {
# 	"name": "Morris",
# 	"breed": "German Shepherd",
# 	"children": [
# 		{
# 			"name": "Doglas",
# 			"breed": "German Shepherd",
# 			"children": []
# 		},
# 		{
# 			"name": "Vofflas",
# 			"breed": "German Shepherd",
# 			"children": []
# 		}
# 	]
# }

# MyDog["name"]
# MyDog["children"][1]["breed"]

# def itterate(ITER):
#     for key, value in ITER.items():
#         if type(value) is list:
#             for items in value:
#                 itterate(items)
#         else:
#             print(key+": "+value)

# itterate(MyDog)



# import json
# brands = ["Toyota", "Volkswagen", "Kia", "Koenigsegg"]
# print(brands)
# brands.pop(-1)
# print(brands)
# brands.append("Ford")
# print(brands)
# brands.insert(3,"General Motors")
# print(brands)
# brands = json.dumps(brands)
# print(brands)


# first_name = ["Lisa", "Gunilla", "Olle"]
# last_name = ["Svensson", "Ångström", "Nygren"]

# full_name = list(first_name)

# full_name[0] += " " + last_name[0]
# full_name[1] += " " + last_name[1]
# full_name[2] += " " + last_name[2]

# print("first_name =", first_name)

# print("last_name =", last_name)

# print("full_name =", full_name)



# president = {
# 	"name": {
# 		"first": "George",
# 		"middle": "Walker",
# 		"last": "Bush"
# 	},
# 	"born": {
# 		"year": 1946,
# 		"month": "July",
# 		"day": 6
# 	},
# 	"parents": [
# 		"George H. W. Bush",
# 		"Barbara Pierce"
# 	],
# 	"children": ["Barbara"]
# }

# print(president["born"]["month"])
# president["children"].append("Jenna")
# print(president)

# print("president",president["name"]["first"],president["name"]["middle"],president["name"]["last"])
# print("Born:",president["born"]["month"],str(president["born"]["day"])+",",str(president["born"]["year"]))
# print("Parents:")
# print(president["parents"][0])
# print(president["parents"][1])
# print("Children:")
# print(president["children"][0])
# print(president["children"][1])


# import json 
# todos = [
# 	"Köpa mat.",
# 	"Gå ut med hunden",
# 	"Plugga"
# ]

# todos = json.dumps(todos)

# with open("todos.json", "w") as f:
# 	f.write(todos)

# message1 = "Please do not hack my computer.\n"
# message2 = "My antivirus is out of date."

# with open("MOTD.txt") as f:
# 	f.write(message1)
# 	f.write(message2)

# print("SUCCESS: Important message written to file.")


# import json
# with open("todos.json") as f:
#     profile = f.read()
# profile = json.loads(profile)
# print(profile["username"])


# number = 0
# with open("C:/Users/User/Desktop/Ny mapp/users.txt") as f:
#     for line in f.readlines():
#         number += 1
#         print("Användare " + str(number) + " - " + line, end= "")
     
# import json
# with open("C:/Users/User/Desktop/Ny mapp/numbers.json") as f:
#     f = json.loads(f)
#     summ = 0
#     for x in f["integers"]:
#         summ += int(x)
#     print(summ)



def increment(li):
    return [x+1 for x in li]
    
nums = [2,3,4,5,6]
new_nums = increment(nums)
print(new_nums)

# def increments(li):
#     lis=[]
#     i=0
#     while i < len(li):
#         lis.append(li[i]+1)
#         i+=1
#     return lis
# new_nums = increments(nums)
# print(new_nums)


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

# def translate(string):
#     worden = string.split(" ")
#     for word in worden:
#         print(words[word.lower()])
#     return words[word]
        

# t = translate("Jag gillar mat")
# print(t)
# # I like food

# t = translate("Det är roligt att spela TV-spel")
# print(t)
# # it is fun to play videogames



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
#     return False
    
# print(get_country("Paris"))


# def largest(*larg):
#     return max(larg)

# l = largest(5, 2, 8, 3, 9, 2, 6)
# print(l)
# # 9

# l = largest(5, 2, 7, 4)
# print(l)
# # 7

# l = largest(6, 4, 2, 3, 1)
# print(l)
# # 6





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

# def translates(string):
#     string.lower().split(" ")

# def translate(string):
#     scentence=""
#     wordss = string.lower().split(" ")
#     for word in wordss:
#         for key in words:
#             if word == key:
#                 scentence+=words[word]+" "
#     return scentence
# t = translate("Jag gillar mat")

# print(t)
# # I like food

# t = translate("det är roligt att spela tv-spel")
# print(t)
# # it is fun to play videogames



# def has_two_even_elements(arr):
#     i=0
#     for num in arr:
#         if num % 2 == 0:
#             print(num)
#             i+=1
#     if i == 2:
#         return True
#     return False
    
# b = has_two_even_elements([2, 6, 5, 4, 3, 7, 9, 8])
# print(b)
# # False

# b = has_two_even_elements([5, 2, 3, 8, 7, 5])
# print(b)
# # True

# b = has_two_even_elements([1, 7, 4, 5, 3, 7, 9])
# print(b)
# # False

# maths = {"e":2.718, "pi":3.142}

# while True:
#     choice=input("choice: ")
#     for math in maths:
#         if choice == math:
#             print(maths[math])
#             break
#     else:
#         if choice == "exit":
#             break
#         print("invalid arg")




# from random import randint

# computerchoice = randint(0,99)

# while True:
#     choice = input("Guess: ")
#     if int(choice) == computerchoice:
#         print(choice,"is correct")
#         break
#     elif int(choice) < computerchoice:
#         print("higher")
#     else:
#         print("lower")

             
# summa =0
# while True:
#     choice = input("Guess: ")
#     if int(choice) != 0:
#         summa += int(choice)
#     else:
#         print(summa)
#         break

# summa = []
# while True:
#     choice = input("Guess: ")
#     if int(choice) != 0:
#         summa.append(int(choice))
#     else:
#         print(max(summa))
#         break


# summa =0
# i=0
# while True:
#     choice = input("Guess: ")
#     if int(choice) != 0:
#         summa += int(choice)
#         i+=1
#     else:
#         print(summa/i)
#         break

    
     

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
#     if user["age"] >= 50:
#         print(user["name"])



# participants = [
# 	{
# 		"forename": "Anna",
# 		"surname": "Andersson",
# 		"age": 52
# 	},
# 	{
# 		"forename": "Lars",
# 		"surname": "Johansson",
# 		"age": 41
# 	},
# 	{
# 		"forename": "Eva",
# 		"surname": "Karlsson",
# 		"age": 32
# 	},
# 	{
# 		"forename": "Mikael",
# 		"surname": "Nilsson",
# 		"age": 32
# 	},
# 	{
# 		"forename": "Maria",
# 		"surname": "Johansson",
# 		"age": 55
# 	},
# 	{
# 		"forename": "Anders",
# 		"surname": "Karlsson",
# 		"age": 60
# 	},
# 	{
# 		"forename": "Karin",
# 		"surname": "Johansson",
# 		"age": 47
# 	},
# ]
# ages=0
# Johansson=0
# for person in participants:
#     ages += person["age"]
#     if person["surname"]=="Johansson":
#         Johansson+=1
# print(ages/len(participants))
# print(Johansson/len(participants))




# floats = [
#     68.32977367236687,
#     33.209328618985,
#     56.071557955086234,
#     22.890202977397244,
#     33.50205864899913,
#     16.779236699227283,
#     59.30313332594327,
#     74.44025372037025,
#     84.91449841004301,
#     62.99338889003317,
#     84.43965436408911,
#     24.58263331420486,
#     13.559620298939745,
#     5.16956950629136,
#     80.96885147250413,
#     0.8268981866415781,
#     12.060427756654068,
#     2.2396726313399395,
#     60.67206100488456,
#     21.732106473742064
# ]
# floats = sorted(floats)
# diff=[]
# for fl in floats:
#     if fl >= 50:
#         diff.append(fl-50)
#     else:
#         diff.append(50-fl)
# print(diff)



# numbers = [
#     31,
#     5,
#     30,
#     16,
#     35,
#     42,
#     21,
#     2,
#     10,
#     40,
#     40,
#     27,
#     3,
#     11,
#     20,
#     8,
#     22,
#     33,
#     38,
#     1
# ]

# naststörst=0
# for number in numbers:
#     if number > störst and number != max(numbers):
#         naststörst=number
# print(naststörst)


# def no_equal_elements(list1, list2):
#     for num in list1:
#         if num in list2:
#             return False
#     return True

# print(no_equal_elements([1, 2, 3], [4, 5]))
# # True

# print(no_equal_elements([1, 3], [2, 4]))
# # True

# print(no_equal_elements([1, 2, 3], [3, 4, 5]))
# # False

# print(no_equal_elements([2], [4, 5, 2]))
# # False



# swede		= input("Bor du i sverige? (J/N) > ")
# grant		= input("Har du aktivitetsersättning eller sjukersättning? (J/N) > ")
# low_salary	= input("Har du en låg inkomst? (J/N) > ")
# house_costs	= input("Har du kostnader för bostaden? (J/N) > ")
# age			= int(input("Vad är din ålder? > "))
# if swede == "J" and grant == "J" and low_salary == "J" and house_costs == "J":
#     print("Du är berättigad bostadstillägg!")
#     if age < 65:
#     	print("Skicka din ansökan till Försäkringskassan.")
#     else:
#     	print("Skicka din ansökan till Pensionsmyndigheten.")
# else:
# 	print("Du är inte berättigad bostadstillägg.")


# import random

# while True:  
#     x = random.randint(0, 9)
#     y = random.randint(0, 9)
#     z = random.randint(0, 9)

#     print("-------------")
#     print("|", x, "|", y, "|",  z, "|")
#     print("-------------")

#     if x == y == z == 0:
#         print("Jackpot!")
#         break
#     elif x==y==z:
#         print("Three in a row!")
#         break
#     elif x==y-1==z-2:
#         print("Ladder!")
#         break
#     elif z==y-1==x-2:
#         print("Reverse ladder!")
#         break
#     else: 
#         print("Try again!")


# import random

# while True:
#     x = random.randint(0, 1)
#     y = random.randint(0, 1)
#     z = random.randint(0, 1)
#     if x == y:
#         if y == z:
#             print("Alpha")
#         else:
#             print("Omega")
#     elif x == z:
#         if z < y:
#             print("Beta")
#         else:
#             print("Omega")
#     else:
#         print("Omega")

#     if x == y == z:
#         print("Alpha")
#     elif x==z and z<y:
#         print("Beta")
#     else:
#         print("Omega")
#     input("")




# print("--- Karusellkollen 3.0 beta ---")

# höjd = int(input("Ange höjd > "))
# vuxens_sällskap = input("Vuxens sällskap? (J/N) > ")

# print("-------------------------------")

# if höjd >= 130:
# 	print("Du får åka Lisebergbanan helt själv!")
# elif vuxens_sällskap == "J" and höjd >= 110:
#     print("Eftersom du har vuxens sällskap")
#     print("får du åka Lisebergsbanan!")
# else:
# 	print("Du får inte åka Lisebergsbanan.")



# users = [
# 	"Anna",
# 	"Lars",
# 	"Eva",
# 	"Mikael",
# 	"Maria",
# 	"Anders"
# ]

# index = 0

# while index <= len(users)-1:
# 	print(users[index], "-", users[index + 1])
# 	index += 2




# import random
# x=1
# while x!=0:
#     x = random.randint(0,9)
#     print(x)



# while True:
#     continue
#     print("l")

# countries = [
# 	"Russia",
# 	"Canada",
# 	"China",
# 	"United States",
# 	"Brazil"
# ]
# nr=1
# for country in countries:
#     print(str(nr)+country)
#     nr+=1

# nr=1
# while nr <= len(countries):
#     print(str(nr)+countries[nr-1])
#     nr+=1


# def is_even(integer):
# 	if integer % 2 == 0:
# 		return True
# 	else:
# 		return False

# numbers = [8, 4, 6, 2, 9, 3, 5, 7, 1]
# odd = []
# even = []

# while len(numbers):
# 	if is_even(numbers[0]):
# 		even.append(numbers[0])
# 	else:
# 		odd.append(numbers[0])
# 	del numbers[0]

# print(numbers)
# print(odd)
# print(even)


# fråga 36                                            123



# server = {
# 	"ip": "192.168.0.5",
# 	"mask": "255.255.255.0",
# 	"hostname": "MinecraftServer",
# 	"os": "Debian 10"
# }

# # for keys in server:
# if server["os"]=="server":
#     print("known")
# else:
#     print("unkbown")

# favoritfrukter = [
# 	"banan",
# 	"vattenmelon",
# 	"äpple",
# 	"grapefrukt"
# ]

# if "banan" in favoritfrukter:
#     print("Banan är min favoritfrukt också!")
# else:
#     print("Min favoritfrukt är banan!")


# v1 = {
# 	"x": 5,
# 	"y": 3
#     "z"
# }

# for keys in v1:
#     if keys=="z":
#         print("Vektorn v1 är en tredimensionell vektor.")
#         break
# else:
#     print("Vektorn v1 är en tvådimensionell vektor.")



# a = 3
# b = 5

# if a < b and b - 3 < a:
# 	if a == b - 1:
# 		print(b + 1)
# 	else:
# 		print(b - 1)
# else:
# 	print(a)



# ListA = [1, 2, 3]
# ListB = ['A', 'B', 'C']

# for a in ListA:
# 	for b in ListB:
# 		print(str(a) + b)



# fancy_numbers = {
#     "even": [0, 2, 4, 6, 8],
#     "odd": [1, 3, 5, 7, 9],
#     "prime": [2, 3, 5, 7]
# }

# min_length = float("inf")
# match = None

# for key in fancy_numbers:
#     if len(fancy_numbers[key]) < min_length:
#         min_length = len(fancy_numbers[key])
#         match = key

# for number in fancy_numbers[match]:
#     print(number)

# float("inf")


# for x in range(10):
#     if x % 2 == 0:
#         print(x)


# a = 0


# while a < 5:
#     a += 1
#     print(a)
# else:
#     print(a)
