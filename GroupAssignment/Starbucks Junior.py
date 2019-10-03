"""
    Program: Starbucks Junior
    File: StarbucksJunior.py
    Author: Jason J Welch, Rita Allen, Eric Gavin
    Date: 9/26/2019
    Purpose: we are selling coffee for $2.00, tea for $1.75, and latte for $4.00;
         in three sizes: tall with price factor of 1, grande with price factor
         of 1.5, venti for price factor of 2

"""

from Validation import *

# constant variables
COFFEE_PRICE = 2.00
TEA_PRICE = 1.75
LATTE_PRICE = 4.00

TALL_PRICE_FACTOR = 1
GRANDE_PRICE_FACTOR = 1.5
VENTI_PRICE_FACTOR = 2

orderDescription = ""


# ============= main ================================
def main():

    while True:
        print("***************************************************************")
        print("\t*** STARBUCKS JUNIOR ***")
        print("\t*** Point of Sales ***")
        print("***************************************************************\n")

        print("*** Initial Menu ***")
        print("\t1. Place Order")
        print("\t2. Exit")
        userSelection = input_menu_option("Option Selection: ", 2)

        if userSelection == 2:
            break

        orderTotal = place_order()
        display_order(orderTotal)
# END main


# =========== place_order ===============================
def place_order():
    orderTotal = 0
    while True:
        print("Current Order:")
        print(orderDescription, "\n")
        print("*** Order Menu ***")
        print("\t1. Coffee")
        print("\t2. Tea")
        print("\t3. Latte")
        print("\t4. Order Complete")

        itemSelection = input_menu_option("Option Selection: ", 4)
        if itemSelection == 4:
            break
        sizeSelection = size_menu()
        orderTotal += float(calculate_order(sizeSelection, itemSelection))
    return orderTotal
# END place_order


# ============ calculate_order ========================
def calculate_order(sizeSelection, itemSelection):
    global orderDescription

    if sizeSelection == 1:
        size = "Tall"
        factor = TALL_PRICE_FACTOR
    elif sizeSelection == 2:
        size = "Grande"
        factor = GRANDE_PRICE_FACTOR
    else:
        size = "Venti"
        factor = VENTI_PRICE_FACTOR

    if itemSelection == 1:
        item = "Coffee"
        price = COFFEE_PRICE
    elif itemSelection == 2:
        item = "Tea"
        price = TEA_PRICE
    else:
        item = "Latte"
        price = LATTE_PRICE

    total = price * factor
    orderDescription += "{} {} - ${:0,.2f}\n".format(size, item, total)
    return total
# END calculate_order


# ============ size_initial_menu ==========================
def size_menu():
    print("\n*** Size Menu ***")
    print("\t1. Tall")
    print("\t2. Grande")
    print("\t3. Venti")

    sizeSelection = input_menu_option("Select size: ", 3)
    return sizeSelection
# END size_initial_menu


# ============ display_order ==========================
def display_order(total):
    print("\n**** RECEIPT ****")
    print(orderDescription)
    print("==================")
    print("Order Total: ${,.2f}\n\n".format(total))
# END display_order

# call main function
main()
