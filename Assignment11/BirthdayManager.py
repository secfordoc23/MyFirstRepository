"""
    Program: BirthdayManager
    File: BirthdayManager.py
    Author: Jason J Welch
    Date: 11/12/2019
    Purpose: 
    
"""
from InputValidation import *


# =================== main ===================
def main():
    programName = "Birthday Manager"
    birthdays = {}
    while True:
        userSelection = display_menu(programName, ("Look up a Birthday", "Add a Birthday", "Update a Birthday",
                                                   "Delete a Birthday", "Exit"))
        if userSelection == 1:
            find_birthday(birthdays)
        elif userSelection == 2:
            add_birthday(birthdays)
        elif userSelection == 3:
            update_birthday(birthdays)
        elif userSelection == 4:
            delete_birthday(birthdays)
        else:
            break
# END main


# =================== find_birthday ===================
def find_birthday(birthdays):
    name = input("Enter a name: ")
    birthday = birthdays.get(name, "unknown")
    print(f"The date of {name}\'s birthday is {birthday}.")
# END find_birthday


# =================== add_birthday ===================
def add_birthday(birthdays):
    name = input("Enter a name: ")
    birthday = input("Enter the date of the birthday: ")

    if name in birthdays:
        print(f"{name} already has a birthday entered.")
    else:
        birthdays[name] = birthday
        print(f"Added {name} with a birthday of {birthday}.")
# END add_birthday


# =================== update_birthday ===================
def update_birthday(birthdays):
    name = input("Enter a name: ")
    if name in birthdays:
        birthday = input("Enter the date of the birthday: ")
        birthdays[name] = birthday
        print(f"{name}\'s birthday has been updated to {birthday}.")
    else:
        print(f"Unable to find the name {name}.")
# END update_birthday


# =================== delete_birthday ===================
def delete_birthday(birthdays):
    name = input("Enter a name: ")
    if name in birthdays:
        del birthdays[name]
        print(f"Deleted {name}\'s entry.")
    else:
        print(f"Unable to find the name {name}.")
# END delete_birthday


# Call Main
main()
# *************************** NO CODE FOLLOWS ***************************
