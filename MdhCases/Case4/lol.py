rainbowColors=['\033[31m','\033[38;2;243;134;48m','\033[33m','\033[32m','\033[34m','\033[35m']
string = "hejsansvejsan"

for Amount, Char in enumerate(string):
    print(Amount,(Amount % len(rainbowColors)),len(rainbowColors))
    print(rainbowColors[Amount % len(rainbowColors)]+Char)
