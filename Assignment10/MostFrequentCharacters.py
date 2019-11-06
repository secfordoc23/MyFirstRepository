"""
    Program: Most Frequent Characters
    File: MostFrequentCharacters.py
    Author: Jason J Welch
    Date: 11/3/2019
    Purpose: 
    
"""
from InputValidation import *


# =================== main ===================
def main():
    programName = "Most Frequent Characters Utility"
    while True:
        userSelection = display_menu(programName, ("Find the most frequent character in a string", "Exit"))
        if userSelection == 1:
            enteredText = input("Enter Text: ")
            character = character_frequency(enteredText)
            print(f"\nThe highest frequency character is {character.upper()}.\n")
        else:
            break
# END main


# =================== character_frequency ===================
def character_frequency(inputString):
    alphabetTuple = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'o', 'p', 'q', 'r', 's', 't', 'u'
                     , 'v', 'w', 'x', 'y', 'z')
    alphabetCounterList = [0] * 26
    for character in inputString:
        for index in range(len(alphabetTuple)):
            if character.lower() in alphabetTuple and character.lower() == alphabetTuple[index]:
                alphabetCounterList[index] += 1
    highestFrequencyIndex = alphabetCounterList.index(max(alphabetCounterList))
    return alphabetTuple[highestFrequencyIndex]
# END character_frequency


main()
# *************************** NO CODE FOLLOWS ***************************
