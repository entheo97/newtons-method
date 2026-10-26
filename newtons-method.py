#!/usr/bin/env python3

"""
The following is the same function as the final version, but I find the
single-letter variables more conducive to following the math and have therefore
placed it here for reference.

def newton(n, x):
    while True:
        y = (x+n/x)/2
        if abs(y - x) <= .00001:
            print(y)
            return y
        else:
            x = y

newton(10, 3)
"""
def newton(radicand, guess):  # function has two positional parameters
    while True:  # while loop runs until below condition met
        next_guess = (guess + radicand / guess) / 2
        if abs(next_guess - guess) <= .00001:  # .00001 is the tolerance
            print(next_guess)  # print used for test calls
            return next_guess  # returns the approximate value of the square root
        else:
            guess = next_guess  # reassign guess variable

# test calls
newton(81, 8)
newton(101, 1)
newton(69,8)