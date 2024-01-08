'''

@Author: Rohan Vetale

@Date: 2023-01-03 16:00:30

@Last Modified by: Rohan Vetale

@Last Modified time: 2023-01-03 16:00:30

@Title : Program to calculate windchill from given values

'''


import math

try:
    # Input temperature (t) and wind speed (v)
    temper = float(input("Enter the temperature in Fahrenheit: "))
    v = float(input("Enter the wind speed in miles per hour: "))
    
    # Check the validity of the inputs
    if abs(temper) > 50 or v < 3 or v > 120:
        print("Invalid input. Temperature (|t|) should be <= 50, and wind speed (v) should be between 3 and 120.")
    else:
        # Calculate the wind chill
        wind_chill = 35.74 + 0.6215 * temper - 35.75 * math.pow(v, 0.16) + 0.4275 * temper * math.pow(v, 0.16)
        
        # Print the result
        print(f"The wind chill is: {wind_chill}")

except ValueError:
    print("Invalid input. Please enter valid numerical values.")
