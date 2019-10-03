"""
   Program: Trip Calculator Utility
   File: DistanceTraveledWithMPGUtility.py
   Author: Jason J. Welch
   Date: 8/24/2019
   Purpose: A utility to calculate distance traveled and gas usage from MPG, MPH, and hours driven
"""

print('*******************************')
print('\tTrip Calculator Utility')
print('*******************************')
# Enter Miles per Hour
milesPerHour = int(input("Enter the vehicle's speed in Miles Per Hour(mph): "))
# Enter Hours driven
hoursDriven = float(input("Enter the total hours driven: "))
# Enter vehicle's MPG
milesPerGallon = int(input("Enter the vehicle's gas mileage in Miles Per Gallon(mpg): "))
# Calculate Distance Traveled to the tenth of a mile
milesTraveled = float(milesPerHour * hoursDriven)
# Calculate the Amount of gas it took, to one decimal place
amountOfGas = float(milesTraveled / milesPerGallon)
# Display Distance and Amount of gas used
print('\n*******************************\n')
print('With the below information entered:')
print(f'\tMPH: {milesPerHour} MPG: {milesPerGallon} Hours: {hoursDriven}\n')
print('Your calculated results are:')
print(f'\tDistance Traveled: {milesTraveled}')
print(f'\tGallons of Gas used: {amountOfGas}')

