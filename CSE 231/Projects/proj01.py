#################################################
#  Computer Project #1
#  Created on Wed May 17 14:45:44 2023
#  @author: Conner O'Sullivan
#  
#  Prompt for a float
#  input float
#  convert float to other units
#  display converted units
#################################################

rod_length_meter = 5.0292 # Rod length in meters
furlong_length_rods = 40 # Furlong length in rods
mile_length_meter = 1609.34 # Mile length in meters
foot_length_meter = 0.3048 # Foot length in meters
avg_walking_speed_mph = 3.1 # Average walking speed in miles per hour

rods = float(input("Input rods: ")) # Converts string input to float
print("\nYou input", rods, "rods.\n") 

meter_conversion = rods*rod_length_meter # Rods converted to meters
feet_conversion = meter_conversion/foot_length_meter # Rods converted to feet
miles_conversion = meter_conversion/mile_length_meter # Rods converted to miles
furlong_conversion = rods/furlong_length_rods # Rods converted to furlong
mins_to_walk = miles_conversion/(avg_walking_speed_mph/60) 
# Distance in miles divided by mph converted to mpm by dividing by 60

print("Conversions")
print("Meters:", round(meter_conversion,3))
print("Feet:", round(feet_conversion,3))
print("Miles:", round(miles_conversion,3))
print("Furlongs:", round(furlong_conversion,3))
print("Minutes to walk", rods, "rods:", round(mins_to_walk,3))
