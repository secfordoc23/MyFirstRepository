'''
    Program: Read Declaration
    File: ReadDeclaration.py
    Author: Jason J. Welch
    Date: 10/10/2019
    Purpose: To read lines from the Declararion of Independence
      
'''

from InputValidation import *


# ==================== main ====================
def main():
    while True:
        print("***************************************************************")
        print("\tDeclaration Of Independence Reader")
        print("***************************************************************")

        # Validate File name
        inFile = input_filename("Enter the name of a file: ", "r")

        # Read first line of input
        line = inFile.readline()
        counter = 1

        # Loop till file is empty or 10 lines have been read.
        while line != '' and counter <= 10:
            print("{0}: {1}".format(counter, line.rstrip('\n')))
            line = inFile.readline()
            counter += 1

        # Close File
        inFile.close()

        # Run Again?
        runAgain = input("Run Again?(y/n): ")
        if runAgain != 'y' or runAgain != 'Y':
            break
# END main


main()
