#########################################################################################
# Project #1
#
# Algorithm
#    prompt for floating-point value representing distance in rods
#    input floating-point value
#    output floating-point value from user i.e. "you input x rods"
#    output text "Conversions"
#    output conversion to Meters
#    output conversion to Feet
#    output conversion to Miles
#    output conversion to Furlongs
#    output Minutes to walk x rods where x is the floating point value input by the user
#########################################################################################

# Conversion of walking speed from miles/hour to miles/minute
AVERAGE_WALKING_SPEED = 3.1/60

# Receiving user input and converting to float
rods = float(input("Input rods: "))
print("You input", rods, "rods.")
print()

# Computing conversions and outputting to user
print("Conversions")
rods_in_meters = rods*5.0292
print("Meters:", round(rods_in_meters, 3))
print("Feet:", round(rods_in_meters/0.3048, 3))
rods_in_miles = rods_in_meters/1609.34
print("Miles:", round(rods_in_miles, 3))
print("Furlongs:", round(rods/40, 3))
print("Minutes to walk", rods, "rods:", round(rods_in_miles/AVERAGE_WALKING_SPEED, 3))
