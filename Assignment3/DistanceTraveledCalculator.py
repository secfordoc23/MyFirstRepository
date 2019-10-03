"""
    Program: DistanceTraveledCalculator
    File: DistanceTraveledCalculator.py
    Author: Jason J Welch
    Date: 9/5/2019
    Purpose: A program to calculate a list of distances based on the speed of the vehicle and the total time traveled.
    
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

# ==================== inputFloat() ===================
def inputFloat(message):
    while True:
        try:
            userInput = float(input(message + ": "))
        except ValueError:
            print("That is not a number! Please try again.")
            continue
        else:
            return userInput
            break


# ==================== Main ===========================
TIME_INCREMENT = .5
print("***************************************************************")
print("\tDistance Traveled Calculator")
print("***************************************************************\n")
runAgain = 'y'
while runAgain.lower() == 'y':
    speed = inputNumber("Please enter the speed of the vehicle in miles per hour(mph)")
    totalTime = inputFloat("Please enter the number of hours traveled")

    print("\nTime\t\tDistance")
    print("--------------------")
    time = TIME_INCREMENT
    while time <= totalTime:
        distance = time * speed
        print(f"{time}\t\t\t{distance}")
        time += TIME_INCREMENT
    # Ask the user if they wish to run the program again
    runAgain = input("\nDo you want to run again?(y/n): ")