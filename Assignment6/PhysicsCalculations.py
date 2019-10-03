"""
    Program: Physics Utility
    File: PhysicsCalculations.py
    Author: Jason J Welch
    Date: 9/30/2019
    Purpose: Collection of methods to perform physics calculations
    
"""

GRAVITATIONAL_ACCELERATION = 9.8

# =================== calculate_falling_distance ===================
def calculate_falling_distance(fallingTime):
    """
    Formula: d = 1/2 gt^2
    d = distance in meters, g = 9.8, t = time object has been falling in seconds
    param: time object has been falling in seconds
    return: distance in meters
    """
    distance = (1/2) * GRAVITATIONAL_ACCELERATION * fallingTime ** 2
    return distance
# End calculate_falling_distance


# =================== calculate_kinetic_energy ===================
def calculate_kinetic_energy(mass, velocity):
    """
    Formula: KE = 1/2 mv^2
    KE = Kinetic Energy, m = objects mass in kilograms, v = velocity in meters per second
    param: objects mass in kilograms
    param: velocity in meters per second
    return: Kinetic Energy
    """
    kineticEnergy = (1/2) * mass * velocity ** 2
    return kineticEnergy
# END calculate_kinetic_energy

# *************************** NO CODE FOLLOWS ***************************
