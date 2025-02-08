# -*- coding: utf-8 -*-
"""
Created on Wed May 01 22:59:30 2024

@author: DD-Z3ro
"""
# Write your code here :-)

import random
import time
import sys


class coinflip:
    def instant():
        print('coin is being flipped, awaiting results')
        time.sleep(3)

        num = random.randint(1, 2)

        if num == 1:
            result = "heads"
            print('The choins face shows..', result)
        elif num == 2:
            result = "tails"
            print('the coins face shows.. ', result)

        print('Would you like to play again? y/n?')

        answer = input()

        if answer == "y":
            print("Playing Coinflip again..")
            time.sleep(3)
            coinflip.instant()
        elif answer == "n":
            print('Returning to menu..')
            time.sleep(3)

    def choice():
        saying = random.randint(1, 5)  # this declares 'saying' a random number of choice, when done so will quote the below message assigned to the number.

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
        choice = choice.capitalize()

        print('Im flipping now, the best of luck to you...')
        time.sleep(3)  # this adds suspense if there was a coin is being flipped.

        num = random.randint(1, 2)

        if num == 1:
            result = "Heads"
        elif num == 2:
            result = "Tails"

        if choice == result:
            print('You won the coin flip, you got ' + result)
        else:
            print('Unfortunately the coin was not on your side..' + result)

        print('Would you like to play again? y/n?')

        answer = input()

        if answer == "y":
            print('Playing Coinflip again..')
            time.sleep(3)
            coinflip.choice()
        elif answer == "n":
            print('Returning to menu..')


class main_menu:
    def main():
        print('Do you wish to do an instant coin flip or choose heads or tails?')
        print('1. Instant')
        print('2. Choice')
        print('3. Exit')

        choice = input()

        if choice == "1":
            coinflip.instant()

        elif choice == "2":
            coinflip.choice()

        elif choice == "3":
            print('Goodbye!')
            sys.exit()


if __name__ == "__main__":
    while True:
        main_menu.main()
