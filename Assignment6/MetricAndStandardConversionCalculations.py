"""
    Program: Metric And Standard Conversion Utility
    File: MetricAndStandardConversionCalculations.py
    Author: Jason J Welch
    Date: 9/30/2019
    Purpose: 
    
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


# ===================
def convert_kilogram_to_pounds(kilograms):
    pounds = kilograms * KG_TO_LB_CONVERSION
    return pounds
# END


# ===================
def convert_pounds_to_kilograms(pounds):
    kilograms = pounds * LB_TO_KG_CONVERSION
    return kilograms
# END

# ===================
def convert_grams_to_ounces(grams):
    ounces = grams * G_TO_OZ_CONVERSION
    return ounces
# END


# ===================
def convert_ounces_to_grams(ounces):
    grams = ounces * OZ_TO_G_CONVERSION
    return grams
# END


# ===================
def convert_grams_to_kilograms(grams):
    kilograms = grams / METRIC_CONVERSION
    return kilograms
# END


# ===================
def convert_kilograms_to_grams(kilograms):
    grams = kilograms * METRIC_CONVERSION
    return grams
# END


# ===================
def convert_ounces_to_pounds(ounces):
    pounds = ounces / OZ_IN_LB
    return pounds
# END


# ===================
def convert_pounds_to_ounces(pounds):
    ounces = pounds * OZ_IN_LB
    return ounces
# END


# ===================

# ===================

# ===================

# ===================

# ===================

# ===================

# ===================

# ===================

# ===================

# *************************** NO CODE FOLLOWS ***************************
