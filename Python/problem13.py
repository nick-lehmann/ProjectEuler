from math import fsum

f = open('./files/13_numbers.txt', 'r')
a = [int(x) for x in f]

sum = 0
for num in a:
    sum += num

print str(sum)[0:10]
