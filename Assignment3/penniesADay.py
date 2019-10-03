"""
    Program: penniesADay
    File: penniesADay.py
    Author: Jason J Welch
    Date: 9/6/2019
    Purpose: Program to calculate a system of pay where the amount paid to workers
        is non-cummulative double a day from 1 - 31 days.
    
"""

# ==================== inputNumber() ===================
def inputNumber(message):
    while True:
        try:
            userInput = int(input(message + ": "))
        except ValueError:
            print("That is not a number! Please try again.")
            # continue
        else:
            return userInput
    # break


# ==================== Main ===========================
PENNY = .01
NICKEL = .05
DIME = .10
QUARTER = .25

print("***************************************************************")
print("\tMoney A Day Calculator")
print("***************************************************************\n")

runAgain = 'y'
while runAgain.lower() == 'y':
    # Menu to select the amount per day
    while True:
        print("Please select one of the following: ")
        print("\t1. Pennies")
        print("\t2. Nickels")
        print("\t3. Dimes")
        print("\t4. Quarters")
        selectedPay = inputNumber("Enter select amount")
        if selectedPay <= 0 or selectedPay > 4:
            print("Selection is out of Range!")
        else:
            break
    # Enter how many days to calculate
    while True:
        daysWorked = inputNumber("Enter the number of days worked(1 - 31)")
        if daysWorked <= 0 or daysWorked > 31:
            print("Invalid Date! Please enter a date between 1 and 31.")
        else:
            break
    # Based on Menu selection set dailyPay to constant money value
    if selectedPay == 1:
        dailyPay = PENNY
    elif selectedPay == 2:
        dailyPay = NICKEL
    elif selectedPay == 3:
        dailyPay = DIME
    elif selectedPay == 4:
        dailyPay = QUARTER
    else:
        print("Invalid Pay selection!  You should never see this error!!!")
        break
    # Display daily pay calculation
    print("\nDay\t\tPay")
    print("------------")
    for day in range(1, daysWorked + 1):
        print("{0}\t\t{1:.2f}".format(day, dailyPay))
        dailyPay = dailyPay * 2
    # Ask the user if they wish to run the program again
    runAgain = input("\nDo you want to run again?(y/n): ")
