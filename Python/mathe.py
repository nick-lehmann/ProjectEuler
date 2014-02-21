# -*- coding: utf-8 -*-
# my own module with some functions for solving mathematical problems

# finds the highest prime factor of the argument in a recursive way
def highest_prime(n):
    i = 2
    while(n % i != 0 and i < n):
        i += 1
    if(i < n):
        return highest_prime(n/i)
    else:
        return n