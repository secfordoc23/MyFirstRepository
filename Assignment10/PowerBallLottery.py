"""
    Program: PowerBallLottery
    File: PowerBallLottery.py
    Author: Jason J Welch
    Date: 11/5/2019
    Purpose: 
    
"""
from InputValidation import *


def main():
    programName = "PowerBall Lottery"
    fileName = "pbnumbers.txt"
    numbersList = load_list_from_file(fileName)
    countList = find_frequency(numbersList)
    numberToDisplay = 10
    
    while True:
        userSelection = display_menu(programName, ["Most Frequent PowerBall Numbers", "Least Frequent PowerBall Numbers", "Exit"])
        if userSelection == 1:
            get_max_frequency(countList, numberToDisplay)
        elif userSelection == 2:
            get_min_frequency(countList, numberToDisplay)
        else:
            break
# END main


def find_frequency(numbersList):
    powerBallPickList = []
    frequencyCountList = [0] * 69

    for line in numbersList:
        powerBallPickList.append(line.split())

    for index in range(0, len(frequencyCountList)):
        for powerBallPick in powerBallPickList:
            for number in powerBallPick:
                if int(number) == index + 1:
                    frequencyCountList[index] += 1
    return frequencyCountList
# END convert_to_two_dimensional


def get_max_frequency(numbersList, howManyToGet):
    maxValueList = []
    maxIndexList = []

    for counter in range(howManyToGet):
        maxValue = 0
        maxIndex = 0
        for index in range(0, len(numbersList)):
            if numbersList[index] > maxValue:
                maxValue = numbersList[index]
                maxIndex = index + 1

        maxValueList.append(maxValue)
        maxIndexList.append(maxIndex)
        numbersList[maxIndex - 1] = -1

    display_results(maxIndexList, maxValueList)
# END get_max_frequency


def get_min_frequency(numbersList, howManyToGet):
    minValueList = []
    minIndexList = []
    maxListValue = max(numbersList)

    for counter in range(howManyToGet):
        minValue = maxListValue
        minIndex = 0
        for index in range(0, len(numbersList)):
            if numbersList[index] < minValue:
                minValue = numbersList[index]
                minIndex = index + 1

        minValueList.append(minValue)
        minIndexList.append(minIndex)
        numbersList[minIndex - 1] = maxListValue

    display_results(minIndexList, minValueList)
# END get_max_frequency


def display_results(indexList, valueList):
    print("PowerBall Number Frequency:")
    for index in range(len(indexList)):
        print(f"\t{indexList[index]} has shown up {valueList[index]} times.")
    print("\n")
# END display_results


main()
# *************************** NO CODE FOLLOWS ***************************
