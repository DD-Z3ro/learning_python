# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 22:24:04 2024

@author: DD-Z3ro
"""


class todolist:
    def __init__(self):
        self.tasklist = []
        self.completed = []

    def view(self):
        # # this function will view the to-do list

        # this will list each task as {t}, starting at 1 it will print each task until it reaches the end of the list
        # e.g. task {t} becomes task 1: task etc etc.
        for t, task in enumerate(self.tasklist, start=1):
            print(f"task {t}: {task}")

    def add(self, task):
        # This function will add tasks to the to-do list
        print("\n")
        print(task + " has now been added to the list")
        # This will add the string input from the task variable to the task list
        self.tasklist.append(task)

    def remove(self, task):
        # this function will remove tasks to the to-do list
        print(task + " has been removed from the list.")
        self.tasklist.remove(task)

    def completedlist(self, task):
        # this function will add the string input from the task variable and add it to the completed task list
        self.completed.append(task)

    def viewcompletedlist(self):
        # this function will view the completed tasks list
        print("Here is the completed tasks list: ")
        print(self.completed)

    def clearcompletedlist(self):
        # this function will clear the list entirely of all tasks within self.completed
        self.completed.clear()
        print("The completed list is now cleared.")


class main:
    def main_menu():
        print("\n")
        print("Welcome to your to-do list!")
        print("Here are the options for you currently: ")
        print("1. View To-Do List")
        print("2. Add task to To-Do List")
        print("3. Remove task from To-Do List")
        print("4. Mark task as completed. ")
        print("5. View completed tasks list")
        print("6. Empty completed tasks list")

        choice = input("choose a number: ")
        if choice == "1":
            # calls for the view function of the to-do list
            print("Here is the current Task List: ")
            todolist.view()

        if choice == "2":
            # takes the input from the user and sets the string into the variable task and calls for the add function with the variable
            print("What is the task you'd like to add?")
            task = input("task: ")
            print("\n")
            todolist.add(task)

        if choice == "3":
            # takes input from the user and sets the string into the variable task and calls the remove function with the variable
            todolist.view()
            print("which task would you like to remove?")
            task = input("Task: ")
            todolist.remove(task)

        if choice == "4":
            todolist.view()  # Shows user the current to do list to help make a choice on which task to mark as completed
            print("Which task would you like to mark as completed?")
            task = input("Task: ")
            todolist.completedlist(task)  # Adds the task to the completed list
            todolist.remove(task)  # Then removes that specific task from the to-do list
            print("Task has successfully been moved to the completed list.")

        if choice == "5":
            # This will call for the viewcompletedlist function
            todolist.viewcompletedlist()

        if choice == "6":
            # this will call for the clearcompletedlist function
            todolist.clearcompletedlist()


if __name__ == "__main__":
    # upon launching will immediately load up the main menu
    todolist = todolist()
    while True:
        main.main_menu()
