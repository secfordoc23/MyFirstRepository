"""
    Program: Read Declaration
    File: InputValidation.py
    Author: Jason J Welch
    Date: 9/26/2019
    Purpose: Collection of methods for input validation

"""


# =================== input_number ==============
def input_number(message):
    while True:
        try:
            userInput = int(input(message))
        except ValueError:
            print("That is not an integer! Try again!")
            continue
        else:
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
            return userInput
# END input_menu_option


# ================== input_filename ==================
def input_filename(message, fileOperation):
    while True:
        try:
            userInput = input(message)
            fileContents = open(userInput, fileOperation)
        except IOError:
            print("Invalid File! Please try again.")
            continue
        else:
            return fileContents
# END input_filename


# ================== parse_int ==================
def parse_int(numberString):
    try:  # Try to parse string to int
        number = int(numberString)
    except ValueError:
        number = 0
    finally:
        return number
# END parse_number


# ================== parse_float ==================
def parse_float(numberString):
    try: # Try to parse string to float
        number = float(numberString)
    except ValueError:
        number = 0.0
    finally:
        return number
# END parse_number


# *************************** NO CODE FOLLOWS ***************************

