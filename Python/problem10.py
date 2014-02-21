from mathe import prime

sum = 0
max = 2000000
for num in range(1, max+1):
    if prime(num):
        sum += num

print sum
