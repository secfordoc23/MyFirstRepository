"""
    Program: AgeClassifierUtility
    File: AgeClassifierUtility.py
    Author: Jason J Welch
    Date: 8/30/2019
    Purpose: Program to determine the age classification of a person based on there age
    
"""

print("***************************************************************")
print("\tAge Classifier Utility")
print("***************************************************************")
# Constants
INFANT = 1
CHILD = 13
TEENAGER = 20

# Get a Person's age
personsAge = int(input("Enter the age of the desired person: "))

# Age Comparison
if personsAge <= INFANT:
    ageClassification = "Infant"
elif personsAge < CHILD:
    ageClassification = "Child"
elif personsAge < TEENAGER:
    ageClassification = "Teenager"
else:
    ageClassification = "Adult"
# Output results
print(f"\nBased on the age entered for the person they are an {ageClassification}")
# *************************** NO CODE FOLLOWS ***************************
