from math import sqrt

grenze = 500
nummer = 1
teiler = 1
zahl = 1

while teiler < grenze:
    teiler = 0
    nummer += 1
    zahl += nummer
    for x in range(1, int(sqrt(zahl))+1):
        if zahl % x == 0:
            teiler += 2

print zahl
