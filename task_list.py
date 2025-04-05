# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 22:24:04 2024

@author: DD-Z3ro
"""
import sys


class todolist:
    def __init__(self):
        self.tasklist = []
        self.in_progress = []
        self.completed = []

    def view(self):
        # # this function will view the to-do list
        print("Here is the current Task List: ")
        # this will list each task as {t}, starting at 1 it will print each task until it reaches the end of the list
        # e.g. task {t} becomes task 1: task etc etc.
        for t, task in enumerate(self.tasklist, start=1):
            print("Task " + str(t) + " : " + task)

    def add(self, task):
        # This function will add tasks to the to-do list
        print("\n")
        print(task + " has now been added to the list")
        # This will add the string input from the task variable to the task list
        self.tasklist.append(task)

    def set_in_progress(self, task):
        task = int(task) - 1
        in_progress_task = self.tasklist.pop(task)
        self.in_progress.append(in_progress_task)
        print(in_progress_task + " Has now been set to making progress on.")

    def remove(self, task):
        # this function will remove tasks to the to-do list
        task = int(task) - 1  # reduces the input so that it deletes the accurate task
        self.tasklist.pop(task)
        print("Task has been removed from the list.")

    def completedlist(self):
        if not self.in_progress:
            print("There is no progressed tasks to mark as completed, returning to main menu.")
        else:
            todolist.view_in_progress()  # Shows user the current to do list to help make a choice on which task to mark as completed
            print("Type the number of the task you would like to mark as completed")
            task = int(input("Task number: "))
            # reduces the amount to find the precise item on the list
            task = int(task) - 1
            # stores and removes the task on the list within oldtask
            oldtask = self.in_progress.pop(task)
            # this function will add the string input from the task variable and add it to the completed task list
            self.completed.append(oldtask)
            print("{" + oldtask + "} -Task has been marked and moved to the completed list.")

    def viewcompletedlist(self):
        # this function will view the completed tasks list
        print("Here is the completed tasks list: ")
        if not self.completed:
            print("There is no tasks that were completed.")
        else:
            for t, completed_task in enumerate(self.completed, start=1):
                print("task" + str(t) + ":" + completed_task + "-Completed")

    def clearcompletedlist(self):
        # this function will clear the list entirely of all tasks within self.completed
        try:
            while self.completed:
                self.completed.pop()
            print("The completed list is now cleared.")
        except:
            print("Error occured, returning to menu")

    def loadfile(self):

        file = open("tasklist.txt", "r")
        tasks = file.read().splitlines()
        # reads the file list and splits the strings into a list
        for task in tasks:
            # adds each task from the split tasks into the tasklist
            self.tasklist.append(task)
        file.close()

        file = open("in_progress_list.txt", "r")
        tasks = file.read().splitlines()
        for task in tasks:
            self.in_progress.append(task)
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

        file = open("in_progress_list.txt", "w")
        for task in self.in_progress:
            file.write(task + '\n')
        file.close()

        file = open("completed.txt", "w")
        for task in self.completed:
            # takes the list self.completed and writes each of them on a new line to completed.txt
            file.write(task + '\n')
        file.close()

    def view_in_progress(self):
        for t, task in enumerate(self.in_progress, start=1):
            print("Task " + str(t) + " : " + task)
        if not self.in_progress:
            print("There is no tasks in progress currently.")
            print("\n")


class main_menu:
    def main():
        print("\n")
        print("Welcome to your to-do list!")
        print("Current in progress tasks:")
        todolist.view_in_progress()
        print("Here are the options for you currently: ")
        print("1. View To-Do List")
        print("2. Add task to To-Do List")
        print("3. Set task to making progress")
        print("4. Remove task from To-Do List")
        print("5. Mark task as completed. ")
        print("6. View completed tasks list")
        print("7. Empty completed tasks list")
        print("8. Save/load Tasks & completed list")
        print("9. Exit")

        choice = input("choose a number: ")
        if choice == "1":
            # calls for the view function of the to-do list
            todolist.view()

        if choice == "2":
            # takes the input from the user and sets the string into the variable task and calls for the add function with the variable
            print("What is the task you'd like to add?")
            task = input("task: ")
            if task == "":  # incase of no input, return user to menu
                print("Invalid input, returning to menu")
            else:
                print("\n")
                todolist.add(task)

        if choice == "3":
            todolist.view()
            print("Type in the number of the task that you wish to work on")
            task = input("Task number: ")
            todolist.set_in_progress(task)

        if choice == "4":
            # takes input from the user and sets the string into the variable task and calls the remove function with the variable
            todolist.view()
            print("which task would you like to remove?")
            task = int(input("Task: "))
            if task == "":
                print("Invalid input, returning to menu")
            else:
                todolist.remove(task)

        if choice == "5":
            todolist.completedlist()  # Adds the task to the completed list

        if choice == "6":
            # This will call for the viewcompletedlist function
            todolist.viewcompletedlist()

        if choice == "7":
            # this will call for the clearcompletedlist function
            todolist.clearcompletedlist()

        if choice == "8":
            print("What would you like to do?")
            print("1.Load file")
            print("2.Save file")
            scndchoice = input("Choice: ")
            if scndchoice == "1":
                todolist.loadfile()

            if scndchoice == "2":
                todolist.savefile()
                print("Tasklist, in progress and completed lists are now saved")
        if choice == "9":
            print("Switching off, goodbye!")
            sys.exit(0)


if __name__ == "__main__":
    todolist = todolist()
    try:
        todolist.loadfile()
    except OSError:
        # will catch OSError when it fails to load the tasklist file
        print('failed to load tasklist, in_progress or completed list')

    while True:
        main_menu.main()
