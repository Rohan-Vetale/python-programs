'''

@Author: Rohan Vetale

@Date: 2023-01-03 16:00:30

@Last Modified by: Rohan Vetale

@Last Modified time: 2023-01-03 16:00:30

@Title : Input and print a 2d array

'''

# Input: Number of rows and columns
rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))

# Initialize an empty 2D array
array_2d = []

# Read input for the 2D array
for i in range(rows):
    row = []
    for j in range(cols):
        # Taking input for each element in the 2D array
        element = input(f"Enter element at position {i + 1}, {j + 1}: ")
        row.append(element)
    array_2d.append(row)

# Print the 2D array
print("2D Array:")
for row in array_2d:
    for element in row:
        # Printing each element in the 2D array
        print(element, end=" ")
    print()
