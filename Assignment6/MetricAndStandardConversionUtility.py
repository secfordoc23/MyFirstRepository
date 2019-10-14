"""
    Program: Metric And Standard Conversion Utility
    File: MetricAndStandardConversionUtility.py
    Author: Jason J Welch
    Date: 9/30/2019
    Purpose: 
    
"""
from MetricAndStandardConversionCalculations import *
from InputValidation import *

# =================== main() ===================
def main():
    while True:
        print("***************************************************************")
        print("\tMetric And Standard Conversion Utility")
        print("***************************************************************")

        print("Main Menu:")
        print("\t1. Convert Weights")
        print("\t2. Convert Lengths")
        print("\t3. Exit")
        userSelection = input_menu_option("Enter selection: ", 3)
        if userSelection == 1:
            weights_menu()
        elif userSelection == 2:
            length_menu()
        else:
            break

# END main

# =================== weights_menu() ===================
def weights_menu():
    print("\nWeights Menu:")
    print("\t1. Kilograms to Pounds")
    print("\t2. Grams to Ounces")
    print("\t3. Pounds to Kilograms")
    print("\t4. Ounces to Grams")
    print("\t5. Grams to Kilograms")
    print("\t6. Kilograms to Grams")
    print("\t7. Pounds to Ounces")
    print("\t8. Ounces to Pounds")
    print("\t9. Back to Main Menu")
    userSelection = input_menu_option("Enter selection: ", 9)

    if userSelection != 9:
        amount = input_decimal("Enter the amount to convert: ")
        if userSelection == 1:
            convertedValue = convert_kilogram_to_pounds(amount)
            convertedFrom = "kg"
            convertedTo = "lb"
        elif userSelection == 2:
            convertedValue = convert_grams_to_ounces(amount)
            convertedFrom = "g"
            convertedTo = "oz"
        elif userSelection == 3:
            convertedValue = convert_pounds_to_kilograms(amount)
            convertedFrom = "lb"
            convertedTo = "kg"
        elif userSelection == 4:
            convertedValue = convert_ounces_to_grams(amount)
            convertedFrom = "oz"
            convertedTo = "g"
        elif userSelection == 5:
            convertedValue = convert_metric_to_metric(amount, 3, convertUp=True)
            convertedFrom = "g"
            convertedTo = "kg"
        elif userSelection == 6:
            convertedValue = convert_metric_to_metric(amount, 3, convertUp=False)
            convertedFrom = "kg"
            convertedTo = "g"
        elif userSelection == 7:
            convertedValue = convert_pounds_to_ounces(amount)
            convertedFrom = "lb"
            convertedTo = "oz"
        elif userSelection == 8:
            convertedValue = convert_ounces_to_pounds(amount)
            convertedFrom = "oz"
            convertedTo = "lb"

        display_results(amount, convertedFrom, convertedValue, convertedTo)
# END weight_menu


# =================== length_menu() ===================
def length_menu():
    print("\nLengths Menu:")
    print("\t1. Kilometers to Miles")
    print("\t2. Miles to Kilometers")
    print("\t3. Meters to Feet")
    print("\t4. Feet to Meters")
    print("\t5. Centimeters to Inches")
    print("\t6. Inches to Centimeters")
    print("\t7. Inches to Feet")
    print("\t8. Feet to Inches")
    print("\t9. Centimeters to Meters")
    print("\t10. Meters to Centimeters")
    print("\t11. Meters to Kilometers")
    print("\t12. Kilometers to Meters")
    print("\t13. Centimeters to Kilometers")
    print("\t14. Kilometers to Centimeters")
    print("\t15. Back to Main Menu")
    userSelection = input_menu_option("Enter selection: ", 15)

    if userSelection != 15:
        amount = input_decimal("Enter the amount to convert: ")
        if userSelection == 1:
            convertedValue = convert_kilometers_to_miles(amount)
            convertedFrom = "km"
            convertedTo = "mi"
        elif userSelection == 2:
            convertedValue = convert_miles_to_kilometers(amount)
            convertedFrom = "mi"
            convertedTo = "km"
        elif userSelection == 3:
            convertedValue = convert_meters_to_feet(amount)
            convertedFrom = "m"
            convertedTo = "ft"
        elif userSelection == 4:
            convertedValue = convert_feet_to_meters(amount)
            convertedFrom = "ft"
            convertedTo = "m"
        elif userSelection == 5:
            convertedValue = convert_centimeters_to_inches(amount)
            convertedFrom = "cm"
            convertedTo = "in"
        elif userSelection == 6:
            convertedValue = convert_inches_to_centimeters(amount)
            convertedFrom = "in"
            convertedTo = "cm"
        elif userSelection == 7:
            convertedValue = convert_inches_to_feet(amount)
            convertedFrom = "in"
            convertedTo = "ft"
        elif userSelection == 8:
            convertedValue = convert_feet_to_inches(amount)
            convertedFrom = "ft"
            convertedTo = "in"
        elif userSelection == 9:
            convertedValue = convert_metric_to_metric(amount, 2, convertUp=True)
            convertedFrom = "cm"
            convertedTo = "m"
        elif userSelection == 10:
            convertedValue = convert_metric_to_metric(amount, 2, convertUp=False)
            convertedFrom = "m"
            convertedTo = "cm"
        elif userSelection == 11:
            convertedValue = convert_metric_to_metric(amount, 3, convertUp=True)
            convertedFrom = "m"
            convertedTo = "km"
        elif userSelection == 12:
            convertedValue = convert_metric_to_metric(amount, 3, convertUp=False)
            convertedFrom = "km"
            convertedTo = "m"
        elif userSelection == 13:
            convertedValue = convert_metric_to_metric(amount, 5, convertUp=True)
            convertedFrom = "cm"
            convertedTo = "km"
        elif userSelection == 14:
            convertedValue = convert_metric_to_metric(amount, 5, convertUp=False)
            convertedFrom = "km"
            convertedTo = "cm"
        display_results(amount, convertedFrom, convertedValue, convertedTo)
# End length_menu


# =================== display_results()  ===================
def display_results(amount, convertedFrom, convertedValue, convertedTo):
    print("\nResult:")
    print(f"\t{amount} {convertedFrom} = {convertedValue:.3f} {convertedTo}\n")
# END display_results


main()
# *************************** NO CODE FOLLOWS ***************************
