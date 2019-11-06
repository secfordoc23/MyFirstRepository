"""
    Program: Magic 8 Ball
    File: InputValidation.py
    Author: Jason J Welch
    Date: 9/26/2019
    Updated: 10/28/2019
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


# ================== display_menu =========================
def display_menu(options):
    while True:
        try:
            print("Options: ")
            for index in range(len(options)):
                print(f"\t{index + 1}. {options[index]}")
            userInput = int(input("Enter Selection: "))
            if 1 > userInput or userInput > len(options):
                print("Please enter a valid menu choice.")
                continue
        except ValueError:
            print("That is not a number! Please try again.")
            continue
        else:
            return userInput
# END display_menu


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


# ================== does_file_exist ==================
def does_file_exist(filename):
    doesExist = False
    try:
        infile = open(filename, "r")
    except IOError:
        print("File not found or error opening file!")
    else:
        doesExist = True
    finally:
        infile.close()
        return doesExist
# END does_file_exist


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


# ================== load_list_from_file ==================
def load_list_from_file(fileName):
    if not does_file_exist(fileName):
        outFile = open(fileName, "w")
        outFile.write("Default\n")
        outFile.close()

    fileList = []
    infile = open(fileName, "r")
    for line in infile:
        fileList.append(line.rstrip('\n'))

    infile.close()

    return fileList
# END load_list_from_file

# *************************** NO CODE FOLLOWS ***************************

