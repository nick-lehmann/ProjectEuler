def mul(list):
    return reduce(lambda x, y: x*y, list)

f = open('./files/11_matrix.txt', 'r')
l = [map(int, line.split(' ')) for line in f]

highest = 0

print 'Left and Right'
# left and right
for line in range(0,20):
    for col in range(0,17):
        test = mul(l[line][col:col+4])
        if test > highest:
            highest = test

print highest

print 'Up and Down'
# up and down
for line in range(0,17):
    for col in range(0,20):
        test = 1
        for x in range(0, 4):
            test *= l[line+x][col]

        if test > highest:
            highest = test

print highest

print 'diagonal from up left to bottom right'
# diagonal from left up to bottom right
for line in range(0,17):
    for col in range(0, 17):
        test = 1
        for x in range(0, 4):
            test *= l[line+x][col+x]

        if test > highest:
            highest = test

print highest

print 'diagonal from up right to bottom left'
# diagonal from right up right to bottom left
for line in range(0, 17):
    for col in range(2, 20):
        test = 1
        for x in range(0,4):
            test *= l[line+x][col-x]

        if test > highest:
            highest = test

print highest
