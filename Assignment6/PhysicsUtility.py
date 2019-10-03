"""
    Program: Physics Utility
    File: PhysicsUtility.py
    Author: Jason J Welch
    Date: 9/30/2019
    Purpose: 
    
"""
from PhysicsCalculations import *
from InputValidation import *

# =================== main() ===================
def main():

    while True:
        print("***************************************************************")
        print("\tPhysics Utility")
        print("***************************************************************")

        print("\nMenu:")
        print("\t1. Calculate the Falling Distance of an Object")
        print("\t2. Calculate the Kinetic Energy of an Object")
        print("\t3. Exit")
        userSelection = input_menu_option("Enter Selection: ", 3)
        if userSelection == 1:
            falling_distance()
        elif userSelection == 2:
            kinetic_energy()
        else:
            break

# END main


# =================== falling_distance() ===================
def falling_distance():
    print("\nThe Formula: d = 1/2gt^2")
    time = input_decimal("Enter the the length of time the object was falling in seconds: ")
    distance = calculate_falling_distance(time)
    print(f"The object has fallen {distance} meters.\n")
# END falling_distance()


# =================== kinetic_energy() ===================
def kinetic_energy():
    print("\nThe Formula: KE = 1/2mv^2")
    mass = input_decimal("Enter the mass of the object in kilograms: ")
    velocity = input_decimal("Enter the velocity of the object in meters per second: ")
    kineticEnergy = calculate_kinetic_energy(mass, velocity)
    print(f"The object has {kineticEnergy} Kinetic Energy.\n")
# END kinetic_energy()


main()

# *************************** NO CODE FOLLOWS ***************************
