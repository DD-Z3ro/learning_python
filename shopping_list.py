# -*- coding: utf-8 -*-
"""
Created on Tue May  7 00:42:14 2024

@author: DD-Z3ro
"""


class shoppinglist:
    def __init__(self):
        self.items = {
        }

    # This function views the list currently, if theres nothing in it will prompt user
    def view_list(self):
        if len(self.items) == 0:
            print('\nYour shopping list is empty')

        for item in self.items:
            print(item + ':' + str(self.items[item]))
    # this function appends the list

    def append(self, item):
        if item.name in self.items:                  # if the item already exists on the list do this:
            print("\nthis Item already exists on the list")
            print("\n")
            print(item.name + " has been changed to the new amount of " + str(item.amount))
            self.items[item.name] = item.amount

        else:
            print("\n" + item.name + " has been added with an amount of " + str(item.amount))
            self.items[item.name] = item.amount

    # this function removes an item from the list

    def remove_from_list(self):
        if len(self.items) == 0:
            print('\n Your shopping list is empty, add some items to it.')
            return main_menu()
        print('\nThis is the list currently.')
        for item in self.items:  # this will print the list as it is currently
            print(item + ':' + str(self.items[item]))
        print("\nName the item you wish to remove from the list.")
        name = input()
        name = name.lower()     # this will capitalize our input
        if name in self.items:  # if it finds the item it will proceed to remove the named item from the list
            print('\n' + name + ' has been removed from the list')
            self.item = name
            del self.items[self.item]
        else:                   # if not it will inform the user that it is not on the list
            print("\n" + name + " does not exist on the list.")

    # this function changes the value on an already existing item
    def change_amount(self):
        for item in self.items:
            print(item + ':' + str(self.items[item]))
        print("\nwhich item amount do you want to change?")
        name = input('Item name: ')
        name = name.lower()
        if name in self.items:         # looks for the item within the shoppinglist
            # name = item.name
            print("\n" + name + " are on the list with an amount of " + str(self.items[name]))

            amount = input('\nhow much do you wish to change it to? ')
            self.items[name] = amount  # appends the shopping list now with the new value
            print("\n" + name + " amount has been changed to " + amount)
        else:
            print("\n" + name + " does not exist on the list.")


class List_item:
    def __init__(self):
        self.name = ''
        self.amount = 0

    def __str__(self):
        return self.name + ":" + str(self.amount)

    def getname(self):
        return self.name

    def input_item(self):  # function for inputting item name
        print("What would you like to add to the list? ")
        item_name = input()
        self.name = item_name.lower()  # lower cases the first letter from the text that was input. and puts it into the variable self.name

    def input_amount(self):  # function for inputting item amount
        print(".. and how many do you want to get? ")
        self.amount = int(input())


class main_menu:
    def main():
        print("\n")
        print('Welcome to your shopping list\n')
        print('choose an option below')
        print('1.View List')
        print('2.Append List')
        print('3.Remove from list')
        print('4.change an item amount')

        # sets the variable choice pending on the number input from the user
        choice = input("Type the number of your choice: ")
        print("")

        if choice == "1":
            # will call for the function view_list()

            shoppinglist.view_list()
           # print(shoppinglist.view_list())

        elif choice == "2":
            # will call for the function append_list()
            item = List_item()
            item.input_item()
            item.input_amount()
           # shoppinglist.check_item()
            # print("\n" + item.name + " has been added with an amount of " + str(item.amount))
            shoppinglist.append(item)
            shoppinglist.view_list()
            # append_list()
        elif choice == "3":
            # will call for the function remove_from_list()
            shoppinglist.remove_from_list()

        elif choice == "4":
            # will ask for item name and then load the change_amount function
            shoppinglist.change_amount()

        else:
            print("\nInvalid option, try another selection")


if __name__ == "__main__":
    # upon launching will immediately start the function main()
    shoppinglist = shoppinglist()
    while True:
        main_menu.main()
