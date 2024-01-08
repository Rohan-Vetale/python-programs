'''

@Author: Rohan Vetale

@Date: 2023-01-03 16:00:30

@Last Modified by: Rohan Vetale

@Last Modified time: 2023-01-03 16:00:30

@Title : Find euclidean distance from a given user input x and y

'''


import math

try:
    # Input two integer command-line arguments
    x = int(input("Enter the value of x: "))
    y = int(input("Enter the value of y: "))
    
    # Calculate Euclidean distance
    distance = math.sqrt(math.pow(x, 2) + math.pow(y, 2))
    
    # Print the result
    print(f"The Euclidean distance from the point ({x}, {y}) to the origin (0, 0) is: {distance}")

except ValueError:
    print("Invalid input. Please enter valid integers.")
