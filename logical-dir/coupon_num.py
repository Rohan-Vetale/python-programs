'''

@Author: Rohan Vetale

@Date: 2023-01-04 16:00:30

@Last Modified by: Rohan Vetale

@Last Modified time: 2023-01-04 16:00:30

@Title : Coupon Number problem of distinct numbers

'''

import random


num_digits = int(input("Enter a number between 1 and 9 : "))
def generateNum():
    if num_digits > 0 and num_digits < 10:
            # Calculate the range of numbers with the specified digits
            lower_bound = 10 ** (num_digits - 1)
            upper_bound = 10 ** num_digits - 1

            # Generate a random number within the specified range
            random_number = random.randint(lower_bound, upper_bound)

            #print(random_number) 
            if checkExists(random_number=random_number):
                generateNum()
            else:
                print(f"Final non-repeating random number is {random_number}")
            
    else:
        print("Invalid input. Please enter a positive number of digits between 1 and 9.")
    


def checkExists(random_number):
    """
        Description:
        This function is used to check the duplicate numbers

        Parameter:
        random_number : It is an integer

        Return:
        It returns true if the duplicate number is present
    """
    seen_digits = set()
    for char in str(random_number):
        if char in seen_digits:
            #print(f"Repeating char is {char} hence generating again")
            #print("Exists, generating again...")
            return True # Repeating number found
        seen_digits.add(char)
            
generateNum()

