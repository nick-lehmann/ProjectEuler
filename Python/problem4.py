# -*- coding: utf-8 -*-
from mathe import palindrom

number1 = number2 = temp = 999
highest_palindrom = 0

while(number1 > 100):
    while(number2 > 100):
        erg = number1 * number2

        if palindrom(erg):
            if erg > highest_palindrom:
                highest_palindrom = erg
        number2 -= 1

    number2 = temp
    number1 -= 1

print highest_palindrom
