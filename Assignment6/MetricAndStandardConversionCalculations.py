"""
    Program: Metric And Standard Conversion Utility
    File: MetricAndStandardConversionCalculations.py
    Author: Jason J Welch
    Date: 9/30/2019
    Purpose: Collection of Methods to Convert Weights and Lengths from Metric to Standard, Standard to Standard,
        Metric to Metric.
    
"""


KM_TO_MI_CONVERSION = 1.609
M_TO_FT_CONVERSION = 3.281
CM_TO_IN_CONVERSION = 2.54

KG_TO_LB_CONVERSION = 2.204
G_TO_OZ_CONVERSION = .035
LB_TO_KG_CONVERSION = .4536
OZ_TO_G_CONVERSION = 28.375
OZ_IN_LB = 16

METRIC_CONVERSION = 10


# =================== convert_kilogram_to_pounds ===================
def convert_kilogram_to_pounds(kilograms):
    pounds = kilograms * KG_TO_LB_CONVERSION
    return pounds
# END convert_kilogram_to_pounds


# =================== convert_pounds_to_kilograms ===================
def convert_pounds_to_kilograms(pounds):
    kilograms = pounds * LB_TO_KG_CONVERSION
    return kilograms
# END convert_pounds_to_kilograms


# =================== convert_grams_to_ounces ===================
def convert_grams_to_ounces(grams):
    ounces = grams * G_TO_OZ_CONVERSION
    return ounces
# END convert_grams_to_ounces


# =================== convert_ounces_to_grams ===================
def convert_ounces_to_grams(ounces):
    grams = ounces * OZ_TO_G_CONVERSION
    return grams
# END convert_ounces_to_grams


# =================== convert_grams_to_kilograms ===================
def convert_grams_to_kilograms(grams):
    kilograms = grams / METRIC_CONVERSION
    return kilograms
# END convert_grams_to_kilograms


# =================== convert_kilograms_to_grams ===================
def convert_kilograms_to_grams(kilograms):
    grams = kilograms * METRIC_CONVERSION
    return grams
# END convert_kilograms_to_grams


# =================== convert_ounces_to_pounds ===================
def convert_ounces_to_pounds(ounces):
    pounds = ounces / OZ_IN_LB
    return pounds
# END convert_ounces_to_pounds


# =================== convert_pounds_to_ounces ===================
def convert_pounds_to_ounces(pounds):
    ounces = pounds * OZ_IN_LB
    return ounces
# END convert_pounds_to_ounces


# ===================
def convert_kilometers_to_miles(kilometers):
    miles = kilometers
    return miles
# END


# ===================
def convert_miles_to_kilometers(miles):
    kilometers = miles
    return kilometers
# END


# ===================
def convert_meters_to_feet(meters):
    feet = meters
    return feet
# END


# ===================
def convert_feet_to_meters(feet):
    meters = feet
    return meters
# END


# ===================
def convert_centimeters_to_inches(centimeters):
    inches = centimeters
    return inches
# END


# ===================
def convert_inches_to_centimeters(inches):
    centimeters = inches
    return centimeters
# END


# ===================
def convert_inches_to_feet(inches):
    feet = inches
    return feet
# END


# ===================
def convert_feet_to_inches(feet):
    inches = feet
    return inches
# END


# ===================

# END


# ===================

# END


# ===================

# END


# ===================

# END


# ===================

# END


# ===================

# END


# ===================

# END


# ===================

# END


# ===================

# END


# ===================

# END


# ===================

# END


# *************************** NO CODE FOLLOWS ***************************
