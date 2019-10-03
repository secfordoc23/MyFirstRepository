"""
    Program: HotDogCookoutCalculator
    File: HotDogCookoutCalculator.py
    Author: Jason J Welch
    Date: 8/30/2019
    Purpose: Program to calculate the number of hot dog packages and hot dog packages needed
        for a cookout and how many will be left over.
    
"""

print("***************************************************************")
print("\tHot Dog Cookout Calculator")
print("***************************************************************")

# Constants
HOT_DOG_PACKAGE_COUNT = 10
HOT_DOG_BUN_PACKAGE_COUNT = 8
ONE_PACKAGE = 1

# Get the number of people
numberOfPeople = int(input("Enter the expected count of people that are to attend the cookout: "))

# Get the number of hot dogs per person
hotDogsPerPerson = int(input("Enter the estimated number of hot dogs per person: "))

# Calculate the total number of hot dogs needed
estimatedHotDogTotal = numberOfPeople * hotDogsPerPerson

# Calculate the number of hot dogs packages needed, and the number of hot dog buns needed
if estimatedHotDogTotal == 0:
    # if count is 0 then nothing is needed
    hotDogPackagesNeededCount = 0
    hotDogsLeftCount = 0
    hotDogBunPackagesNeededCount = 0
    hotDogBunsLeftCount = 0
else:
    if estimatedHotDogTotal <= HOT_DOG_PACKAGE_COUNT:
        # if count is less then or equal to the number of hot dogs in a package set to 1 package
        hotDogPackagesNeededCount = ONE_PACKAGE
    else:
        if (estimatedHotDogTotal % HOT_DOG_PACKAGE_COUNT) > 0:
            # if the modulus of the number of hot dogs is greater then 0 then add 1 more package
            hotDogPackagesNeededCount = int(estimatedHotDogTotal / HOT_DOG_PACKAGE_COUNT) + ONE_PACKAGE
        else:
            hotDogPackagesNeededCount = int(estimatedHotDogTotal / HOT_DOG_PACKAGE_COUNT)

    if estimatedHotDogTotal <= HOT_DOG_BUN_PACKAGE_COUNT:
        # if count is less then or equal to the number of hot dogs buns in a package set to 1 package
        hotDogBunPackagesNeededCount = ONE_PACKAGE
    else:
        if (estimatedHotDogTotal % HOT_DOG_BUN_PACKAGE_COUNT) > 0:
            # if the modulus of the number of hot dog buns is greater then 0 then add 1 more package
            hotDogBunPackagesNeededCount = int(estimatedHotDogTotal / HOT_DOG_BUN_PACKAGE_COUNT) + ONE_PACKAGE
        else:
            hotDogBunPackagesNeededCount = int(estimatedHotDogTotal / HOT_DOG_BUN_PACKAGE_COUNT)

# Calculate the left over hot dogs and buns
hotDogsLeftCount = (hotDogPackagesNeededCount * HOT_DOG_PACKAGE_COUNT) - estimatedHotDogTotal
hotDogBunsLeftCount = (hotDogBunPackagesNeededCount * HOT_DOG_BUN_PACKAGE_COUNT) - estimatedHotDogTotal

# Output results
print(f"\nThe total hot dogs estimated for the cookout is: {estimatedHotDogTotal}")
print(f"This will require {hotDogPackagesNeededCount} packages of hot dogs, and {hotDogBunPackagesNeededCount}"
      f" packages of hot dog buns.")
print(f"There will be {hotDogsLeftCount} hot dogs and {hotDogBunsLeftCount} hot dog buns left over.")

# *************************** NO CODE FOLLOWS ***************************
