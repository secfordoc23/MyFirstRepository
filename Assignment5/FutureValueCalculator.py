"""
    Program: Future Value Calculator
    File: FutureValueCalculator.py
    Author: Jason J Welch
    Date: 9/25/2019
    Purpose: Calculate the Future balance of an account given the current balance, monthly interest rate, and
        number of months.
    
"""


# ==================== main() ===================
def main():
    runAgain = 'y'
    while runAgain.lower() == 'y':
        print("***************************************************************")
        print("\tFuture Value Calculator")
        print("***************************************************************\n")

        # Get User input
        currentBalance = input_number("Enter the the account's current balance: ")
        monthlyInterestRate = input_decimal("Enter the monthly interest rate for the account as a decimal: ")
        numberOfMonths = input_number("Enter the number of months to calculate: ")

        # Calculate Future balance
        futureBalance = calculate_compounded_monthly_interest(currentBalance, monthlyInterestRate, numberOfMonths)

        # Display Results
        display_future_value(futureBalance)
        runAgain = input("\nDo you want to run again?(y/n): ")
    # End While runAgain
# End main


# ==================== calculate_compounded_monthly_interest() ===================
def calculate_compounded_monthly_interest(currentBalance, interestRate, numberOfMonths):
    futureBalance = currentBalance * (1 + interestRate) ** numberOfMonths
    return futureBalance
# End calculate_compounded_monthly_interest


# ==================== display_future_value() ===================
def display_future_value(futureBalance):
    print(f"\nYour future balance will be: {futureBalance}.")
# End display_future_value


# ==================== input_number() ===================
def input_number(message):
    while True:
        try:
            userInput = int(input(message))
        except ValueError:
            print("That is not a number! Please try again.")
            continue
        else:
            return userInput
            break
# end input_number


# ==================== input_decimal() ===================
def input_decimal(message):
    while True:
        try:
            while True:
                userInput = float(input(message))
                if 0 > userInput > 1:
                    print("Please enter a decimal between 0 and 1!")
                else:
                    break
        except ValueError:
            print("That is not a number! Please try again.")
            continue
        else:
            return userInput
            break
# end input_number


main()
# *************************** NO CODE FOLLOWS ***************************
