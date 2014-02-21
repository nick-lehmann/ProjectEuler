def digit_sum(string):
    return sum([ord(c)-96 for c in string])

with open('./files/22_names.txt', 'r') as f:
    names = sorted(f.readline().lower().replace('"', '').split(','))

names.insert(0, "")

summe = 0
num = 0

for num in xrange(0, len(names)):
    score = num * digit_sum(names[num])
    summe += score

print summe
