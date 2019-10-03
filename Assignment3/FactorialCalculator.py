"""
    Program: FactorialCalculator
    File: FactorialCalculator.py
    Author: Jason J Welch
    Date: 9/8/2019
    Purpose: Program to calculate a non negative number's factorial
    
"""


# ==================== inputNumber() ===================
def inputNumber(message):
    while True:
        try:
            userInput = int(input(message + ": "))
        except ValueError:
            print("That is not a number! Please try again.")
            continue
        else:
            return userInput
            break


# ==================== Main ===========================
while True:
    print("***************************************************************")
    print("\t\t\t\tFactorial Calculator")
    print("***************************************************************")
    # Get a non negative number from the user
    while True:
        factorialToCalculate = inputNumber("Please enter a non negative integer to calculate its factorial")
        # Validate that the number in not a negative number
        if factorialToCalculate <= 0:
            print(f"{factorialToCalculate} is not a non negative integer.")
        else:
            break

    # Calculate the factorial
    print("\n\tCalculation Steps")
    print("\t-----------------")
    calculatedFactorial = factorialToCalculate
    for number in range(factorialToCalculate - 1, 0, -1):
        currentCalculation = calculatedFactorial * number
        print(f"\t{calculatedFactorial} x {number} = {currentCalculation}")
        calculatedFactorial = currentCalculation

    # Display the calculated Factorial
    print(f"\n\t{factorialToCalculate}! is {calculatedFactorial}.")

    # Ask user to run program again
    runAgain = input("\nDo you want to calculate another factorial? (y/n): ")
    if runAgain.lower() != 'y':
        break

# *************************** NO CODE FOLLOWS ***************************
