"""
    Program: Name Search
    File: NameSearch.py
    Author: Jason J Welch
    Date: 10/24/2019
    Purpose: Program to find, add, insert, delete girl's and boy's names from lists.
    
"""
from InputValidation import *


# ================== main ==================
def main():
    menuItems = ("Find a Boy's name", "Find a Girl's name", "Add a Boy's name", "Add a Girl's name",
                 "Insert a Boy's name at a specific rank", "Insert a Girl's name at a specific rank",
                 "Delete a Boy's name", "Delete a Girl's name", "Save Lists", "Exit")

    girlNameFile = "GirlNames.txt"
    boyNameFile = "BoyNames.txt"
    girlList = load_list_from_file(girlNameFile)
    boyList = load_list_from_file(boyNameFile)

    while True:
        print("***************************************************************")
        print("\tName Search")
        print("***************************************************************")
        userSelection = display_menu(menuItems)
        if userSelection == 1: # Find a Boy's name
            find_name(boyList)
        elif userSelection == 2: # Find a Girl's name
            find_name(girlList)
        elif userSelection == 3: # Add a Boy's name
            boyList = add_name(boyList)
        elif userSelection == 4: # Add a Girl's name
            girlList = add_name(girlList)
        elif userSelection == 5: # Insert a Boy's name at a specific index
            boyList = insert_name(boyList)
        elif userSelection == 6: # Insert a Girl's name at a specific index
            girlList = insert_name(girlList)
        elif userSelection == 7: # Delete a Boy's name
            boyList = delete_name(boyList)
        elif userSelection == 8: # Delete a Girl's name
            girlList = delete_name(girlList)
        elif userSelection == 9: # Save Lists
            write_list_to_file(girlList, girlNameFile)
            write_list_to_file(boyList, boyNameFile)
        else: # Exit
            break

# END main


# ================== load_list_from_file ==================
def load_list_from_file(fileName):
    if not does_file_exist(fileName):
        outFile = open(fileName, "w")
        outFile.write("Default\n")
        outFile.close()

    fileList = []
    infile = open(fileName, "r")
    for line in infile:
        fileList.append(line.rstrip('\n'))

    infile.close()

    return fileList
# END load_list_from_file


# ================== write_list_to_file ==================
def write_list_to_file(nameList, fileName):
    try:
        outFile = open(fileName, "w")
        for name in nameList:
            outFile.write(name + "\n")
    except IOError:
        print("\nFailed to write list to File!\n")
    else:
        print(f"\nList was successfully saved to {fileName}\n")
    finally:
        outFile.close()
# END write_list_to_file


# ================== find_name ==================
def find_name(nameList):
    name = get_name()
    if name in nameList:
        display_name_rank(nameList, name)
    else:
        print(f"\n{name} was not found in name list.\n")
# END find_name


# ================== add_name ==================
def add_name(nameList):
    name = get_name()
    nameList.append(name)
    display_name_rank(nameList, name)

    return nameList
# END add_name


# ================== insert_name ==================
def insert_name(nameList):
    name = get_name()
    nameRank = input_number("Enter what rank to place the name: ")
    nameList[nameRank] = name
    display_name_rank(nameList, name)

    return nameList
# END insert_name


# ================== delete_name ==================
def delete_name(nameList):
    name = get_name()
    if name in nameList:
        nameRank = nameList.remove(name)
        print(f"\n{name} was removed.\n")
    else:
        print(f"\n{name} was not found in name list.\n")
    return nameList
# END delete_name


# ================== get_name ==================
def get_name():
    name = input("Enter name a name: ")
    return name
# END get_name


# ================== display_name_rank ==================
def display_name_rank(nameList, name):
    nameRank = nameList.index(name) + 1
    print(f"\n{name} is ranked {nameRank}.\n")
# END display_name_rank


main()
# *************************** NO CODE FOLLOWS ***************************
