number_min  = 2
number_max  = 100
power_min   = 2
power_max   = 100

l = []

for number in xrange(number_min, number_max+1):
    for power in xrange(power_min, power_max+1):
        l.append(number**power)

print len(set(l))