"""
    Program: Stadium Seating Price Calculator
    File: StadiumSeatingPriceCalculator.py
    Author: Jason J Welch
    Date: 9/23/2019
    Purpose: 
    
"""
CLASS_A_SEATS = 'A'
CLASS_B_SEATS = 'B'
CLASS_C_SEATS = 'C'

CLASS_A_PRICING = 20
CLASS_B_PRICING = 15
CLASS_C_PRICING = 10


# ==================== main() ===================
def main():
    runAgain = 'y'
    while runAgain.lower() == 'y':
        print("***************************************************************")
        print("\tStadium Seating Price Calculator")
        print("***************************************************************\n")
        # Get User Input
        seatACount = get_seat_count(CLASS_A_SEATS)
        seatBCount = get_seat_count(CLASS_B_SEATS)
        seatCCount = get_seat_count(CLASS_C_SEATS)

        # Calculate Ticket Total per Class
        aTotal = calculate_ticket_total(seatACount, CLASS_A_SEATS)
        bTotal = calculate_ticket_total(seatBCount, CLASS_B_SEATS)
        cTotal = calculate_ticket_total(seatCCount, CLASS_C_SEATS)

        display_results(aTotal, bTotal, cTotal)
        runAgain = input("\nDo you want to run again?(y/n): ")
    # End While runAgain
# End Main


# ==================== display_results() ===================
def display_results(totalA, totalB, totalC):
    print("\n***************************************************************\n")
    print(f"Seat A ticket sales total: ${totalA}")
    print(f"Seat B ticket sales total: ${totalB}")
    print(f"Seat C ticket sales total: ${totalC}")
    print("==========================")
    grandTotal = totalA + totalB + totalC
    print(f"Total Ticket sales: ${grandTotal}\n")
# End display_results


# ==================== calculate_ticket_total() ===================
def calculate_ticket_total(seatCount, seatClass):
    if seatClass == CLASS_A_SEATS:
        total = seatCount * CLASS_A_PRICING
    elif seatClass == CLASS_B_SEATS:
        total = seatCount * CLASS_B_PRICING
    else:
        total = seatCount * CLASS_C_PRICING
    return total
# End calculate_ticket_total


# ==================== get_seat_count() ===================
def get_seat_count(seatLetter):
    seatCount = input_number(f"How many tickets sold for Class {seatLetter} seats: ")
    return seatCount
# End get_input


# ==================== input_number() ===================
def input_number(message):
    while True:
        try:
            userInput = int(input(message))
        except ValueError:
            print("That is not a number! Please try again.")
            continue
        else:
            return userInput
            break
# end input_number


main()

# *************************** NO CODE FOLLOWS ***************************
