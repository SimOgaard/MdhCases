school_class = {
	"school": "Malmö skola 7-9",
	"class_name": "9D",
	"students": [
		{
			"forename": "Mikael",
			"surname": "Eriksson",
			"age": 16,
			"female": False
		},
		{
			"forename": "Mikael",
			"surname": "Eriksson",
			"age": 16,
			"female": False
		},
		{
			"forename": "Maria",
			"surname": "Persson",
			"age": 16,
			"female": True
		},
		{
			"forename": "Lucas",
			"surname": "Olsson",
			"age": 15,
			"female": False
		},
		{
			"forename": "Kristina",
			"surname": "Larsson",
			"age": 16,
			"female": True
		}
	]
}

xs=[]
x=0
for students in school_class["students"]:
    if students["age"]!=15 or students["female"]==False:
        xs.append(x)
    x+=1
print(xs)
for y in xs:
    print(y)
    del school_class["students"][int(y)]


################
# VERIFIKATION #
#   (RÖR EJ)   #
################
try:
  col_size = max([max([len(student["forename"]), len(student["surname"])]) for student in school_class["students"]])
except ValueError:
  col_size = 8
print((2 * col_size + 7 ) * "-")
print("|", ("Flickor 15 år | " + school_class["class_name"]).center(2 * col_size + 3), "|")
print((2 * col_size + 7 ) * "-")
for student in school_class["students"]:
  print("|", student["forename"].center(col_size), "|", student["surname"].center(col_size), "|")
print((2 * col_size + 7 ) * "-")
################