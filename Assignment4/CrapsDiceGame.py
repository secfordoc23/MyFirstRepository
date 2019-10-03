"""
    Program: CrapsDiceGame
    File: CrapsDiceGame.py
    Author: Jason J Welch
    Date: 9/17/2019
    Purpose: A simple game of Craps
    
"""
import random


# ==================== inputNumber() ===================
def inputNumber(message):
    while True:
        try:
            userInput = int(input(message))
        except ValueError:
            print("That is not a number! Please try again.")
            continue
        else:
            return userInput
            break


# ==================== Main ===========================
MIN = 1
MAX = 6
runAgain = 'y'
while runAgain.lower() == 'y':
    print("***************************************************************")
    print("\tCraps Dice Game")
    print("***************************************************************")
    passLine = "OFF"
    point = 0
    selectedOption = 1
    gameOver = False
    while not gameOver and selectedOption == 1:
        # Menu
        while True:
            print(f"\n*** Pass Line: {passLine} ***")
            if passLine == "OFF":
                print(f"*** Point: {point} ***\n")
            print("Please select one of the following: ")
            if passLine == "OFF":
                print("\t1. Roll the Come-out Roll")
            else:
                print("\t1. Roll Again")
            print("\t2. Exit")
            selectedOption = inputNumber("Enter selection: ")
            if 0 > selectedOption > 2:
                print("Selection is out of Range!")
            elif selectedOption == 2:
                gameOver = True
                break
            else:
                break
        # End Menu

        if not gameOver:
            # Game Play information
            if passLine == "OFF":
                print("You need a 7 or an 11 to win.  If you roll 2, 3, or 12 you lose.")
                print("Any other roll will be set as the point.")
            else:
                print(f"You need a(n) {point} to win.  If you roll a 7 you lose.\n")

            # Roll the Dice
            dice1 = random.randint(MIN, MAX)
            dice2 = random.randint(MIN, MAX)
            roll = dice1 + dice2
            print(f"\nDice 1: {dice1}\nDice 2: {dice2}\n\nYou Rolled a(n) {roll}\n")

            # Check Role
            if passLine == "OFF":
                if roll == 7 or roll == 11:
                    print("You Win!\n")
                elif roll == 2 or roll == 3 or roll == 12:
                    gameOver = True
                    print("You Lose!\n")
                else:
                    passLine = "ON"
                    point = roll
            else:
                if roll == 7:
                    gameOver = True
                    print("You Lose!\n")
                elif roll == point:
                    print("You Win!\n")
    # End gameOver
    runAgain = input("Thank you for playing! Do you wish to play again?(y/n): ")
# End runAgain
# *************************** NO CODE FOLLOWS ***************************
