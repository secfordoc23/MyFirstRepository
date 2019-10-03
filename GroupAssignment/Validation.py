"""
    Program: Validation
    File: Validation.py
    Author: Jason J Welch, Rita Allen, Eric Gavin
    Date: 9/26/2019
    Purpose: Collection of methods for validation

"""


# ===================inputNumber ==============
def input_number(message):
    while True:
        try:
            userInput = int(input(message))
        except ValueError:
            print("That is not an integer! Try again!")
            continue
        else:
            break
    return userInput
# END input_number


# ==================== input_decimal ===================
def input_decimal(message):
    while True:
        try:
            userInput = float(input(message))
        except ValueError:
            print("That is not a number! Please try again.")
            continue
        else:
            break
    return userInput
# End input_decimal


# ================== input_menu_option =========================
def input_menu_option(message, numberOfOptions):
    while True:
        try:
            userInput = int(input(message))
            if 1 > userInput or userInput > numberOfOptions:
                print("Please enter a valid menu choice: ")
                continue
        except ValueError:
            print("That is not a number! Please try again.")
            continue
        else:
            break
    return userInput
# END input_menu_option
