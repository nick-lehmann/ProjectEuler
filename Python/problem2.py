number1 = 1
number2 = 2
sum = 2

while(True):
    if((number1+number2) % 2 == 0):
        sum += number1+number2

    temp = number1
    number1 = number2
    number2 += temp

    if(number1+number2 > 4000000):
        break

print sum
