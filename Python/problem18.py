f = open('./files/18_triangle.txt', 'r')
l = [map(int, line.split(' ')) for line in f]

for line in reversed(range(0, len(l)-1)):
    # print l[line][len(l[line])-1]
    for col in range(0, len(l[line])):
        l[line][col] += max(l[line+1][col], l[line+1][col+1])

print l[0][0]
