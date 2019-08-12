#-------------------------------------------------#
# Title: Working with Dictionaries
# Dev:   RRoot
# Date:  July 16, 2012
# ChangeLog: (Who, When, What)
#   RRoot, 11/02/2016, Created starting template
#   Rachel Smith, 8/11/2019, Added code to complete assignment 5
#https://www.tutorialspoint.com/python/python_dictionary.htm
#-------------------------------------------------#

#-- Data --#
# declare variables and constants
# objFile = An object that represents a file
# strData = A row of text data from the file
# dicRow = A row of data separated into elements of a dictionary {Task,Priority}
# lstTable = A dictionary that acts as a 'table' of rows
# strMenu = A menu of user options
# strChoice = Capture the user option selection

#-- Input/Output --#
# User can see a Menu (Step 2)
# User can see data (Step 3)
# User can insert or delete data(Step 4 and 5)
# User can save to file (Step 6)

#-- Processing --#
# Step 1
# When the program starts, load the any data you have
# in a text file called ToDo.txt into a python Dictionary.

# Step 2
# Display a menu of choices to the user

# Step 3
# Display all todo items to user

# Step 4
# Add a new item to the list/Table

# Step 5
# Remove a new item to the list/Table

# Step 6
# Save tasks to the ToDo.txt file

# Step 7
# Exit program
#-------------------------------

import os

objFileName = "C:\_PythonClass\Assignment05\ToDo.txt"
strData = ""
dicRow = {}
lstTable = []

# Step 1 - Load data from a file
# When the program starts, load each "row" of data
# in "ToDo.txt" into a python Dictionary.
# Add the each dictionary "row" to a python list "table"

with open(objFileName) as file:
    lines = file.readlines()
    for line in lines:
        strData = line.strip().split(',')
        value1 = strData[0]
        value2 = strData[1]
        dicRow.update({'task': value1, 'priority': value2})
        lstTable.append(dicRow)
        dicRow = {}

# Step 2 - Display a menu of choices to the user

while(True):
    print ("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 4] - "))
    print()#adding a new line

    # Step 3 -Show the current items in the table
    if (strChoice.strip() == '1'):
        print('Ok, each line in your list is printed below:')
        for i in lstTable:
            print(i['task']+', '+i['priority'])
    # Step 4 - Add a new item to the list/Table
    elif(strChoice.strip() == '2'):
        dicRow = {}
        priority = ''
        task = input('OK, please give a name for the task: ')
        while priority not in ('low', 'med', 'high'):
            priority = input("Input this task's priority (low/med/high): ").lower()
        dicRow.update({'task': task, 'priority': priority})
        lstTable.append(dicRow)
        print('This data has been successfully added to the list.')
    # Step 5 - Remove an item from the list/Table
    elif(strChoice == '3'):
        tasks = []
        for i in lstTable:
            tasks.append(i['task'].lower().strip())
        rmv_task = input('OK, which task would you like to remove? : ').lower().strip()
        while rmv_task not in tasks:
            rmv_task = input('Please enter an existing task to remove. Your choices are {}: '.format(tasks)).lower().strip()
        # using list comprehension we just rebuild the lstTable with the entries which are NOT removed
        lstTable = [x for x in lstTable if x['task'].lower().strip() != (rmv_task)]
        print('This data has been successfully removed from the list.')
    # Step 6 - Save tasks to the ToDo.txt file
    elif(strChoice == '4'):
        new_file = open(objFileName, "w")
        for i in lstTable:
            new_file.write('{} , {} \n'.format(i['task'],i['priority']))
        new_file.close()
        filepath = os.path.abspath(objFileName)
        print('Your changes have been saved here: {}'.format(filepath))
    elif (strChoice == '5'):
        print('OK this program will close. Thank you.')
        break #and Exit the program
