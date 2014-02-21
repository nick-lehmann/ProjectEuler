from math import sqrt
from mathe import sum_proper_divisor

amicable = []
for x in range(1, 10001):
    if x == sum_proper_divisor(sum_proper_divisor(x)) and x != sum_proper_divisor(x):
        amicable.append(x)

print sum(amicable)

print "\n ----------------- \n"

for x in range(1,10001):
    if x == sum_proper_divisor(x):
        print x
