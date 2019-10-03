"""
    Program: RectangleAreaCompareUtility
    File: RectangleAreaCompareUtility.py
    Author: Jason J Welch
    Date: 8/30/2019
    Purpose: Program to compare the area of 2 different rectangles
    
"""

# Get the length and width of Rectangle one
print("***************************************************************")
print("\tCompare the Area of Two Rectangles")
print("***************************************************************")
rectangleOneLength = float(input("Please enter the Length of Rectangle One:"))
rectangleOneWidth = float(input("Please enter the Width of Rectangle One:"))

# Get the length and width of Rectangle two
rectangleTwoLength = float(input("Please enter the Length of Rectangle Two:"))
rectangleTwoWidth = float(input("Please enter the Width of Rectangle Two:"))
# Calculate area of each Rectangle
rectangleOneArea = rectangleOneLength * rectangleOneWidth
rectangleTwoArea = rectangleTwoLength * rectangleTwoWidth

# Compare the rectangles area and output which one has the greatest area
print(f"\nRectangle One has an area of {rectangleOneArea}, and Rectangle Two has an area of {rectangleTwoArea}.\n")
if rectangleOneArea > rectangleTwoArea:
    print("Rectangle One has a greater area.")
elif rectangleOneArea == rectangleTwoArea:
    print("Both Rectangle One and Rectangle Two have the same area.")
else:
    print("Rectangle Two has a greater area.")

# *************************** NO CODE FOLLOWS ***************************