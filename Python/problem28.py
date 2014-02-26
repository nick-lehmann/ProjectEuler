height  = 1001
width   = 1001
end = height * width
sum = 1
summand = 2
cur = 1
finish = False

while(not finish):
    for x in xrange(0,4):
        cur = cur + summand
        if cur <= end:
            sum += cur
        else:
            finish = True
    summand += 2

print sum