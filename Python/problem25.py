def len_digit(num):
    return len(str(num))

fib1 = 1
fib2 = 1
num = 2
max_digits = 1000

# print str(1) + " : " + str(fib1)
# print str(2) + " : " + str(fib2)

while(True):
    temp    = fib2
    fib2    += fib1
    fib1    = temp
    num += 1
    
    # print str(num) + " : " + str(fib2)

    if len_digit(fib2) == max_digits:
        print "Final: " + str(num)
        break