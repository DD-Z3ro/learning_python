# -*- coding: utf-8 -*-
"""
Created on Thu May 30 14:14:12 2024

@author: DD-Z3ro
"""


class scoreboard:
    def __init__(self):
        self.scores = {
        }

    def view_score(self):
        print("\n")
        print("Here are the scores currently: ")
        print("\n")
        for name in self.scores:
            # prints the scoreboard in rows
            print(name + " : " + str(self.scores[name]))

    def append(self, add):
        # stores data from inputs function and stores it in to the scoreboard
        self.scores[add.name] = add.score

    def adjust_player_score(self):
        print("Who's scored points")
        # sets variable name to what the user inputs in, assumedly a name and stores it
        name = input("player name: ")
        if name in self.scores:
            # finds the inputted name within the list
            print("how much did they score?")
            # sets variable amount to whatever the score was that the player has earned
            amount = int(input("Score: "))
            # adds onto the current amount that player has scored
            result = self.scores[name] + amount
            # changes the results back into self.amount so that it is ready to store the new answer
            self.amount = result
            self.name = name
            # sets name and results into self.amount and self.name variables and then stores them back into the dictionary with updated numbers
            self.scores[self.name] = self.amount
            # informs that the player they chosen
            print(self.name + " score is now " + str(self.amount))
        else:
            # if it doesnt find the name it tells the user it wasnt found and returns them back to the menu
            print("\nPlayer not found on scoreboard")

    def leader(self):
        print("\nHere is leaderboard so far: ")
        # takes key and value and prints them out in order of highest to lowest values
        # lambda defines anonymous function
        # sorted returns a sorted list of the specified iterable object
        for key, value in sorted(self.scores.items(), key=lambda kv: kv[1], reverse=True):
            print("%s : %s" % (key, value))


class inputs:
    def __init__(self):
        self.name = ''
        self.score = 0

    def new_entry(self):
        print("Enter the name:")
        # takes users input for a name and sets it as such
        self.name = input("Name:")
        # sets the score for the new player to 0
        self.score = 0


class main():
    def menu():
        print("\n")
        print("What would you like to do?")
        print("1. View scoreboard")
        print("2. Add a new player")
        print("3. Add to player score")
        print("4. Who's in the lead?")
        print("\n")
        print("type number of choice")
        choice = input("Number: ")

        if choice == "1":
            # launches the view_score function
            scoreboard.view_score()

        if choice == "2":
            # launches new entry function then carries the data from new_entry into append
            add = inputs()
            add.new_entry()
            scoreboard.append(add)

        if choice == "3":
            # launches the adjust_player_score function
            scoreboard.adjust_player_score()

        if choice == "4":
            # launches the leader function within scoreboard
            scoreboard.leader()
        else:
            # if user enters a number greater than 4 will inform the user to make a slection between 1 to 4
            print("invalid input, enter a number from 1 to 4 to make a selection")


if __name__ == "__main__":
    scoreboard = scoreboard()
    while True:
        main.menu()
