import itertools

digits = range(0, 10)
l = len(digits)

num = 0
fin = []

for p in itertools.permutations(digits, l):
    num += 1

    if num == 1000000:
        fin = p
        break

s = ""
for x in fin:
    s += str(x) + " "

print s

