"""
    Program: Sum and Average Of Numbers Calculator
    File: SumAndAverageOfNumbersCalculator.py
    Author: Jason J Welch
    Date: 10/14/2019
    Purpose: A program to read and write a file with integers, upon reading the file calculate the sum and average of
        the numbers.
    
"""
from InputValidation import *


# ================== main() ==================
def main():
    while True:
        print("***************************************************************")
        print("\tSum And Average Of Numbers Calculator")
        print("***************************************************************\n")

        print("Options: ")
        print("\t1. Create a file with integers")
        print("\t2. Calculate the Sum and Average of a file with integers")
        print("\t3. Quit")
        selection = input_menu_option("Enter Selection: ", 3)
        if selection == 1:  # Read from file with numbers
            write_file_option()
        elif selection == 2:  # Write to a file with numbers
            read_file_option()
        else:  # If selection is 3 exit
            break

# End main


# ================== read_file_option() ==================
def read_file_option():
    inFile = input_filename("Enter a the name of the file: ", "r")
    sum = 0

    line = inFile.readline()
    counter = 0
    # Loop till file is empty.
    while line != '':
        sum += parse_int(line)
        counter += 1
        line = inFile.readline()

    # Close the file after reading
    inFile.close()

    print("File has been read.\n")

    print(f"The sum of the numbers in the file are {sum}")
    average = sum / counter
    print(f"The average of the numbers in the file are {average}\n")
# END read_file_menu


# ================== write_file_option() ==================
def write_file_option():
    outFile = input_filename("Enter the name of the file to be created: ", "w")

    while True:
        print("Options: ")
        print("\t1. Enter a integer")
        print("\t2. Done")
        selection = input_menu_option("Enter Selection: ", 2)

        if selection == 1:
            number = input_number("Enter a number: ")
            outFile.write(str(number) + "\n")
        else:
            break

    # Close the file
    outFile.close()
# END write_file_menu


main()
# *************************** NO CODE FOLLOWS ***************************
