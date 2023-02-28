import random

string = "Hola Mundo"

#string = str(random.randint(0,9))

for s in string:
    if s in "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz":
        print(s)

print(string)