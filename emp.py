'''

@Author: Rohan Vetale

@Date: 2023-01-05 16:00:30

@Last Modified by: Rohan Vetale

@Last Modified time: 2023-01-05 16:00:30

@Title : Employee wage with Use Cases


'''
import random

def is_present():
    """
        Description:
        This function is used to tell whether the employee is present or not

        Parameter:
        None

        Return:
        It returns a boolean value True or False based on random.choice()
    """
    
    return random.choice([True, False])

try:
    if is_present() :
        print("Employee is present today")
    else:
        print("Employee is absent today")
        
except Exception as e:
    print(f"Exception occured {e} please try again")
    