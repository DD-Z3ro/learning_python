# -*- coding: utf-8 -*-
"""
Created on Tue May  7 00:42:14 2024

@author: DD-Z3ro
"""

# This is the view_list function


def view_list():

    # this will check to see if the variable shoppinglist is empty
    if shoppinglist == []:
        print("There appears to be nothing on your shopping list!")
        print("Would you like to add some items to the list now?")
        choice = input("enter yes or no: ")
        # calls the choice variable and checks if yes was typed, taking user to append_list() function
        if choice == "yes":
            append_list()
        # calls the choice variable and checks if no was typed, will print message and continue forward
        elif choice == "no":
            print("Understood, continuing on..")

    else:
        # calls for the variable shoppinglist and prints its list for review
        print('\nThis is the Shopping list so far: \n')
        print(shoppinglist, '\n')
        # calls the main() function and sends user back to the main menu
    return main()


# This is the append_list function

def append_list():

    # calls for the variable shoppinglist and prints its list for review
    print(shoppinglist)
    # sets a variable as item and stores input from the user
    item = input("Adding something to the list? Please type it here: ")
    # calls the shopping list and appends the list with the item from item variable to the shopping list
    shoppinglist.append(item)
    # calls the new shopping list with the appended items now added
    print("added, here is the new list", shoppinglist)
    # calls the main() function and sends user back to the main menu
    return main()


# this is the remove_from_list function

def remove_from_list():
    # checks the shoppinglist variable to see if it is empty
    if shoppinglist == []:
        # if the list is empty it will print the following message
        print("\nThe shopping list is empty, returning to menu.\n")
        return main()
    # calls for the variable shoppinglist and prints its list for review
    print(shoppinglist, "\n")
    # sets a variable for item takes the users input that has to be removed from the list
    item = input("What would you like to remove from the list? ")
    # calls the shopping list and removes the users inputted item from the list
    shoppinglist.remove(item)
    # calls for the shopping list to show the user the new shopping list
    print("\n", shoppinglist, "\n")
    # calls the main() function and sends user back to the main menu
    return main()


# this is the list_length function

def list_length():

    # prints how many items on are on the shopping list
    print("\n", "the Length is this shopping list is..", len(shoppinglist), "\n")
    # calls the main() function and sends user back to the main menu
    # may change in future
    return main()


# This is the main menu function
def main():

    print('Welcome to your shopping list\n')
    print('choose an option below')
    print('1.View List')
    print('2.Append List')
    print('3.Remove from list')
    print('4.List length')
    # sets the variable choice pending on the number input from the user
    choice = input("Type the number of your choice: ")

    if choice == "1":
        # will call for the function view_list()
        view_list()

    elif choice == "2":
        # will call for the function append_list()
        append_list()
    elif choice == "3":
        # will call for the function remove_from_list()
        remove_from_list()

    elif choice == "4":
        # will call for the function list_length()
        list_length()

    return main()


if __name__ == "__main__":
    # upon launching will immediately start the function main()
    shoppinglist = []
    main()
