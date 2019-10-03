"""
    Program: ElementarySchoolMath
    File: ElementarySchoolMath.py
    Author: Jason J Welch
    Date: 9/17/2019
    Purpose: A program to teach elementary math operations to the user.
    Limited to 0-9 digits.
    
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
MIN = 0
MAX = 9

runAgain = 'y'
while runAgain.lower() == 'y':
    print("============================================")
    print("\tElementary Math Tutor")
    print("============================================")

    # Menu
    while True:
        print("Please select one of the following: ")
        print("\t1. Addition")
        print("\t2. Subtraction")
        print("\t3. Multiplication")
        print("\t4. Division")
        print("\t5. Exit")
        selectedOption = inputNumber("Enter selection: ")
        if selectedOption <= 0 or selectedOption > 5:
            print("Selection is out of Range!")
        elif selectedOption == 5:
            runAgain = 'n'
            numberOfProblems = 0
            break
        else:
            # Enter how many math problems to display
            while True:
                numberOfProblems = inputNumber("Enter the number of questions to generate: ")
                if numberOfProblems <= 0:
                    print("Please enter a number greater that 1!")
                else:
                    break
            break

    numberCorrect = 0
    numberIncorrect = 0
    # Generate a number of Math Problems based on user input
    for number in range(numberOfProblems):
        # Generate Random Numbers
        firstNumber = random.randint(MIN, MAX)
        secondNumber = random.randint(MIN, MAX)

        if selectedOption == 1:
            # Addition
            correctAnswer = firstNumber + secondNumber
            operation = '+'
        elif selectedOption == 2:
            # Subtraction
            if secondNumber > firstNumber:
                tempNumber = firstNumber
                firstNumber = secondNumber
                secondNumber = tempNumber
            correctAnswer = firstNumber - secondNumber
            operation = '-'
        elif selectedOption == 3:
            # Multiplication
            correctAnswer = firstNumber * secondNumber
            operation = '*'
        elif selectedOption == 4:
            # Division
            if secondNumber == 0:
                secondNumber += 1
            if firstNumber % secondNumber > 0:
                tempNumber = firstNumber
                firstNumber *= secondNumber
            correctAnswer = secondNumber
            secondNumber = tempNumber
            operation = '/'
        else:
            break

        userAnswer = inputNumber("\n{} {} {} = ".format(firstNumber, operation, secondNumber))
        # Validate Answer
        if correctAnswer == userAnswer:
            numberCorrect += 1
            print("Correct")
        else:
            numberIncorrect += 1
            print("Incorrect - The correct answer is {}".format(correctAnswer))
    # End For Loop
    if selectedOption != 5:
        print("\nYou got {} correct, and {} incorrect.\n".format(numberCorrect, numberIncorrect))
        runAgain = input("Play again?(y/n): ")
# End runAgain loop
print("\nThank you for using the Elementary Math Tutor!")
# *************************** NO CODE FOLLOWS ***************************
