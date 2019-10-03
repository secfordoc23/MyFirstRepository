"""
   Program: Vineyard Planning Utility
   File: VineyardPlanningUtility.py
   Author: Jason J. Welch
   Date: 8/24/2019
   Purpose: A utility to calculate the number of vines that can be planted in a row given the row length
        end post assembly length and space between vines.
"""
print('*******************************')
print('  Vineyard Planning Utility')
print('*******************************')
# Enter in the Row length in feet
rowLength = float(input('Enter the length of a row in feet: '))
# Enter in the Amount of space the End Post Assembly takes up in feet
endPostAssemblyLength = float(input('Enter the amount of space the End Post Assembly takes up in feet: '))
# Enter the Space between vines in feet
spaceBetweenVines = float(input('Enter the space between vines in feet: '))
# Calculate number of vines possible in a row
# FORMULA: Vines in a row = ( Row Length - (2 X End Post Assembly)) divided by Space Between Vines
numberOfVines = float((rowLength - (2 * endPostAssemblyLength)) / spaceBetweenVines)
# Display the number of possible vines in a row
print('\n*******************************\n')
print(f'Total number of vines in a row: {numberOfVines}')