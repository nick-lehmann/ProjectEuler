max = 0
digits = 1
power = 5       # possible to specify power (with 4 you get the result from the example)
max_power = 9**power
found = False
n = []

while(not found):
    if len(str(digits * max_power)) > digits:
        digits += 1
    else:
        found = True

# result is six; with the seven fifth powers of nine you can only display a number with six digits 
max = digits * max_power

for num in xrange(2, max+1):
    summe = 0
    for c in str(num):
        summe += int(c) ** power
    if summe == num:
        n.append(num)

print sum(n)
