from math import fsum

def square(n):
    return n**2

max = 100

# compute sum of squares
sum_of_squares = fsum(map(square, range(1, max+1)))

# compute square of sum
square_of_sum = square(fsum(range(1, max+1)))

diff = square_of_sum - sum_of_squares
print diff
