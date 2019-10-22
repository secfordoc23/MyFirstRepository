"""
    Program: Number Analysis Program
    File: NumberAnalysis.py
    Author: Jason J Welch
    Date: 10/21/2019
    Purpose: A program to allow a user to input a list of numbers.  Then display the lowest, highest, total of numbers,
    and the average number in the entered list.
    
"""
from InputValidation import *


def main():
    while True:
        print("***************************************************************")
        print("\tNumber Analysis Program")
        print("***************************************************************")

        userSelection = display_menu(("Enter 20 numbers for analysis", "Exit"))
        if userSelection == 1:
            numList = get_list_of_numbers()
            analyze_numbers(numList)
        else:
            break

# END main


def get_list_of_numbers():
    numList = []
    for index in range(20):
        number = input_number(f"Enter a number at index {index}: ")
        numList.append(number)
    return numList
# END get_list_of_numbers


def analyze_numbers(numList):
    print("The entered list of numbers: ")
    listTotal = 0
    for number in numList:
        print(f"\t{number}")
        listTotal += number

    listAverage = listTotal / len(numList)

    print(f"\nThe lowest number is: {min(numList)}.")
    print(f"The highest number is: {max(numList)}.")
    print(f"The total of the numbers is: {listTotal}.")
    print(f"The average of the numbers is: {listAverage}.\n")
# END analyze_numbers


main()
# *************************** NO CODE FOLLOWS ***************************
