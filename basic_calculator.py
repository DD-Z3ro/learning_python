# -*- coding: utf-8 -*-
"""
Created on Sun May  5 22:28:23 2024

@author: DD-Z3ro
"""


def add():
    # sets the variable First from the input of the user.
    First = (input("First: "))
    # sets the variable Second from the input of the user.
    Second = (input("Second : "))
    # Sets the variable answer to take the number(s) from First and adds it to the number(s) in Second, providing the solution when answer is called.
    answer = int(First) + int(Second)
    # Prints the string "answer: " whilst also converting the answer from an integer to a string and shows the solution.
    print("Answer : " + str(answer))

    return


def subtract():
    # Sets the variable from the input of the user.
    First = input("First: ")
    # Sets the variable from input of the user.
    Second = input("Second: ")
    # Sets the variable answer to take the number(s) from First and subtracts it by the number(s) in Second, providing the solution when answer is called.
    answer = int(First) - int(Second)
    # Prints the string "answer: " whilst also converting the answer from an integer to a string and shows the solution.
    print("Answer: " + str(answer))

    return


def multiply():
    # Sets the variable First from input of the user.
    First = input("First: ")
    # Sets the variable Second from input of the user.
    Second = input("Second: ")
    # Sets the variable answer to take the number(s) from First and subtracts it by the number(s) in Second, providing the solution when answer is called.
    answer = int(First) * int(Second)
    # Prints the string "answer: " whilst also converting the answer from an integer to a string and shows the solution.
    print("Answer: " + str(answer))

    return


def divide():
    # sets the variable First of input provided by user
    First = input("First: ")
    # sets the variable Second of input provided by user
    Second = input("Second: ")

    # Checks to see if both inputs from the user are zero and prints the message below.
    if First and Second == "0":
        print("woah there, we cant divide by zero, thats impossible!")
    else:
        # Sets the variable answer to take the number(s) from First and subtracts it by the number(s) in Second, providing the solution when answer is called.
        answer = int(First) / int(Second)
        # Prints the string "answer: " whilst also converting the answer from an integer to a string and shows the solution.
        print("Answer: " + str(answer))

    return


if __name__ == "__main__":

    print("welcome to the calculator.")
    print("""
          1.) Add
          2.) Subtract
          3.) Multiply
          4.) Divide""")

    choice = input("Type the name of the function you wish to perform: ")
    # if users input provided from the variable choice is Add it will start the function for add()
    if choice == "Add":
        add()
    # if the input provided from the variable choice is Subtract it will start the function for subtract()
    elif input() == "Subtract":
        subtract()
    # if the input provided from the variable choice is Multiply it will start the function for multiply()
    elif input() == "Multiply":
        multiply()
    # if the input provided fromthe variable  choice is Divide it will start the function for divide()
    elif input() == "Divide":
        divide()
