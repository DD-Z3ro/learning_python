# -*- coding: utf-8 -*-
"""
Created on Wed May  8 20:23:02 2024

@author: DD-Z3ro
"""


def factorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * factorial(n - 1)


if __name__ == "__main__":
    num = 24
    fact = factorial(num)
    print(fact)
