# -*- coding: utf-8 -*-
# my own module with some functions for solving mathematical problems

from math import sqrt

# finds the highest prime factor of the argument in a recursive way
def highest_prime(n):
    i = 2
    while(n % i != 0 and i < n):
        i += 1
    if(i < n):
        return highest_prime(n/i)
    else:
        return n


# checks argument for being a palindrom
def palindrom(n):
    if str(n) == str(n)[::-1]:
        return True
    else:
        return False


# Checks whether arg is a prime or not
def prime(n):
    n = abs(int(n))

    # 0 and 1 are not primes
    if n < 2:
        return False

    # 2 is the only even prime number
    if n == 2: 
        return True    

    # all other even numbers are not primes
    if not n & 1: 
        return False

    # range starts with 3 and only needs to go up the squareroot of n for all odd numbers
    for x in range(3, int(n**0.5)+1, 2):
        if n % x == 0:
            return False

    return True


# create list of primes 
def create_prime_list(min, max):
    primes = []
    for x in xrange(min, max+1):
        if prime(x):
            primes.append(x)

    return primes


# return list of proper divisors of num
def proper_divisor(num):
    max = sqrt(num)
    pdivisor = [1]
    for x in range(2, int(max)+1):
        if num % x == 0:
            pdivisor.append(x)
            if x != num/x:
                pdivisor.append(num/x)
    return pdivisor

def sum_proper_divisor(num):
    return sum(proper_divisor(num))
