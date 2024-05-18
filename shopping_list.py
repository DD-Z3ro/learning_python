# -*- coding: utf-8 -*-
"""
Created on Tue May  7 00:42:14 2024

@author: DD-Z3ro
"""


class shoppinglist:
    def __init__(self):
        self.items = []

    # This function views the list currently, if theres nothing in it will prompt user
    def view_list(self):
        if len(self.items) == 0:
            print("\nYour shopping list is empty")

        for item in self.items:
            print(item)
    # this function appends the list

    def append(self, item):
        self.items.append(item)

    # this function removes an item from the list, not working currently.
    def remove_from_list(self):
        name = input()
        for item in self.items:
            if item.getname() == name:
                self.item = item
                break
        self.items.remove(self.item)
    # this function appends the item on the list

    def increase_amount(self):
        name = input()
        for item in self.items:
            if item.getname() == name:
                self.item = item
                # print('The current amount for' + str(self.item) + 'is' + str(self.amount))
                # amount = input('how much would you like to add it? ')
                # new_amount = (self.amount) + int(amount)
                # self.amount.append(item)

        pass

    def decrease_amount(self):
        pass


class List_item:
    def __init__(self):
        self.name = ''
        self.amount = 0

    def __str__(self):
        return self.name + ":" + str(self.amount)

    def getname(self):
        return self.name

    def input_item(self):  # function for inputting item
        print("What item would you like to add to the list? ")
        self.name = input()

    def input_amount(self):  # function for inputting amount
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
        print('4.Add to items amount')
        print('5.Reduce an items amount')
        # sets the variable choice pending on the number input from the user
        choice = input("Type the number of your choice: ")

        if choice == "1":
            # will call for the function view_list()

            shoppinglist.view_list()
           # print(shoppinglist.view_list())

        elif choice == "2":
            # will call for the function append_list()
            item = List_item()
            item.input_item()
            item.input_amount()
            print(item.name + " has been added with an amount of" + str(item.amount))
            shoppinglist.append(item)
            print(shoppinglist.view_list())
            # append_list()
        elif choice == "3":
            # will call for the function remove_from_list()
            print("Name the item you wish to remove from the list")
            shoppinglist.remove_from_list()

        elif choice == "4":
            # will call for the increase_amount function()
            print('enter the item you wish to change the amount of: ')
            shoppinglist.increase_amount()

        elif choice == "5":
            shoppinglist.decrease_amount()

        else:
            print("\nInvalid option, try another selection")


if __name__ == "__main__":
    # upon launching will immediately start the function main()
    shoppinglist = shoppinglist()
    while True:
        main_menu.main()
