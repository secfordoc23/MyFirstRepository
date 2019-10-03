"""
   Program: Celsius to Fahrenheit Utility
   File: CelsiusToFahrenheitUtility.py
   Author: Jason J. Welch
   Date: 8/24/2019
   Purpose: A utility to calculate the degrees Fahrenheit from entered degrees Celsius
"""

print('*******************************')
print(' Celsius to Fahrenheit Utility')
print('*******************************')
# Enter Temperature in Celsius
tempInCelsius = float(input('Enter the temperature in degrees celsius: '))
# Convert Celsius to Fahrenheit
# FORMULA: degreesCelsius1 * 9/5 + 32 or degreesCelsius * 1.8 + 32
tempInFahrenheit = float((tempInCelsius * 1.8) + 32)
# Display Temperature in Fahrenheit
print('\n*******************************\n')
print(f'Temperature in Fahrenheit: {tempInFahrenheit}')
