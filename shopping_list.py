# -*- coding: utf-8 -*-
"""
Created on Tue May  7 00:42:14 2024

@author: DD-Z3ro
"""

import sqlite3


class shoppinglist:
    def __init__(self):
        self.conn = sqlite3.connect("shoppinglist.db")
        self.items = {
        }

    # This function views the list as it currently is
    def view_list(self):
        try:
            # this will pull all information within the database
            view = self.conn.execute("SELECT * FROM SHOPPINGLIST")
            print("Here is shopping list currently: ")
            for row in view:
                # Then print specificly the products and the amount for each one in rows
                print(row[1], row[2])
        except:
            # if there is nothing to print from the database will print the following message.
            print("nothing to print, consider adding items the shopping list.")

    # this function appends the list
    def append(self, item):
        try:
            # sets the variables for product with item.name and the number from item.amount
            product = item.name
            amount = item.amount
            # telling the database that we are adding a product into PRODUCT and its amount to AMOUNT, sets it to the query variable
            query = "INSERT INTO SHOPPINGLIST(PRODUCT, AMOUNT) VALUES(?,?)"
            # takes the the variables product and amount and puts them within the arg variable
            arg = (product, int(amount))
            # proceeds to insert the product and amount into the shoppinglist database
            self.conn.execute(query, arg)
            # Then saves the changes to the database
            self.conn.commit()
            print("\n" + item.name + " has been added with an amount of " + str(item.amount))
        except:
            print("Error with adding item.")

    # this function removes things from the list
    def remove_from_list(self, item):
        try:
            # sets the variable product with the string from item.name
            product = item.name
            # telling the database that to delete the targetted product from the product variable and sets it in the query variable
            query = "DELETE FROM SHOPPINGLIST WHERE PRODUCT = (?)"
            # takes the variable product and stores it within the arg variable,
            arg = (product,)
            # proceeds to find the desired product from the database and remove it.
            self.conn.execute(query, arg)
            # Then saves the changes to the database
            self.conn.commit()
            print(product + " has been successfully been removed.")
        except:
            # if should it fail to find the item the user has input then print the following message
            print("Item not found.")

    # this function changes the value of an already existing item
    def change_amount(self, item):
        try:
            product = item.name
            amount = item.amount
            # tells the database that we wish to set the amount for the targetted product that was input and sets it in the query variable
            query = "UPDATE SHOPPINGLIST SET AMOUNT = ? WHERE PRODUCT = ?"
            # takes both variables and sets them to a new variable when communicating with the database
            arg = (int(amount), product, )
            # proceeds to change the items value to the newly set one
            view = self.conn.execute(query, arg)
            # finds the targetted item and changes its original amount to the new amount set
            self.conn.commit()
            # then saves the changes to the database
            print(product + " has now been updated.")

        except:
            # if should it fail to find the item the user has input then print the following message
            print("Item not found.")


class List_item:
    def __init__(self):

        self.name = ''
        self.amount = 0

    def __str__(self):
        return self.name + str(self.amount)
        # return self.name + ":" + str(self.amount)

    def getname(self):
        return self.name

    # function for inputting item name
    def input_item(self):

        item_name = input("Item name: ")
        # if the name was capitalised it will lower case the first letter from the text that was input and puts it into the variable self.name
        self.name = item_name.lower()

    # function for inputting item amount
    def input_amount(self):
        self.amount = int(input())


class main_menu:
    def main():
        print("\n")
        print('Welcome to your shopping list\n')
        print('choose an option below')
        print('1.View List')
        print('2.Add to List')
        print('3.Remove from list')
        print('4.change an item amount')

        # sets the variable choice pending on the number input from the user
        choice = input("Type the number of your choice: ")
        print("")

        if choice == "1":
            # will call for the function view_list()

            shoppinglist.view_list()

        elif choice == "2":
            # will call for the functions input_item, input_amount and append_list() then view_list to show it is added
            item = List_item()
            print("What would you like to add to the list? ")
            item.input_item()
            print("..and how many would you like to add? ")
            item.input_amount()
            shoppinglist.append(item)
            shoppinglist.view_list()
        elif choice == "3":
            # will call for the functions, view list, input_item and remove_from_list()
            item = List_item()
            shoppinglist.view_list()
            print("Which item would you like to remove?")
            item.input_item()
            shoppinglist.remove_from_list(item)

        elif choice == "4":
            # will call for functions, view_list, input_ item and input_amount to then change_amount function
            shoppinglist.view_list()
            item = List_item()
            print("Which item would you like to adjust the amount of?")
            item.input_item()
            print("How much of " + item.name + " do you want?")
            item.input_amount()
            shoppinglist.change_amount(item)

        else:
            print("\nInvalid option, try another selection")


if __name__ == "__main__":

    # upon launching will immediately start the function main()
    shoppinglist = shoppinglist()
    try:
        shoppinglist.conn.execute('''CREATE TABLE SHOPPINGLIST
                     (ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                      PRODUCT VARCHAR(50) NOT NULL,
                      AMOUNT INTEGER NOT NULL)''')
        print("Shoppinglist created, moving to menu")

    except:
        print("Shoppinglist exists, now loading..")
    while True:
        main_menu.main()
