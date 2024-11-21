# -*- coding: utf-8 -*-
"""
Created on Wed May 01 22:59:30 2024

@author: DD-Z3ro
"""
# Write your code here :-)

import random
import time
import sys

saying = random.randint(1, 5)  # this declares 'saying' a random number of choice, when done so will quote the below message assigned to the number.


print('Do you wish to do an instant coin flip or choose heads or tails?')
print('1. Instant')
print('2. Choice')

choice = input()

if choice == "1":

    print('coin is being flipped, awaiting results')
    time.sleep(3)

    num = random.randint(1, 2)

    if num == 1:
        result = "heads"
    elif num == 2:
        result = "tails"

    if choice == result:
        print('You won the coin flip, you got ', result)
    else:
        print('Unfortunately the coin was not on your side..', result)


elif choice == "2":

    if saying == 1:
        print('Welcome back, what will fates coin decide for you?')
        print('type heads or tails to make your choice')
    elif saying == 2:
        print('making a choice on something? let fate decide..')
        print('type heads or tails for your choice of face')
    elif saying == 3:
        print('Two choices, two faces, fates hand will decide..')
        print('type heads or tails for your choice of face')

    elif saying == 4:
        print('Behold the wonderous coin flipper!')
        print('type heads or tails for your choice of face')

    elif saying == 5:
        print('back again? Well.. Its time to make a choice..')
        print('type heads or tails for your choice of face')

    choice = input()

    print('Im flipping now, the best of luck to you...')
    time.sleep(3)  # this adds suspense if there was a coin is being flipped.

    num = random.randint(1, 2)

    if num == 1:
        result = "heads"
    elif num == 2:
        result = "tails"

    if choice == result:
        print('You won the coin flip, you got ', result)
    else:
        print('Unfortunately the coin was not on your side..', result)

    print('Would you like to play again? y/n?')

    answer = input()

    if answer == "y":
        print('We are looking into a way of getting that function implemented, sorry for the inconvenience.')
        time.sleep(5)
    elif answer == "n":
        print('Very well, see you next time.')
        time.sleep(3)
        sys.exit
