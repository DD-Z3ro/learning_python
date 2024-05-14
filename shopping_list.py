# -*- coding: utf-8 -*-
"""
Created on Tue May  7 00:42:14 2024

@author: DD-Z3ro
"""


class shoppinglist:
    def __init__(self):
        self.items = []

    # This is the view_list function
    def view_list(self):
        if len(self.items) == 0:
            print("\nYour shopping list is empty")
            # input("would you like to add things to it? y/n  ")
            # if input == "yes"
            # elif
        for item in self.items:
            print(item)
            #     # this will check to see if the variable shoppinglist is empty
            # if shoppinglist == []:
            #     print("There appears to be nothing on your shopping list!")
            #     print("Would you like to add some items to the list now?")
            #     choice = input("enter yes or no: ")
            #     # calls the choice variable and checks if yes was typed, taking user to append_list() function
            # if choice == "yes":
            #     append_list()
            #     # calls the choice variable and checks if no was typed, will print message and continue forward
            # elif choice == "no":
            #     print("Understood, continuing on..")

            # else:
            #     # calls for the variable shoppinglist and prints its list for review
            #     print('\nThis is the Shopping list so far: \n')
            #     print(shoppinglist, '\n')
            #     # calls the main() function and sends user back to the main menu
        return main_menu.main()
        # This is the append_list function

    def append(self, item):
        self.items.append(item)
        # # calls for the variable shoppinglist and prints its list for review
        # print(shoppinglist)
        # # sets a variable as item and stores input from the user
        # item = input("Adding something to the list? Please type it here: ")
        # # calls the shopping list and appends the list with the item from item variable to the shopping list
        # shoppinglist.append(item)
        # # calls the new shopping list with the appended items now added
        # print("added, here is the new list", shoppinglist)
        # # calls the main() function and sends user back to the main menu
        # return main()

    # this is the remove_from_list function

    def remove_from_list(self, name):
        for item in self.items:
            if item.getname() == name:
                self.item = item
                break
        self.items.remove(self.item)

        # # checks the shoppinglist variable to see if it is empty
        # if shoppinglist == []:
        #     # if the list is empty it will print the following message
        #     print("\nThe shopping list is empty, returning to menu.\n")
        #     return main()
        # # calls for the variable shoppinglist and prints its list for review
        # print(shoppinglist, "\n")
        # # sets a variable for item takes the users input that has to be removed from the list
        # item = input("What would you like to remove from the list? ")
        # # calls the shopping list and removes the users inputted item from the list
        # shoppinglist.remove(item)
        # # calls for the shopping list to show the user the new shopping list
        # print("\n", shoppinglist, "\n")
        # # calls the main() function and sends user back to the main menu
        # return main()

    # this is the list_length function


class List_item:
    def __init__(self):
        self.name = ''
        self.amount = 0

    def __str__(self):
        return self.name + ":" + str(self.amount)

    def getname(self):
        return self.name

    def input(self):
        print("What item would you like to add to the list? ")
        self.name = input()
        print(".. and how many do you want to get? ")
        self.amount = int(input())
        print(self.name + " has been added to the list")
        shoppinglist.append(item)
        print(shoppinglist.view_list())
        return main_menu.main()
        # # prints how many items on are on the shopping list
        # print("\n", "the Length is this shopping list is..", len(shoppinglist), "\n")
        # # calls the main() function and sends user back to the main menu
        # # may change in future
        # return main()

    # This is the main menu function


class main_menu:
    def main():
        print("\n")
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
            shoppinglist.view_list()
#            print(shoppinglist.view_list())

        elif choice == "2":
            # will call for the function append_list()
            item.input()
            # append_list()
        elif choice == "3":
            # will call for the function remove_from_list()
            shoppinglist.remove_from_list()

        elif choice == "4":
            # will call for the function list_length()
            print("\noption unavailable at the moment")
            main_menu.main()
            # list_length()
        else:
            print("\nInvalid option, try another selection")
            main_menu.main()
            # return main()


if __name__ == "__main__":
    # upon launching will immediately start the function main()
    shoppinglist = shoppinglist()
    item = List_item()
    main_menu.main()
