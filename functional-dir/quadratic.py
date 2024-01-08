'''

@Author: Rohan Vetale

@Date: 2023-01-03 16:00:30

@Last Modified by: Rohan Vetale

@Last Modified time: 2023-01-03 16:00:30

@Title : Find quadratic from a given user input a, b, c

'''


import math

try:
    # Input coefficients a, b, and c
    a = float(input("Enter the value of a: "))
    b = float(input("Enter the value of b: "))
    c = float(input("Enter the value of c: "))
    
    # Calculate the discriminant (delta)
    delta = b**2 - 4*a*c
    
    # Check if roots are real
    if delta >= 0:
        # Calculate the roots
        root1 = (-b + math.sqrt(delta)) / (2*a)
        root2 = (-b - math.sqrt(delta)) / (2*a)
        
        # Print the roots
        print(f"Root 1 of x: {root1}")
        print(f"Root 2 of x: {root2}")
    else:
        # If the discriminant is negative, roots are complex
        real_part = -b / (2*a)
        imaginary_part = math.sqrt(abs(delta)) / (2*a)
        
        # Print complex roots
        print(f"Root 1 of x: {real_part} + {imaginary_part}i")
        print(f"Root 2 of x: {real_part} - {imaginary_part}i")

except ValueError:
    print("Invalid input. Please enter valid numerical values.")
