"""
    Program: Charge Account Validation
    File: ChargeAccountValidation.py
    Author: Jason J Welch
    Date: 10/21/2019
    Purpose: A program to read a given list of charge account numbers and ask for a user to enter a charge account
        number and verify if the number is in the list.
    
"""
from InputValidation import *


def main():
    filename = "charge_accounts.txt"
    while True:
        print("***************************************************************")
        print("\tCharge Account Validation")
        print("***************************************************************")
        userSelection = display_menu(["Find a Charge Account Number", "Exit"])
        if userSelection == 1 and does_file_exist(filename):
            chargeAccountList = get_charge_account_numbers(filename)
            accountToFind = input("Enter an account to find: ")
            if accountToFind in chargeAccountList:
                print("\nValid Charge Account!\n")
            else:
                print("\nUnable to find entered account number.  Please try again.\n")
        else:
            break

# END main


def get_charge_account_numbers(filename):
    infile = open(filename, "r")

    chargeAccountList = infile.readline()

    infile.close()

    return chargeAccountList
# END get_charge_account_numbers


main()
# *************************** NO CODE FOLLOWS ***************************
