from mathe import sum_proper_divisor

abundant = []
vals = []
for num in xrange(2, 28123):
    if num < sum_proper_divisor(num):
        abundant.append(num)

for num in xrange(1, 28123):
    val = True
    print num
    for abun in abundant:
        if abun > num:
            break
        if (num - abun) in abundant:
            val = False
            break

    if val:
        vals.append(num)

print sum(vals)
