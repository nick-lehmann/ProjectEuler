def collatz_chain(num):
    if num == 1:
        return 1
    if(num % 2):
        # ungerade
        return 1+collatz_chain(num*3+1)
    else:
        # gerade
        return 1+collatz_chain(num/2)


highest_col = 0
highest_num = 0
max = 1000000
for x in range(1, max+1):
    # print x
    cur = collatz_chain(x)
    if cur > highest_col:
        highest_num = x
        highest_col = cur

print highest_num


# print collatz_chain(97)
