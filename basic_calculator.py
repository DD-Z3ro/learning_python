# -*- coding: utf-8 -*-
"""
Created on Sun May  5 22:28:23 2024

@author: DD-Z3ro
"""


def add():
    # sets the variable First from the input of the user.
    First = input("First: ")
    # sets the variable Second from the input of the user.
    Second = input("Second : ")
    # Sets the variable answer by converting their strings into integers and take the number(s) from First and adds it to the number(s) in Second, providing the solution when answer is called.
    answer = int(First) + int(Second)
    # Prints the string "answer: " whilst also converting the answer from an integer to a string and shows the solution.
    print("Answer : " + str(answer))

    return


def subtract():
    # Sets the variable from the input of the user.
    First = input("First: ")
    # Sets the variable from input of the user.
    Second = input("Second: ")
    # Sets the variable answer by converting their strings into integers and take the number(s) from First and subtracts it by the number(s) in Second, providing the solution when answer is called.
    answer = int(First) - int(Second)
    # Prints the string "answer: " whilst also converting the answer from an integer to a string and shows the solution.
    print("Answer: " + str(answer))

    return


def multiply():
    # Sets the variable First from input of the user.
    First = input("First: ")
    # Sets the variable Second from input of the user.
    Second = input("Second: ")
    # Sets the variable answer by converting their strings into integers and take the number(s) from First and mulitplies it by the number(s) in Second, providing the solution when answer is called.
    answer = int(First) * int(Second)
    # Prints the string "answer: " whilst also converting the answer from an integer to a string and shows the solution.
    print("Answer: " + str(answer))

    return


def divide():
    # sets the variable First of input provided by user
    First = input("First: ")
    # sets the variable Second of input provided by user
    Second = input("Second: ")

    # Checks to see if Second variable from the user is zero and prints the message below.
    if Second == "0":
        print("woah there, we cant divide by zero, thats impossible!")
        divide()
    else:
        # Sets the variable answer by converting their strings into integers and take the number(s) from First and divides it by the number(s) in Second, providing the solution when answer is called.
        answer = int(First) / int(Second)
        # Prints the string "answer: " whilst also converting the answer from an integer to a string and shows the solution.
        print("Answer: " + str(answer))

    return


if __name__ == "__main__":

    print("welcome to the calculator.")
    print("1.) Add")
    print("2.) Subtract")
    print("3.) Multiply")
    print("4.) Divide")

    choice = input("Type the name of the function you wish to perform: ")
    # if users input provided from the variable choice is Add it will start the function for add()
    if choice == "Add":
        add()
        # if the input provided from the variable choice is Subtract it will start the function for subtract()
    elif choice == "Subtract":
        subtract()
    # if the input provided from the variable choice is Multiply it will start the function for multiply()
    elif choice == "Multiply":
        multiply()
    # if the input provided fromthe variable  choice is Divide it will start the function for divide()
    elif choice == "Divide":
        divide()
