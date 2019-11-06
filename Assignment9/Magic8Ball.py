"""
    Program: Magic 8 Ball
    File: Magic8Ball.py
    Author: Jason J Welch
    Date: 10/28/2019
    Purpose: A simple magic 8 ball program that reads responses from a file.
    
"""
import random
from InputValidation import *


# ================== main ==================
def main():
    fileName = "8_ball_responses.txt"
    while True:
        print("***************************************************************")
        print("\tMagic 8 Ball")
        print("***************************************************************")
        userSelection = display_menu(["Ask a Question", "Exit"])
        if userSelection == 1:
            responseList = load_list_from_file(fileName)
            ball_response(responseList)
        else:
            break


# END main

# ================== ball_response ==================
def ball_response(responseList):
    selectedRandomResponse = random.randint(0, len(responseList) - 1)
    userQuestion = input("Enter your question for the Magic 8 Ball: ")
    print(f"\nThe Magic 8 Ball says:\n\t{responseList[selectedRandomResponse]}\n")
# END ball_response


main()
# *************************** NO CODE FOLLOWS ***************************
