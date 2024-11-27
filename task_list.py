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
        print("Here is the current Task List: ")
        # this will list each task as {t}, starting at 1 it will print each task until it reaches the end of the list
        # e.g. task {t} becomes task 1: task etc etc.
        for t, task in enumerate(self.tasklist, start=1):
            print("Task" + str(t) + ":" + task)

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
        for t, completed_task in enumerate(self.completed, start=1):
            print("task" + str(t) + ":" + completed_task + "-Completed")

    def clearcompletedlist(self):
        # this function will clear the list entirely of all tasks within self.completed
        self.completed.clear()
        print("The completed list is now cleared.")

    def loadfile(self):

        file = open("tasklist.txt", "r")
        tasks = file.read().splitlines()
        # reads the file list and splits the strings into a list
        for task in tasks:
            # adds each task from the split tasks into the tasklist
            self.tasklist.append(task)
        file.close()

        file = open("completed.txt", "r")
        tasks = file.read().splitlines()
        for task in tasks:
            self.completed.append(task)
        file.close()
        print("Tasklist and completed list are now loaded!")

    def savefile(self):

        file = open("tasklist.txt", "w")
        for task in self.tasklist:
            # takes all tasks in self.tasklist and writes each of them on a new line to tasklist.txt
            file.write(task + '\n')
        file.close()

        file = open("completed.txt", "w")
        for task in self.completed:
            # takes the list self.completed and writes each of them on a new line to completed.txt
            file.write(task + '\n')
        file.close()


class main_menu:
    def main():
        print("\n")
        print("Welcome to your to-do list!")
        print("Here are the options for you currently: ")
        print("1. View To-Do List")
        print("2. Add task to To-Do List")
        print("3. Remove task from To-Do List")
        print("4. Mark task as completed. ")
        print("5. View completed tasks list")
        print("6. Empty completed tasks list")
        print("7. Save/load Tasks & completed list")

        choice = input("choose a number: ")
        if choice == "1":
            # calls for the view function of the to-do list
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
            print("Type the task you would like to mark as completed?")
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
        if choice == "7":
            print("this option is not available at the moment.")
            print("What would you like to do?")
            print("1.Load file")
            print("2.Save file")
            scndchoice = input("Choice: ")
            if scndchoice == "1":
                todolist.loadfile()

            if scndchoice == "2":
                todolist.savefile()
                print("Tasklist and completed list are now saved")


if __name__ == "__main__":
    todolist = todolist()
    while True:
        main_menu.main()
