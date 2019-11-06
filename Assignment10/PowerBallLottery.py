"""
    Program: PowerBallLottery
    File: PowerBallLottery.py
    Author: Jason J Welch
    Date: 11/5/2019
    Purpose: 
    
"""
from InputValidation import *


def main():
    fileName = "pbnumbers.txt"
    while True:
        print("***************************************************************")
        print("\tPowerBallLottery")
        print("***************************************************************")
        userSelection = display_menu(["Start", "Exit"])
        if userSelection == 1:
           numberList = load_list_from_file(fileName)
           convert_to_two_dimensional(numberList)
        else:
            break


# END main


def convert_to_two_dimensional(numbersList):
    numbers2DList = [len(numbersList)][6]

    for index in range(len(numbersList)):
        tempList = numbersList[index].split()
        for index2 in range(len(tempList)):
            numbers2DList[index][index2] = int(tempList[index2])
    return numbers2DList
# END convert_to_two_dimensional

main()
# *************************** NO CODE FOLLOWS ***************************
