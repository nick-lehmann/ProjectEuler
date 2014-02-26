from mathe import prime, create_prime_list
import itertools

def func(num, ko1, ko2):
    return num**2 + (ko1*num) + ko2

def prime_length(a, b):
    length = 0
    for x in itertools.count(0):
        if prime(func(x, a, b)):
            length += 1
        else:
            break

    return length

def main():
    highest = 0
    best_a = 0
    best_b = 0
    for b in create_prime_list(-1000, 1000):
        for a in xrange(-1000,1001):
            length = prime_length(a,b)
            if length > highest:
                highest = length
                best_a = a
                best_b = b

    print best_a * best_b


main()