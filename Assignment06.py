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

objFileName = "C:\_PythonClass\Assignment06\ToDo.txt"

# Step 1 - Load data from a file
# When the program starts, load each "row" of data
# in "ToDo.txt" into a python Dictionary.
# Add the each dictionary "row" to a python list "table"

class FileProcessing():
    '''This class contains methods to process files'''

    @staticmethod
    def FiletoDict(path):
        '''This function takes values from a csv file and puts each of the two fields into a dictionary.
           The dictionary has keys task and priority to correspond with our to-do list'''
        dic_row = {}
        new_list = []
        with open(path) as file:
            lines = file.readlines()
            for line in lines:
                str_dat = line.strip().split(',')
                value1 = str_dat[0]
                value2 = str_dat[1]
                dic_row.update({'task': value1, 'priority': value2})
                new_list.append(dic_row)
                dic_row = {}
        return new_list

    @staticmethod
    def SaveToFile(file, lst):
        '''This function takes in a list and writes a CSV file with two columns corresponding to the entries'''
        new_file = open(file, "w")
        for i in lst:
            new_file.write('{} , {} \n'.format(i['task'], i['priority']))
        new_file.close()
        filepath = os.path.abspath(file)
        print('Your changes have been saved here: {}'.format(filepath))


# Step 2 - Display a menu of choices to the user

# define a class to hold my various list operations
class ListProcessing():
    '''This class contains methods to process list items'''
    @staticmethod
    def AddValues(lst):
        '''This function allows users to add new items to a dictionary.'''
        row = {}
        priority = ''
        task = input('OK, please give a name for the task: ')
        while priority not in ('low', 'med', 'high'):
            priority = input("Input this task's priority (low/med/high): ").lower()
        row.update({'task': task, 'priority': priority})
        lst.append(row)
        return lst

    @staticmethod
    def PrintValues(lst):
        '''This function prints values from a list in comma-separated format'''
        print('Ok, each line in your list is printed below:')
        for i in lst:
            print(i['task']+', '+i['priority'])

    @staticmethod
    def RemoveValues(lst):
        '''This function allows users to remove items from a dictionary.'''
        tasks = []
        for i in lst:
            tasks.append(i['task'].lower().strip())
        rmv_task = input('OK, which task would you like to remove? : ').lower().strip()
        while rmv_task not in tasks:
            rmv_task = input('Please enter an existing task to remove. Your choices are {}: '.format(tasks)).lower().strip()
        # using list comprehension we just rebuild the lstTable with the entries which are NOT removed
        lst = [x for x in lst if x['task'].lower().strip() != (rmv_task)]
        print('This data has been successfully removed from the list.')
        return lst



lstTable = FileProcessing.FiletoDict(objFileName)


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
        ListProcessing.PrintValues(lstTable)
    # Step 4 - Add a new item to the list/Table
    elif(strChoice.strip() == '2'):
        lstTable = ListProcessing.AddValues(lstTable)
    # Step 5 - Remove an item from the list/Table
    elif(strChoice == '3'):
        lstTable = ListProcessing.RemoveValues(lstTable)
    # Step 6 - Save tasks to the ToDo.txt file
    elif(strChoice == '4'):
        FileProcessing.SaveToFile(objFileName, lstTable)
    elif (strChoice == '5'):
        print('OK this program will close. Thank you.')
        break #and Exit the program
