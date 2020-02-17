import os
import operator

lila = '\033[95m'
gul = '\033[93m'
röd = '\033[91m'

math=["+", "-", "*", "/"]
op=[operator.add, operator.sub, operator.mul, operator.truediv]
lista=[]
integers=[]
methonds=[]

def header(head):
    print(lila+head.center(30))

def line(typ):
    print(lila+typ*30)

selection = input(gul+"Selection > ")
for char in selection:
    try:
        lista.append(int(char))
    except:
        for matte in math:
            if char == matte:
                ops = op[math.index(matte)]
                integers.append(''.join(map(str, lista)))
                lista = []
                break
        else: print("fuck")
    print(char)
print(integers)