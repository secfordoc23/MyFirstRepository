"""
    Program: AcmePaintJobEstimator
    File: AcmePaintJobEstimator.py
    Author: Jason J Welch
    Date: 9/19/2019
    Purpose: Program to estimate the cost of a paint job from user input of
    size of the building, cost of the paint, labor rate, hours,and gallons of paint
    
"""


# ==================== main() ===================
def main():
    runAgain = 'y'
    while runAgain.lower() == 'y':
        print("***************************************************************")
        print("\tAcme Paint Job Calculator")
        print("***************************************************************\n")

        length = get_footage("long")
        width = get_footage("high")
        square_feet = calculate_square_footage(length, width)

        cost_per_gallon = input_number("What does a gallon of paint cost?: ")

        gallons_needed = get_gallons(square_feet)

        paint_cost = calculate_paint_cost(cost_per_gallon, gallons_needed)
        hours_worked = get_hours(square_feet)
        payroll_cost = get_payroll(hours_worked)

        output_details(square_feet, cost_per_gallon, gallons_needed,
                       paint_cost, hours_worked, payroll_cost)
        runAgain = input("Do you want to run again?(y/n): ")
    # End While runAgain
# end Main


# ==================== get_footage() ===================
def get_footage(choice):
    if choice == "long":
        userInput = input_number("Enter the length of surface: ")
    else:
        userInput = input_number("Enter the width of surface: ")
    return userInput
# end get_footage


# ==================== input_number() ===================
def input_number(message):
    while True:
        try:
            userInput = float(input(message))
        except ValueError:
            print("That is not a number! Please try again.")
            continue
        else:
            return userInput
            break
# end input_number


# ==================== calculate_sq_feet()
def calculate_square_footage(length, width):
    sq_feet = length * width
    return sq_feet
# end calculate_sq_feet


# ==================== get_gallons()
def get_gallons(area):
    AREA_PER_GALLON = 112
    total_gallons = area / AREA_PER_GALLON

    if total_gallons % 1 != 0:
        total_gallons = int(total_gallons) + 1

    return total_gallons
# end get_gallons


# ==================== calculate_paint_cost()
def calculate_paint_cost(cost_per_gallon, gallons):
    total_cost = cost_per_gallon * gallons
    return total_cost
# end calculate_paint_cost


# ====================
def get_payroll(hours):
    PAYRATE = 35.00
    total_pay = hours * PAYRATE
    return total_pay
# end get_payroll


# ====================
def get_hours(area):
    SQFT_PER_8HOURS = 112
    hours = (area / SQFT_PER_8HOURS) * 8
    return hours
# end    ​


# ==================== output_details
def output_details(square_feet, cost_per_gallon, gallons_needed,
                   paint_cost, hours_worked, payroll_cost):
    job_cost = paint_cost + payroll_cost

    print("\nJob Estimate:")
    print(f"\tSquare Feet: {square_feet}")
    print(f"\tPaint Cost: ${paint_cost}")
    print(f"\t\t*Based on {cost_per_gallon} per gallon and {gallons_needed} gallons needed.")
    print(f"\tMan Hours: {hours_worked}")
    print(f"\tPayroll: ${payroll_cost}")
    print("===========================")
    print(f"\tTotal Cost: ${job_cost}")
# end


main()
# *************************** NO CODE FOLLOWS ***************************
