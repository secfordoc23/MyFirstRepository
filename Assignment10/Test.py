"""
    Program: Test
    File: Test.py
    Author: Jason J Welch
    Date: 11/6/2019
    Purpose: 
    
"""

def validate_card_number(cardNumber):
    message = "Valid"
    numChar = len(cardNumber)
    startIndex = 0
    if validate_length_and_isNumerical(cardNumber):
        total = double_and_total(cardNumber[-2::-2])
        print(total)
    else:
        message = "Invalid!"
    print(message)
# END


def double_and_total(numbers):
    doubleTotal = 0
    for char in numbers:
        doubleNumber = int(char) * 2
        if doubleNumber > 9:
            doubleNumber = doubleNumber - 9
        doubleTotal += doubleNumber
    return doubleTotal
# END


def validate_length_and_isNumerical(cardNumber):
    if (len(cardNumber) >= 13 or len(cardNumber) <= 16) and cardNumber.isdigit():
        return True
    else:
        return False
# END


validate_card_number("123456789012345")