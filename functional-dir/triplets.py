'''

@Author: Rohan Vetale

@Date: 2023-01-03 16:00:30

@Last Modified by: Rohan Vetale

@Last Modified time: 2023-01-03 16:00:30

@Title : Take an array and print the possible triplets to get sum 0

'''

try:
    n = int(input("Enter the number of integers: "))
    numbers = [int(input(f"Enter integer {i + 1}: ")) for i in range(n)]

    triplets = []

    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                if numbers[i] + numbers[j] + numbers[k] == 0:
                    triplet = (numbers[i], numbers[j], numbers[k])
                    if triplet not in triplets:  # Avoid duplicates
                        triplets.append(triplet)

    print(f"Number of distinct triplets: {len(triplets)}")
    print("Distinct triplets:")
    for triplet in triplets:
        print(triplet)

except ValueError:
    print("Invalid input. Please enter valid integers.")

