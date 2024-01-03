'''

@Author: Rohan Vetale

@Date: 2023-01-03 10:00:30

@Last Modified by: Rohan Vetale

@Last Modified time: 2023-01-03 18:00:30

@Title : Find prime factors of given number

'''
# Input: Number to find the prime factors
number = int(input("Enter a number to find its prime factors: "))
input_num = number
factors = []

# Divide the number by 2 until it becomes odd
while number % 2 == 0:
    factors.append(2)
    number = number // 2

# Check for odd factors starting from 3
for i in range(3, int(number**0.5) + 1, 2):
    while number % i == 0:
        factors.append(i)
        number = number // i

# If the remaining number is a prime greater than 2
if number > 2:
    factors.append(number)

# Print the prime factors
print(f"Prime factors of {input_num}: {factors}")
