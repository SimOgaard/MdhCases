import os
import operator

lila = '\033[95m'
gul = '\033[93m'
röd = '\033[91m'
math=["add", "sub", "mul", "div"]
math2=["+", "-", "*", "/"]
op=[operator.add, operator.sub, operator.mul, operator.truediv]

def header(head):
    print(lila+head.center(30))

def line(typ):
    print(lila+typ*30)

while 1+1==2:
    os.system("cls")
    line("*")
    header("Math")
    line("-")
    for x in ["add", "subtract", "multiply", "divide"]: print(gul+x[:3] + " | " + x + " two numbers")
    line("-")
    selection = input(gul+"Selection > ").lower()
    line("-")
    for x in math:
        if selection == x:
            idx = math.index(x)
            print(gul + "Calculating 'c' for expression:" + "\na " + math2[idx] + " b = c")
            ops = op[idx]
            while 1+1==2:
                a = input(gul + "a = ")
                b = input(gul + "b = ")
                try:
                    c = ops(float(a),float(b))
                    print(gul+str(a)+" "+str(math2[idx])+" "+str(b)+" = "+str(c))
                    break
                except: print(röd+"ERROR: Invalid expression '" + str(a) + " " + str(math2[idx]) + " " + str(b) + "'")    
            input(gul+"Continue?")
    if selection not in math:
        print(röd + "ERROR: Invalid expression '" + selection + "' is not an option")
        input(gul+"Continue?")