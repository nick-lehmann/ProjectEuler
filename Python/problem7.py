from mathe import prime

target = 10001
lastprime = 2
num = 1
test = 3

while(num < target):
    if(prime(test)):
        num += 1
        lastprime = test
    test += 2

print lastprime
