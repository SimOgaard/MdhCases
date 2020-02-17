# MyDog = {
# 	"name": "Morris",
# 	"breed": "German 2",
# 	"children": [
# 		{
# 			"name": "123",
# 			"breed": "2 1",
# 			"children": [		{
# 			"name": "Doglas",
# 			"breed": "German 6",
# 			"children": []
# 		},
# 		{
# 			"name": "Vofflas",
# 			"breed": "German 2",
# 			"children": [		{
# 			"name": "Doglas",
# 			"breed": "German 3",
# 			"children": []
# 		},
# 		{
# 			"name": "123",
# 			"breed": "German 1",
# 			"children": []
# 		}]
# 		}]
# 		},
# 		{
# 			"name": "2",
# 			"breed": "German Shepherd",
# 			"children": [		{
# 			"name": "Doglas",
# 			"breed": "German Shepherd",
# 			"children": []
# 		},
# 		{
# 			"name": "612",
# 			"breed": "German Shepherd",
# 			"children": []
# 		}]
# 		}
# 	]
# }

# print(MyDog["name"])
# print(MyDog["children"][1]["breed"])

# def ITER(obj):
#     for key, value in obj.items():
#         if type(value) is list:
#             for objects in value:
#                 ITER(objects)
#         else:
#             print(key+": "+value)

# ITER(MyDog)

# # Världens största bilproducenter.
# brands = ["Toyota", "Volkswagen", "Kia", "Koenigsegg"]
# print(brands)
# del brands[-1]
# print(brands)
# brands.append("Ford")
# print(brands)
# brands.insert(3,"General Motors")
# print(brands)
# import json
# print(json.dumps(brands))

# import json

# todos = [
# 	"Köpa mat.",
# 	"Gå ut med hunden",
# 	"Plugga"
# ]

# with open("todos.json", "w") as f:
# 	f.write(json.dumps(todos))

# message1 = "Please do not hack my computer.\n"
# message2 = "My antivirus is out of date."

# with open("MOTD.txt", "w") as f:
# 	f.write(message1)
# 	f.write(message2)

# print("SUCCESS: Important message written to file.")
# import json

# with open("profile.json") as f:
#     profile = json.loads(f.read())

# print(profile["username"])
import json
with open("profile.json") as f:
    print(sum(json.loads(f.read())["integers"]))